# DVL A50

## Dimensions

![dvl_a50_dimensions](../img/WL-21035-3_DVL-A50_Side3_1600_dimension_crop.jpg)

### Cable dimensions
Delivered cable length: 3.0 m

Cable diameter: 6.8 mm +/- 0.2 mm


## Mounting holes

![dvl_a50_mounting_holes_drawing](../img/dvl_mounting_holes_drawing.png)


## Transducer numbering

![dvl_a50_transducer_numbering](../img/WL-21035-3_DVL-A50_Front_1600_transducers_crop.jpg)

Mechanical drawings number the transducers from 1 to 4. Protocol messages and diagnostic logs use zero-based transducer `id` values from 0 to 3. See [Transducer numbering and protocol IDs](axes.md#transducer-numbering-and-protocol-ids).

## Transducer beam width

![dvl_a50_transducer_beam](../img/DVL-A50--Transducer-Beam-Width.png)

Half-power beam width is 4.4°


## Line of sight

Keep a 65° cone below the transducers free of obstructions. The cone starts at the outer edge of the housing face, and the drawing is to scale.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 420" fill="currentColor" font-size="12" style="max-width: 680px;" role="img" aria-label="DVL A50 line of sight, side view: keep a 65 degree cone below the transducers free">
  <defs><marker id="los-dvla50-a" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z"/></marker><marker id="los-dvla50-b" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto"><path d="M6,0 L0,3 L6,6 Z"/></marker></defs>
  <text x="20" y="24" font-size="14" font-weight="bold">DVL A50 line of sight (side view)</text>
  <text x="20" y="42" font-size="11" opacity="0.75">Mounting side up, transducers facing the seabed. Drawn to scale against the other DVL models.</text>
  <polygon points="287.2,116.0 392.8,116.0 561.0,380.0 119.0,380.0" fill="currentColor" fill-opacity="0.07" stroke="none"/>
  <line x1="287.2" y1="116.0" x2="119.0" y2="380.0" stroke="currentColor" stroke-width="1.4"/>
  <line x1="392.8" y1="116.0" x2="561.0" y2="380.0" stroke="currentColor" stroke-width="1.4"/>
  <path d="M207.5,241.1 A246.6,246.6 0 0 0 472.5,241.1" fill="none" stroke="currentColor" stroke-width="0.8" marker-start="url(#los-dvla50-a)" marker-end="url(#los-dvla50-b)"/>
  <text x="340" y="297.7" text-anchor="middle" font-size="13" font-weight="bold">65°</text>
  <text x="340" y="402.0" text-anchor="middle" font-size="11">Keep this 65° cone free of brackets, frames, cables, thrusters and hull</text>
  <g stroke="currentColor" stroke-width="0.9" stroke-dasharray="5 4" opacity="0.8">
    <line x1="378.3" y1="122.0" x2="457.3" y2="312.7"/>
    <line x1="301.7" y1="122.0" x2="222.7" y2="312.7"/>
    <line x1="378.3" y1="122.0" x2="378.3" y2="182.0" stroke-dasharray="2 3"/>
  </g>
  <path d="M378.3,168.0 A46,46 0 0 0 395.9,164.5" fill="none" stroke="currentColor" stroke-width="0.8"/>
  <text x="402.3" y="186.0" font-size="11">22.5°</text>
  <text x="467.3" y="314.7" font-size="11" opacity="0.85">Beam axis</text>
  <path d="M287.2,88.0 L392.8,88.0 L392.8,116.0 L363.8,128.0 L316.2,128.0 L287.2,116.0 Z" fill="currentColor" fill-opacity="0.18" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
  <g stroke="currentColor" stroke-width="3.2" stroke-linecap="round">
    <line x1="389.3" y1="117.4" x2="367.2" y2="126.6"/>
    <line x1="290.7" y1="117.4" x2="312.8" y2="126.6"/>
  </g>
  <line x1="287.2" y1="76.0" x2="392.8" y2="76.0" stroke="currentColor" stroke-width="0.7" marker-start="url(#los-dvla50-b)" marker-end="url(#los-dvla50-a)"/>
  <text x="340" y="71.0" text-anchor="middle" font-size="11">Ø66 mm</text>
  <line x1="406.8" y1="88.0" x2="406.8" y2="128.0" stroke="currentColor" stroke-width="0.7" marker-start="url(#los-dvla50-b)" marker-end="url(#los-dvla50-a)"/>
  <text x="412.8" y="112.0" font-size="11">25 mm</text>
  <text x="277.2" y="100.0" text-anchor="end" font-size="11" opacity="0.85">Mounting side</text>
  <text x="267.5" y="132.0" text-anchor="end" font-size="11" opacity="0.85">Transducers</text>
</svg>

## Datasheet

[Datasheet](https://waterlinked.com/dvl-a50#Downloads-%2F-Resources%E2%80%8B)
