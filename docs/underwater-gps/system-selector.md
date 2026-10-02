# Choose your UGPS G2 setup

A UGPS G2 system is one [UGPS G2 Topside](../underwater-gps/ugps-topside.md), one baseline ([Antenna](../underwater-gps/antenna.md) or 4× [Receiver-D1](../underwater-gps/receiver-d1.md)), one locator and a range edition (R100 or R300). This page helps you pick the combination that fits your job. The table and the list below cover the main choices. The interactive guide further down asks a few questions and suggests a setup with an equipment list and the things to think about.

## Locators at a glance

| Feature | [Locator-U1](../underwater-gps/locators/locator-u1.md) | [Locator-A1](../underwater-gps/locators/locator-a1.md) | [Locator-D1](../underwater-gps/locators/locator-d1.md) |
|---|---|---|---|
| **Connection** | Wireless, battery powered (USB-C charge, 5 V/2 A), mounting bracket | 2-wire analog signal cable to the topside Locator port, 1 m open-ended (custom lengths to order). Can run through a spare twisted pair in a tether | Digital, powered by the topside, 50 m or 100 m integrated cable to the topside Locator port |
| **Depth** | Own pressure sensor, sent acoustically | No pressure sensor. Depth must be fed through the [API](../underwater-gps/integration/api.md) from the vehicle's depth sensor | Own pressure sensor |
| **Time sync** | GPS lock on the Locator-U1 before deployment (solid green LED) and GNSS lock on the topside during the whole mission | Through the cable, no GNSS needed | Through the cable, no GNSS needed |
| **Max. submerged time** | About 6 hours (battery, drying of the pressure sensor, time sync) | No limit stated | About 6 hours, then let the pressure sensor dry |
| **Signal range** | 300 m (depth rating 200 m) | 300 m (depth rating 300 m) | 100 m, limited by the cable (depth rating 300 m) |
| **Size** | 13.3 cm × Ø3.2 cm | Smallest: Ø20 mm × 41 mm, 30 g | Ø32 mm × 121 mm, 175 g |
| **BlueROV2 Integration Kit** | Usable for the network part, see the [Locator-U1 guide](../underwater-gps/integration/bluerov-integration-u1.md) | Yes, see the [Locator-A1 guide](../underwater-gps/integration/bluerov-integration-a1.md) | **Not compatible** |
| **Integration into other vehicles** | Mount only | Your responsibility: the analog signal must reach the topside | Your responsibility: the digital cable must reach the topside |

!!! Note
    Only the BlueROV2 has an integration guide. Integrating a locator into any other vehicle, including routing the signal through your own tether or cable, is your responsibility and at your own risk.

## Which locator when

* **Diver, swimmer or untethered object, outdoors:** Locator-U1. It needs GPS lock before deployment and the topside needs GNSS lock during the whole mission.
* **Tethered vehicle with a spare twisted pair and a depth sensor you can send over the API:** Locator-A1. On a BlueROV2, use the BlueROV2 Integration Kit and the [Locator-A1 guide](../underwater-gps/integration/bluerov-integration-a1.md).
* **Tethered vehicle with no depth source, or where a separate cable is fine:** Locator-D1 with its 50 m or 100 m cable. The range is then limited to 100 m, so choose the R100 edition. A 300 m upgrade can be purchased later if you change locator. The Locator-D1 is not compatible with the BlueROV2 Integration Kit.
* **Indoors, in a tank or a pool:** Locator-A1 or Locator-D1 with the topside in Static mode. The Locator-U1 cannot sync its clock without GNSS.
* **Several objects:** one locator per object, each on a different channel (7 channels). Only one locator is tracked at a time; switch between them in the GUI.
* **Topside on a moving boat:** feed [external compass and GNSS](../underwater-gps/integration/external-gps.md) through the API, whatever the locator.

## Interactive guide

Answer the questions that apply. Every question has a "Not sure" option, you can change any answer at any time, and the result updates as you go.

<noscript><p>The interactive guide needs JavaScript. Use the table and list above.</p></noscript>
<div id="ugps-selector" class="sel" hidden>
  <p id="sel-progress" class="sel-progress" aria-live="polite">0 of 7 answered</p>
  <fieldset class="sel-q" data-q="q1"><legend>1. What do you want to track?</legend>
    <label><input type="radio" name="q1" value="rov"> Tethered ROV or crawler</label>
    <label><input type="radio" name="q1" value="diver"> Diver, swimmer or untethered object</label>
    <label><input type="radio" name="q1" value="other"> Something else</label>
    <label><input type="radio" name="q1" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q2"><legend>2. Is the vehicle a BlueROV2?</legend>
    <label><input type="radio" name="q2" value="yes"> Yes</label>
    <label><input type="radio" name="q2" value="no"> No</label>
    <label><input type="radio" name="q2" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q3"><legend>3. How could a locator signal reach the topside?</legend>
    <label><input type="radio" name="q3" value="pair"> Spare twisted pair in the tether</label>
    <label><input type="radio" name="q3" value="cable"> A separate cable from locator to topside is fine</label>
    <label><input type="radio" name="q3" value="none"> Neither, I can't add cables</label>
    <label><input type="radio" name="q3" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q4"><legend>4. Does the vehicle have a depth sensor you can send to the topside over the API?</legend>
    <label><input type="radio" name="q4" value="yes"> Yes</label>
    <label><input type="radio" name="q4" value="no"> No</label>
    <label><input type="radio" name="q4" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q5"><legend>5. Where will you operate?</legend>
    <label><input type="radio" name="q5" value="outdoors"> Outdoors, open sky</label>
    <label><input type="radio" name="q5" value="indoors"> Indoors, tank, pool or under a roof</label>
    <label><input type="radio" name="q5" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q6"><legend>6. How far from the receivers will the tracked object get?</legend>
    <label><input type="radio" name="q6" value="100"> Up to 100 m</label>
    <label><input type="radio" name="q6" value="300"> Up to 300 m</label>
    <label><input type="radio" name="q6" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q7"><legend>7. What kind of position do you need?</legend>
    <label><input type="radio" name="q7" value="relative"> Relative to the topside is enough</label>
    <label><input type="radio" name="q7" value="global"> Global coordinates, a few metres is fine</label>
    <label><input type="radio" name="q7" value="precise"> Global, better than about 2–3 m</label>
    <label><input type="radio" name="q7" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q8"><legend>8. What is the topside and baseline mounted on?</legend>
    <label><input type="radio" name="q8" value="fixed"> Fixed spot (jetty, pool side, fixed installation)</label>
    <label><input type="radio" name="q8" value="boat-still"> Small boat, mostly still</label>
    <label><input type="radio" name="q8" value="boat-moving"> Boat that moves during the job</label>
    <label><input type="radio" name="q8" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q9"><legend>9. How long will the locator stay in the water at a time?</legend>
    <label><input type="radio" name="q9" value="short"> Up to about 6 hours</label>
    <label><input type="radio" name="q9" value="long"> Longer than 6 hours</label>
    <label><input type="radio" name="q9" value="unsure"> Not sure</label>
  </fieldset>
  <fieldset class="sel-q" data-q="q10"><legend>10. How many objects?</legend>
    <label><input type="radio" name="q10" value="one"> One</label>
    <label><input type="radio" name="q10" value="several"> Several</label>
    <label><input type="radio" name="q10" value="unsure"> Not sure</label>
  </fieldset>
  <button type="button" id="sel-reset" class="md-button sel-reset">Start over</button>
  <div id="sel-result" class="sel-result" aria-live="polite">
    <p id="sel-summary" class="sel-summary">Answer the questions above. The result updates as you go.</p>
    <div class="sel-block" id="sel-warnings-block"><h3>Check these first</h3><ul id="sel-warnings"></ul></div>
    <div class="sel-block" id="sel-equipment-block"><h3>Equipment</h3><ul id="sel-equipment"></ul></div>
    <div class="sel-block" id="sel-considerations-block"><h3>Things to think about</h3><ul id="sel-considerations"></ul></div>
    <div class="sel-block" id="sel-reasons-block"><h3>Why this result</h3><ul id="sel-reasons"></ul></div>
    <div class="sel-block" id="sel-accuracy-block"><h3>Indicative accuracy (not a specification)</h3><div id="sel-accuracy"></div></div>
  </div>
</div>
<script type="application/json" id="ugps-selector-data">{
  "questions": [
    {
      "id": "q1",
      "short": "what you track"
    },
    {
      "id": "q2",
      "short": "BlueROV2",
      "if": {
        "q1": [
          "rov"
        ]
      }
    },
    {
      "id": "q3",
      "short": "signal path",
      "if": {
        "q1": [
          "rov"
        ]
      }
    },
    {
      "id": "q4",
      "short": "depth sensor",
      "if": {
        "q1": [
          "rov"
        ]
      }
    },
    {
      "id": "q5",
      "short": "environment"
    },
    {
      "id": "q6",
      "short": "range"
    },
    {
      "id": "q7",
      "short": "position type"
    },
    {
      "id": "q8",
      "short": "mounting"
    },
    {
      "id": "q9",
      "short": "time in water"
    },
    {
      "id": "q10",
      "short": "number of objects"
    }
  ],
  "links": {
    "u1": {
      "label": "Locator-U1",
      "href": "../locators/locator-u1/"
    },
    "a1": {
      "label": "Locator-A1",
      "href": "../locators/locator-a1/"
    },
    "d1": {
      "label": "Locator-D1",
      "href": "../locators/locator-d1/"
    },
    "antenna": {
      "label": "Antenna",
      "href": "../antenna/"
    },
    "receivers": {
      "label": "4× Receiver-D1",
      "href": "../receiver-d1/"
    },
    "topside": {
      "label": "UGPS G2 Topside",
      "href": "../ugps-topside/"
    },
    "power": {
      "label": "Power supply",
      "href": "../power-supply/"
    },
    "api": {
      "label": "API",
      "href": "../integration/api/"
    },
    "extgps": {
      "label": "External compass and GNSS",
      "href": "../integration/external-gps/"
    },
    "brov": {
      "label": "BlueROV2 integration overview",
      "href": "../integration/bluerov-integration/"
    },
    "brov-a1": {
      "label": "Locator-A1 BlueROV2 guide",
      "href": "../integration/bluerov-integration-a1/"
    },
    "brov-u1": {
      "label": "Locator-U1 BlueROV2 guide",
      "href": "../integration/bluerov-integration-u1/"
    },
    "sysconfig": {
      "label": "System configuration",
      "href": "../ugps-sysconfig/"
    },
    "support": {
      "label": "contact support",
      "href": "https://support.waterlinked.com/en/knowledge"
    }
  },
  "rules": [
    {
      "id": "R01",
      "when": {
        "q1": [
          "diver",
          "other"
        ]
      },
      "then": {
        "locator": "U1",
        "addons": [
          {
            "text": "USB-C cable (in the kit) and a 5 V/2 A USB charger",
            "link": "u1"
          }
        ],
        "considerations": [
          {
            "text": "Charge the Locator-U1 fully before each use (USB-C, 5 V/2 A).",
            "link": "u1"
          },
          {
            "text": "Wait for GPS lock on the Locator-U1 (solid green LED) before deploying it."
          },
          {
            "text": "The topside needs GNSS lock during the whole mission for time synchronisation."
          },
          {
            "text": "Recover the Locator-U1 within about 6 hours (battery, drying of the pressure sensor, time sync)."
          }
        ],
        "warnings": [
          {
            "id": "u1-gnss",
            "title": "Locator-U1 needs GNSS lock on both ends",
            "text": "GPS lock on the Locator-U1 before deployment (solid green LED) and GNSS lock on the topside during the whole mission. Without both, the topside cannot position the Locator-U1.",
            "link": "u1"
          }
        ],
        "reason": "You track a diver, swimmer or untethered object, so the locator must be wireless"
      }
    },
    {
      "id": "R01b",
      "when": {
        "q1": [
          "other"
        ]
      },
      "then": {
        "considerations": [
          {
            "text": "Mounting the Locator-U1 on your object is your responsibility."
          }
        ],
        "reason": "You track something else"
      }
    },
    {
      "id": "R02",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "yes"
        ],
        "q3": [
          "pair",
          "unsure"
        ]
      },
      "then": {
        "locator": "A1",
        "addons": [
          {
            "text": "BlueROV2 Integration Kit",
            "link": "brov-a1"
          }
        ],
        "considerations": [
          {
            "text": "The integration is a hardware modification of the ROV. Follow the Locator-A1 BlueROV2 integration guide.",
            "link": "brov-a1"
          },
          {
            "text": "Depth comes from the BlueROV2's own depth sensor as set up in the guide."
          },
          {
            "text": "The Locator-A1 signal runs through a spare twisted pair in the tether."
          }
        ],
        "reason": "A BlueROV2 with a spare twisted pair: the Locator-A1 has a kit and a guide"
      }
    },
    {
      "id": "R02b",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "yes"
        ],
        "q3": [
          "pair",
          "unsure"
        ],
        "q4": [
          "no"
        ]
      },
      "then": {
        "considerations": [
          {
            "text": "You said the vehicle has no depth feed. For a BlueROV2 the integration guide provides the depth to the topside.",
            "link": "brov-a1"
          }
        ],
        "reason": "BlueROV2 without a depth feed of its own"
      }
    },
    {
      "id": "R03",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "yes"
        ],
        "q3": [
          "none"
        ]
      },
      "then": {
        "locator": "U1",
        "addons": [
          {
            "text": "BlueROV2 Integration Kit (optional, for the network part only)",
            "link": "brov-u1"
          }
        ],
        "considerations": [
          {
            "text": "No hardware change to the ROV is needed for the locator itself.",
            "link": "brov-u1"
          },
          {
            "text": "A network bridge between the topside and the BlueROV2 lets the GUI show the position. See the Locator-U1 BlueROV2 guide.",
            "link": "brov-u1"
          },
          {
            "text": "Recover the Locator-U1 within about 6 hours (battery, drying of the pressure sensor, time sync)."
          }
        ],
        "warnings": [
          {
            "id": "u1-gnss",
            "title": "Locator-U1 needs GNSS lock on both ends",
            "text": "GPS lock on the Locator-U1 before deployment (solid green LED) and GNSS lock on the topside during the whole mission. Without both, the topside cannot position the Locator-U1.",
            "link": "u1"
          }
        ],
        "reason": "A BlueROV2 where no cables can be added: the wireless Locator-U1"
      }
    },
    {
      "id": "R04",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "yes"
        ],
        "q3": [
          "cable"
        ]
      },
      "then": {
        "locator": "D1",
        "considerations": [
          {
            "text": "The Locator-D1 has its own pressure sensor, so no depth feed is needed.",
            "link": "d1"
          },
          {
            "text": "The Locator-D1 is powered by the topside (about 130 mA) through its integrated 50 m or 100 m cable."
          },
          {
            "text": "Recover the Locator-D1 within about 6 hours and let the pressure sensor dry."
          }
        ],
        "warnings": [
          {
            "id": "d1-kit",
            "title": "Locator-D1 is not compatible with the BlueROV2 Integration Kit",
            "text": "Attach the Locator-D1 to the ROV any convenient way and run its own cable to the topside. For the network bridge, see the BlueROV2 integration overview.",
            "link": "brov"
          }
        ],
        "reason": "A BlueROV2 with a separate locator cable"
      }
    },
    {
      "id": "R05",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "no",
          "unsure"
        ],
        "q3": [
          "pair",
          "unsure"
        ],
        "q4": [
          "yes",
          "unsure"
        ]
      },
      "then": {
        "locator": "A1",
        "addons": [
          {
            "text": "Depth feed from your vehicle through the API (externaldepth.py example)",
            "link": "api"
          }
        ],
        "considerations": [
          {
            "text": "The Locator-A1 is the smallest locator: Ø20 mm × 41 mm, 30 g.",
            "link": "a1"
          },
          {
            "text": "The Locator-A1 sends an analog signal on a 2-wire cable to the topside Locator port. A spare twisted pair in the tether can carry it."
          },
          {
            "text": "The Locator-A1 has no pressure sensor. Your vehicle must send its depth to the topside through the API.",
            "link": "api"
          }
        ],
        "warnings": [
          {
            "id": "routing",
            "title": "Routing the signal to the topside is up to you and at your own risk",
            "text": "There is an integration guide only for the BlueROV2. How to get the locator signal from your vehicle to the topside Locator port is your responsibility.",
            "link": "brov"
          }
        ],
        "reason": "A tethered vehicle with a spare twisted pair and a depth sensor"
      }
    },
    {
      "id": "R05b",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "no",
          "unsure"
        ],
        "q3": [
          "pair",
          "unsure"
        ],
        "q4": [
          "unsure"
        ]
      },
      "then": {
        "warnings": [
          {
            "id": "a1-depth-confirm",
            "title": "Locator-A1 needs an external depth feed: confirm your vehicle can provide one",
            "text": "The Locator-A1 has no pressure sensor. The topside must get the depth from the vehicle through the API. If that is not possible, the Locator-D1 (own depth sensor, own cable) is the cabled alternative.",
            "link": "api"
          }
        ],
        "reason": "You are not sure the vehicle can send its depth"
      }
    },
    {
      "id": "R06",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "no",
          "unsure"
        ],
        "q3": [
          "pair",
          "unsure"
        ],
        "q4": [
          "no"
        ]
      },
      "then": {
        "locator": "D1",
        "considerations": [
          {
            "text": "The Locator-D1 has its own pressure sensor, so no depth feed is needed.",
            "link": "d1"
          },
          {
            "text": "The Locator-D1 is powered by the topside (about 130 mA) through its integrated 50 m or 100 m cable."
          },
          {
            "text": "Recover the Locator-D1 within about 6 hours and let the pressure sensor dry."
          },
          {
            "text": "Outdoors, the wireless Locator-U1 is an alternative: own depth sensor, no cable, but GNSS lock on both ends.",
            "link": "u1"
          }
        ],
        "warnings": [
          {
            "id": "a1-depth-excluded",
            "title": "Locator-A1 excluded: no depth source",
            "text": "The Locator-A1 has no pressure sensor and needs the depth through the API. Your vehicle cannot provide it, so the Locator-D1 with its own depth sensor is suggested.",
            "link": "a1"
          },
          {
            "id": "routing",
            "title": "Routing the signal to the topside is up to you and at your own risk",
            "text": "There is an integration guide only for the BlueROV2. How to get the locator signal from your vehicle to the topside Locator port is your responsibility.",
            "link": "brov"
          }
        ],
        "reason": "A tethered vehicle without a depth feed"
      }
    },
    {
      "id": "R07",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "no",
          "unsure"
        ],
        "q3": [
          "cable"
        ]
      },
      "then": {
        "locator": "D1",
        "addons": [
          {
            "text": "Locator-D1 cable: choose 50 m or 100 m",
            "link": "d1"
          }
        ],
        "considerations": [
          {
            "text": "The Locator-D1 has its own pressure sensor, so no depth feed is needed.",
            "link": "d1"
          },
          {
            "text": "The Locator-D1 is powered by the topside (about 130 mA) through its integrated 50 m or 100 m cable."
          },
          {
            "text": "Recover the Locator-D1 within about 6 hours and let the pressure sensor dry."
          }
        ],
        "warnings": [
          {
            "id": "routing",
            "title": "Routing the signal to the topside is up to you and at your own risk",
            "text": "There is an integration guide only for the BlueROV2. How to get the locator signal from your vehicle to the topside Locator port is your responsibility.",
            "link": "brov"
          }
        ],
        "reason": "A tethered vehicle where a separate locator cable is fine"
      }
    },
    {
      "id": "R08",
      "when": {
        "q1": [
          "rov"
        ],
        "q2": [
          "no",
          "unsure"
        ],
        "q3": [
          "none"
        ]
      },
      "then": {
        "locator": "U1",
        "addons": [
          {
            "text": "Mounting bracket (in the kit)",
            "link": "u1"
          }
        ],
        "considerations": [
          {
            "text": "Charge the Locator-U1 fully before each use (USB-C, 5 V/2 A).",
            "link": "u1"
          },
          {
            "text": "Wait for GPS lock on the Locator-U1 (solid green LED) before deploying it."
          },
          {
            "text": "The topside needs GNSS lock during the whole mission for time synchronisation."
          },
          {
            "text": "Recover the Locator-U1 within about 6 hours (battery, drying of the pressure sensor, time sync)."
          }
        ],
        "warnings": [
          {
            "id": "u1-gnss",
            "title": "Locator-U1 needs GNSS lock on both ends",
            "text": "GPS lock on the Locator-U1 before deployment (solid green LED) and GNSS lock on the topside during the whole mission. Without both, the topside cannot position the Locator-U1.",
            "link": "u1"
          }
        ],
        "reason": "A tethered vehicle where no cables can be added: the wireless Locator-U1"
      }
    },
    {
      "id": "R09",
      "when": {
        "q1": [
          "unsure"
        ]
      },
      "then": {
        "locator": "U1",
        "baseline": "Antenna",
        "edition": "R100",
        "warnings": [
          {
            "id": "default",
            "title": "Safe default, not a fit",
            "text": "This is the UGPS G2 Standard Kit (R100 topside, Locator-U1, Antenna). Tell us what you want to track, or contact support for advice.",
            "link": "support"
          },
          {
            "id": "u1-gnss",
            "title": "Locator-U1 needs GNSS lock on both ends",
            "text": "GPS lock on the Locator-U1 before deployment (solid green LED) and GNSS lock on the topside during the whole mission. Without both, the topside cannot position the Locator-U1.",
            "link": "u1"
          }
        ],
        "reason": "You did not say what you want to track, so this is the Standard Kit"
      }
    },
    {
      "id": "R10",
      "when": {
        "q5": [
          "indoors"
        ],
        "locator": [
          "U1"
        ]
      },
      "then": {
        "override": true,
        "withhold": true,
        "warnings": [
          {
            "id": "u1-indoors",
            "title": "Locator-U1 needs GNSS time sync on both ends; indoors there is none",
            "text": "Options: a cabled Locator-A1 or Locator-D1 if a cable is acceptable, or a GPS repeater. Contact support to discuss your case.",
            "link": "support"
          }
        ],
        "reason": "Indoors, in a tank or under a roof there is no GNSS for the wireless locator"
      }
    },
    {
      "id": "R11",
      "when": {
        "q5": [
          "indoors"
        ],
        "locator": [
          "A1",
          "D1"
        ]
      },
      "then": {
        "baseline": "Antenna",
        "edition": "R100",
        "considerations": [
          {
            "text": "Set the topside to Static mode and enter the heading. Positions are relative to the topside, or global if you enter the topside coordinates.",
            "link": "sysconfig"
          },
          {
            "text": "The Antenna is the baseline for tanks and pools.",
            "link": "antenna"
          }
        ],
        "warnings": [
          {
            "id": "no-gnss",
            "title": "No GNSS indoors: on-board global position is unavailable",
            "text": "The topside's internal GNSS has no signal indoors, in a tank or under a roof. Use Static mode (relative position, or global if you enter the topside coordinates) or a GPS repeater.",
            "link": "sysconfig"
          }
        ],
        "reason": "Indoors, in a tank or under a roof with a cabled locator"
      }
    },
    {
      "id": "R12",
      "when": {
        "q6": [
          "300"
        ],
        "locator": [
          "D1"
        ]
      },
      "then": {
        "edition": "R100",
        "warnings": [
          {
            "id": "d1-r300",
            "title": "R300 brings nothing with a Locator-D1",
            "text": "The Locator-D1 cable is max 100 m, so it cannot reach 300 m. Choose R100 and buy the 300 m upgrade later if you change locator.",
            "link": "d1"
          }
        ],
        "reason": "300 m range with a cabled Locator-D1"
      }
    },
    {
      "id": "R13",
      "when": {
        "q6": [
          "300"
        ],
        "locator": [
          "U1",
          "A1",
          "D1"
        ]
      },
      "then": {
        "edition": "R300",
        "reason": "Up to 300 m range"
      }
    },
    {
      "id": "R14",
      "when": {
        "q6": [
          "100"
        ],
        "locator": [
          "U1",
          "A1",
          "D1"
        ]
      },
      "then": {
        "edition": "R100",
        "reason": "Up to 100 m range"
      }
    },
    {
      "id": "R15",
      "when": {
        "q6": [
          "unsure"
        ],
        "locator": [
          "U1",
          "A1"
        ]
      },
      "then": {
        "edition": "R100",
        "considerations": [
          {
            "text": "A 300 m upgrade can be purchased later."
          }
        ],
        "reason": "Range not known, so the R100 edition"
      }
    },
    {
      "id": "R15b",
      "when": {
        "q6": [
          "unsure"
        ],
        "locator": [
          "D1"
        ]
      },
      "then": {
        "edition": "R100",
        "considerations": [
          {
            "text": "With a Locator-D1 the range stays 100 m (cable), so a 300 m upgrade only helps if you change locator."
          }
        ],
        "reason": "Range not known with a cabled Locator-D1"
      }
    },
    {
      "id": "R16",
      "when": {
        "q7": [
          "relative"
        ]
      },
      "then": {
        "considerations": [
          {
            "text": "For relative position the topside does not need GNSS with a Locator-A1 or Locator-D1."
          }
        ],
        "reason": "Relative position is enough"
      }
    },
    {
      "id": "R16b",
      "when": {
        "q7": [
          "relative"
        ],
        "locator": [
          "U1"
        ]
      },
      "then": {
        "considerations": [
          {
            "text": "The Locator-U1 still needs GNSS lock on both ends for timing, even for relative position.",
            "link": "u1"
          }
        ],
        "reason": "Relative position with a Locator-U1"
      }
    },
    {
      "id": "R17",
      "when": {
        "q7": [
          "global"
        ]
      },
      "then": {
        "considerations": [
          {
            "text": "Global position comes from the topside's internal GNSS (outdoors) or from the coordinates you enter in Static mode. Set the heading.",
            "link": "sysconfig"
          }
        ],
        "warnings": [
          {
            "id": "heading-drift",
            "title": "Heading drifts: re-set it regularly or use external heading",
            "text": "The topside's heading drifts over time. Re-set it from a reliable compass, use Static mode, or feed heading through the API.",
            "link": "extgps"
          }
        ],
        "reason": "Global coordinates, a few metres is fine"
      }
    },
    {
      "id": "R18",
      "when": {
        "q7": [
          "precise"
        ]
      },
      "then": {
        "addons": [
          {
            "text": "External RTK GNSS through the API (nmeainput.py or ugps-nmea-go)",
            "link": "extgps"
          }
        ],
        "considerations": [
          {
            "text": "The internal GNSS is about 2.5 m CEP (2.0 m with SBAS). For better than about 2–3 m, feed an RTK GNSS position through the API.",
            "link": "extgps"
          }
        ],
        "warnings": [
          {
            "id": "offsets",
            "title": "Enter antenna/receiver offsets relative to the external GNSS antenna, not the topside housing",
            "text": "When position comes from an external GNSS through the API, the offsets in the GUI must be measured from that external GNSS antenna.",
            "link": "extgps"
          }
        ],
        "reason": "Global, better than about 2–3 m"
      }
    },
    {
      "id": "R18b",
      "when": {
        "q7": [
          "precise"
        ],
        "locator": [
          "U1"
        ]
      },
      "then": {
        "warnings": [
          {
            "id": "u1-gnss",
            "title": "Locator-U1 needs GNSS lock on both ends",
            "text": "GPS lock on the Locator-U1 before deployment (solid green LED) and GNSS lock on the topside during the whole mission. Without both, the topside cannot position the Locator-U1.",
            "link": "u1"
          }
        ],
        "reason": "External position with a Locator-U1 still needs the topside's own GNSS lock for timing"
      }
    },
    {
      "id": "R18c",
      "when": {
        "q7": [
          "precise"
        ],
        "q5": [
          "indoors"
        ]
      },
      "then": {
        "warnings": [
          {
            "id": "no-gnss",
            "title": "No GNSS indoors: on-board global position is unavailable",
            "text": "The topside's internal GNSS has no signal indoors, in a tank or under a roof. Use Static mode (relative position, or global if you enter the topside coordinates) or a GPS repeater.",
            "link": "sysconfig"
          }
        ],
        "reason": "Precise global position indoors"
      }
    },
    {
      "id": "R19",
      "when": {
        "q8": [
          "fixed"
        ],
        "q5": [
          "outdoors",
          "unsure"
        ],
        "locator": [
          "U1",
          "A1",
          "D1"
        ]
      },
      "then": {
        "baseline": "4× Receiver-D1",
        "considerations": [
          {
            "text": "Static mode: position and heading entered once gives the best accuracy.",
            "link": "sysconfig"
          },
          {
            "text": "The Antenna works too, for quick deployment or in a pool or tank.",
            "link": "antenna"
          }
        ],
        "reason": "A fixed installation outdoors"
      }
    },
    {
      "id": "R20",
      "when": {
        "q8": [
          "boat-still"
        ],
        "locator": [
          "U1",
          "A1",
          "D1"
        ]
      },
      "then": {
        "baseline": "Antenna",
        "considerations": [
          {
            "text": "On-board mode: set the heading from a compass and re-set it regularly, the topside heading drifts.",
            "link": "sysconfig"
          }
        ],
        "reason": "A small boat, mostly still"
      }
    },
    {
      "id": "R21",
      "when": {
        "q8": [
          "boat-moving"
        ],
        "locator": [
          "U1",
          "A1",
          "D1"
        ]
      },
      "then": {
        "baseline": "Antenna",
        "addons": [
          {
            "text": "External compass and GNSS through the API",
            "link": "extgps"
          }
        ],
        "considerations": [
          {
            "text": "On a larger vessel, 4× Receiver-D1 can replace the Antenna.",
            "link": "receivers"
          },
          {
            "text": "With external position, enter the antenna/receiver offsets relative to the external GNSS antenna, not the topside housing."
          }
        ],
        "warnings": [
          {
            "id": "ext-heading",
            "title": "Always use external heading on a moving boat",
            "text": "The topside's heading drifts and the boat turns. Feed heading and position from the boat's GNSS compass through the API.",
            "link": "extgps"
          }
        ],
        "reason": "A boat that moves during the job"
      }
    },
    {
      "id": "R22",
      "when": {
        "q8": [
          "unsure"
        ],
        "locator": [
          "U1",
          "A1",
          "D1"
        ]
      },
      "then": {
        "baseline": "Antenna",
        "considerations": [
          {
            "text": "The Antenna is the quick-deploy baseline.",
            "link": "antenna"
          }
        ],
        "reason": "Mounting not known, so the Antenna"
      }
    },
    {
      "id": "R23",
      "when": {
        "q9": [
          "long"
        ],
        "locator": [
          "U1",
          "D1"
        ]
      },
      "then": {
        "warnings": [
          {
            "id": "six-hours",
            "title": "Plan recoveries every ~6 h",
            "text": "The Locator-U1 and Locator-D1 need surfacing after about 6 hours (battery, drying the pressure sensor, time sync). The Locator-A1 has no stated limit."
          }
        ],
        "reason": "Longer than 6 hours in the water with a Locator-U1 or Locator-D1"
      }
    },
    {
      "id": "R24",
      "when": {
        "q9": [
          "long"
        ],
        "locator": [
          "A1"
        ]
      },
      "then": {
        "considerations": [
          {
            "text": "The Locator-A1 has no stated submersion limit.",
            "link": "a1"
          }
        ],
        "reason": "Longer than 6 hours in the water with a Locator-A1"
      }
    },
    {
      "id": "R25",
      "when": {
        "q10": [
          "several"
        ]
      },
      "then": {
        "addons": [
          {
            "text": "One locator per object, each on a different channel (7 channels)",
            "link": "sysconfig"
          }
        ],
        "considerations": [
          {
            "text": "Only one locator is tracked at a time. Switch between them in the GUI."
          }
        ],
        "reason": "Several objects"
      }
    },
    {
      "id": "R26",
      "when": {
        "locator": [
          "none"
        ]
      },
      "then": {
        "withhold": true,
        "warnings": [
          {
            "id": "no-result",
            "title": "No recommendation from these answers",
            "text": "Contact support and we will help you choose.",
            "link": "support"
          }
        ],
        "reason": "The answers do not give a locator"
      }
    }
  ],
  "equipmentBase": [
    {
      "text": "UGPS G2 Topside",
      "link": "topside"
    },
    {
      "text": "Power supply",
      "link": "power"
    }
  ],
  "accuracy": {
    "R100": {
      "base": "Datasheet: horizontal range < 0.2 %, horizontal angle < 1°, depth < 1 %. At R = 100 m: range term 0.2 m, cross-range term 1.75 m, so about 1.8 m relative error (root sum of squares; 2.0 m if simply added).",
      "relative": "Relative position only: the figure above is what applies.",
      "global": "Global position with the internal GNSS adds 2.5 m CEP (2.0 m with SBAS), so about 3.1 m, assuming a good heading. A 1° heading error adds about 1.75 m, and the heading drifts.",
      "precise": "With an RTK GNSS fed through the API the GNSS term becomes negligible and the global error approaches the relative figure, about 1.8 m.",
      "unsure": "If you need global position, the internal GNSS adds 2.5 m CEP (2.0 m with SBAS), so about 3.1 m, assuming a good heading. A 1° heading error adds about 1.75 m, and the heading drifts."
    },
    "R300": {
      "base": "Datasheet: horizontal range < 0.2 %, horizontal angle < 1°, depth < 1 %. At R = 300 m: range term 0.6 m, cross-range term 5.2 m, so about 5.3 m relative error (root sum of squares; 5.8 m if simply added).",
      "relative": "Relative position only: the figure above is what applies.",
      "global": "Global position with the internal GNSS adds 2.5 m CEP (2.0 m with SBAS), so about 5.9 m, assuming a good heading. A 1° heading error adds about 5.2 m, and the heading drifts.",
      "precise": "With an RTK GNSS fed through the API the GNSS term becomes negligible and the global error approaches the relative figure, about 5.3 m.",
      "unsure": "If you need global position, the internal GNSS adds 2.5 m CEP (2.0 m with SBAS), so about 5.9 m, assuming a good heading. A 1° heading error adds about 5.2 m, and the heading drifts."
    },
    "static": "With Static mode the global error is the relative figure plus how accurately you entered the topside coordinates.",
    "depth": "Depth: < 1 % of depth (1 m at 100 m depth). All figures are indicative worst cases at the limit of range, not specifications."
  }
}</script>

## Indicative accuracy (not a specification)

The [datasheet](https://waterlinked.com/datasheets/ugps-g2-standard) states the acoustic accuracy as horizontal range < 0.2 %, horizontal angle < 1° and depth < 1 %. These are relative figures in the acoustic frame. The worst case is at the limit of range, R. The range term is 0.2 % × R and the cross-range term is R × tan 1° (about 1.75 % × R). We combine them as the root sum of squares and also show the plain sum as a pessimistic bound.

| | R = 100 m | R = 300 m |
|---|---|---|
| Range term (0.2 % × R) | 0.2 m | 0.6 m |
| Cross-range term (R × tan 1°) | 1.75 m | 5.2 m |
| **Relative error** (root sum of squares) | **about 1.8 m** | **about 5.3 m** |
| Relative error (plain sum) | about 2.0 m | about 5.8 m |
| Global error with the internal GNSS (2.5 m CEP), good heading | about 3.1 m | about 5.9 m |
| Extra error per 1° of heading error | about 1.75 m | about 5.2 m |

* The internal GNSS (u-blox NEO-M8T) is 2.5 m CEP autonomous, 2.0 m with SBAS. The heading from the IMU drifts, so Static mode or external heading matters.
* With an RTK GNSS fed through the API the GNSS term becomes negligible and the global error approaches the relative figure.
* With Static mode the global error is the relative figure plus how accurately you entered the topside coordinates.
* Depth: < 1 % of depth (1 m at 100 m depth).

All of these are indicative, not specifications.
