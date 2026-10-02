/* UGPS system selector engine
 * ---------------------------------------------------------------------------------------
 * Generic, data-driven: every product name, number and rule lives in the page's
 * <script type="application/json" id="ugps-selector-data"> block, next to the prose.
 * This file only knows the contract (loop/G001_ugps-system-selector/round-1/plan.md §3):
 *
 * DOM   #ugps-selector[hidden] (root; `hidden` removed when the engine starts)
 *       fieldset.sel-q[data-q=qN] with one radio group name=qN; last option value "unsure"
 *       #sel-progress, #sel-reset, #sel-result, #sel-summary, #sel-<list>-block / #sel-<list>
 *       for warnings, equipment, considerations, reasons; #sel-accuracy-block / #sel-accuracy.
 * DATA  questions[{id, short, if?}] — `if` {qN:[values]} hides the fieldset (and clears it);
 *       links{key:{label, href}}; rules[{id, when, then}]; equipmentBase[{text, link}];
 *       accuracy{<edition>:{base, <q7 value>…}, static, depth}.
 * RULES run in order. `when` matches when every key holds: qN against the current answer
 *       (unanswered or hidden ⇒ "unsure"); the key `locator` against the locator so far
 *       ("U1" | "A1" | "D1" | "none"). On match: locator/baseline/edition are set only if
 *       still null unless then.override; then.withhold sets withhold and clears all three;
 *       addons/considerations/warnings append (warnings deduped by id); reason appends
 *       "<reason> (from: <short labels of the when keys, locator excluded>)".
 * RENDER on every change: progress "<answered> of <visible> answered"; placeholder summary
 *       until one visible question is answered; equipment = equipmentBase + locator +
 *       baseline + addons; {text, link} resolves link via `links` (missing ⇒ plain text,
 *       http(s) ⇒ rel=noopener); empty blocks hidden; withhold ⇒ .sel-withheld, equipment,
 *       considerations and accuracy hidden (only summary, warnings and reasons remain);
 *       accuracy = [edition||R100].base + [q7 answer] + static (if q8=fixed or q5=indoors)
 *       + depth. "Start over" clears every radio and re-renders.
 * No dependencies, no inline handlers; all text goes through textContent (never innerHTML).
 */
(function () {
  'use strict';

  var UNSURE = 'unsure';
  var ACC = { position: 'q7', mounting: 'q8', environment: 'q5', fixed: 'fixed', indoors: 'indoors' };

  function init() {
    var root = document.getElementById('ugps-selector');
    var dataEl = document.getElementById('ugps-selector-data');
    if (!root || !dataEl) { return; }
    var data;
    try { data = JSON.parse(dataEl.textContent); } catch (e) { return; }
    var questions = data.questions || [];
    var links = data.links || {};
    var rules = data.rules || [];
    var el = function (id) { return document.getElementById(id); };
    var summary = el('sel-summary');
    var placeholder = summary ? summary.textContent : '';
    var result = el('sel-result');

    function fieldset(id) { return root.querySelector('fieldset[data-q="' + id + '"]'); }
    function radios(id) { return root.querySelectorAll('input[type="radio"][name="' + id + '"]'); }
    function answer(id) {
      var r = root.querySelector('input[type="radio"][name="' + id + '"]:checked');
      return r ? r.value : null;
    }
    function eff(id) { return answer(id) || UNSURE; }
    function has(list, v) { return Array.isArray(list) && list.indexOf(v) !== -1; }
    function clear(id) { var rs = radios(id); for (var i = 0; i < rs.length; i++) { rs[i].checked = false; } }
    function short(id) {
      for (var i = 0; i < questions.length; i++) { if (questions[i].id === id) { return questions[i].short || id; } }
      return id;
    }

    /* Apply the `if` conditions in question order; hidden fieldsets are cleared so they
       read as "unsure". Returns {visible, answered}. */
    function applyVisibility() {
      var visible = 0, answered = 0;
      for (var i = 0; i < questions.length; i++) {
        var q = questions[i], fs = fieldset(q.id), show = true;
        if (q['if']) { for (var k in q['if']) { if (!has(q['if'][k], eff(k))) { show = false; } } }
        if (!show) { clear(q.id); }
        if (fs) { fs.hidden = !show; }
        if (show) { visible++; if (answer(q.id)) { answered++; } }
      }
      return { visible: visible, answered: answered };
    }

    function evaluate() {
      var s = { locator: null, baseline: null, edition: null, withhold: false,
                addons: [], considerations: [], warnings: [], reasons: [] };
      var seen = {};
      for (var i = 0; i < rules.length; i++) {
        var rule = rules[i], when = rule.when || {}, then = rule.then || {}, ok = true, from = [];
        for (var k in when) {
          var cur = (k === 'locator') ? (s.locator || 'none') : eff(k);
          if (!has(when[k], cur)) { ok = false; break; }
          if (k !== 'locator') { from.push(short(k)); }
        }
        if (!ok) { continue; }
        ['locator', 'baseline', 'edition'].forEach(function (key) {
          if (then[key] != null && (s[key] === null || then.override)) { s[key] = then[key]; }
        });
        if (then.withhold) { s.withhold = true; s.locator = s.baseline = s.edition = null; }
        s.addons = s.addons.concat(then.addons || []);
        s.considerations = s.considerations.concat(then.considerations || []);
        (then.warnings || []).forEach(function (w) {
          if (w.id && seen[w.id]) { return; }
          if (w.id) { seen[w.id] = true; }
          s.warnings.push(w);
        });
        if (then.reason) { s.reasons.push({ text: then.reason + (from.length ? ' (from: ' + from.join(', ') + ')' : '') }); }
      }
      return s;
    }

    /* A product value ("U1", "antenna", "4× Receiver-D1") → its `links` entry, by key
       (case-insensitive) or by label; null when unknown. */
    function linkFor(key) {
      if (!key) { return null; }
      if (links[key]) { return links[key]; }
      var lower = String(key).toLowerCase();
      for (var k in links) {
        if (k.toLowerCase() === lower || String(links[k].label).toLowerCase() === lower) { return links[k]; }
      }
      return null;
    }
    function anchor(link, text) {
      var a = document.createElement('a');
      a.href = link.href; a.textContent = text || link.label || link.href;
      if (/^https?:/i.test(link.href)) { a.rel = 'noopener'; a.target = '_blank'; }
      return a;
    }
    /* {text, link}: equipment lines become the link itself; other lines get " · label". */
    function item(entry, asLink) {
      var li = document.createElement('li'), link = linkFor(entry.link);
      if (link && asLink) { li.appendChild(anchor(link, entry.text)); }
      else {
        li.appendChild(document.createTextNode(entry.text || ''));
        if (link) { li.appendChild(document.createTextNode(' · ')); li.appendChild(anchor(link)); }
      }
      return li;
    }
    function warning(w) {
      var li = document.createElement('li'), strong = document.createElement('strong'), link = linkFor(w.link);
      li.className = 'sel-warning';
      strong.textContent = w.title || '';
      li.appendChild(strong);
      li.appendChild(document.createTextNode((w.title && w.text ? ' — ' : '') + (w.text || '')));
      if (link) { li.appendChild(document.createTextNode(' · ')); li.appendChild(anchor(link)); }
      return li;
    }
    function fill(name, nodes) {
      var list = el('sel-' + name), block = el('sel-' + name + '-block');
      if (!list) { return; }
      while (list.firstChild) { list.removeChild(list.firstChild); }
      nodes.forEach(function (n) { list.appendChild(n); });
      if (block) { block.hidden = nodes.length === 0; }
    }
    function para(text) { var p = document.createElement('p'); p.textContent = text; return p; }

    function render() {
      var count = applyVisibility(), progress = el('sel-progress');
      if (progress) { progress.textContent = count.answered + ' of ' + count.visible + ' answered'; }
      var started = count.answered > 0;
      var s = started ? evaluate() : { withhold: false, addons: [], considerations: [], warnings: [], reasons: [] };
      if (result) { result.classList.toggle('sel-withheld', !!s.withhold); }

      var loc = linkFor(s.locator), base = linkFor(s.baseline);
      if (summary) {
        if (!started) { summary.textContent = placeholder; }
        else if (s.withhold || !s.locator) { summary.textContent = 'No recommendation yet — see the warnings'; }
        else {
          summary.textContent = 'Recommended: Locator-' + s.locator +
            (s.baseline ? ' with ' + (base ? base.label : s.baseline) : '') +
            (s.edition ? ', ' + s.edition + ' edition' : '');
        }
      }

      var equipment = [];
      if (started && !s.withhold) {
        (data.equipmentBase || []).forEach(function (e) { equipment.push(item(e, true)); });
        if (s.locator) { equipment.push(item({ text: loc ? loc.label : 'Locator-' + s.locator, link: s.locator }, true)); }
        if (s.baseline) { equipment.push(item({ text: base ? base.label : s.baseline, link: s.baseline }, true)); }
        s.addons.forEach(function (e) { equipment.push(item(e, true)); });
      }
      fill('warnings', s.warnings.map(warning));
      fill('equipment', equipment);
      fill('considerations', s.withhold ? [] : s.considerations.map(function (e) { return item(e, false); }));
      fill('reasons', s.reasons.map(function (e) { return item(e, false); }));

      var acc = data.accuracy || {}, paras = [];
      if (started && !s.withhold) {
        var ed = acc[s.edition || 'R100'] || {};
        if (ed.base) { paras.push(para(ed.base)); }
        if (ed[eff(ACC.position)]) { paras.push(para(ed[eff(ACC.position)])); }
        if (acc['static'] && (eff(ACC.mounting) === ACC.fixed || eff(ACC.environment) === ACC.indoors)) { paras.push(para(acc['static'])); }
        if (acc.depth) { paras.push(para(acc.depth)); }
      }
      fill('accuracy', paras);
    }

    root.addEventListener('change', render);
    var reset = el('sel-reset');
    if (reset) {
      reset.addEventListener('click', function () {
        questions.forEach(function (q) { clear(q.id); });
        render();
      });
    }
    root.hidden = false;
    render();
  }

  if (document.readyState === 'loading') { document.addEventListener('DOMContentLoaded', init); }
  else { init(); }
})();
