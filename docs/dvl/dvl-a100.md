# DVL A100

The DVL A100 is a compact, high-accuracy Doppler Velocity Log for lightweight and integration-friendly platforms.

It is designed for close-range and mid-range operation up to 100 m altitude, with Ethernet and RS232 serial interfaces for vehicle and topside integrations.

The DVL A100 is part of the same product family as the DVL A250. From a web GUI, configuration, protocol, and integration perspective, the two products are documented together where the behavior is shared. The main differences are operating range, frequency, speed limits, size, weight, depth rating, and physical configuration.

## Key features

* Altitude range from 5 cm to 100 m.
* 4-beam convex Janus transducer array.
* 625 kHz transducer frequency.
* Integrated AHRS for dead reckoning.
* Ethernet and RS232 serial communication.
* TCP JSON API, serial protocol, PD4, and PD6. PD0 is planned but not available yet.
* Side cable entry and rear O-ring interface versions.

## Mechanical and installation overview

Use the mechanical information together with the common [Installation](installation.md) guidance. Before final drawings are added, verify dimensions, mounting hole placement, cable routing, and line of sight against the latest product drawing or datasheet.

### Dimensions

* **Diameter**: 90 mm
* **Height**: 34 mm
* **Weight in air**: 0.2 kg
* **Weight in water**: 0.125 kg
* **Depth rating**: 1,000 m or 4,000 m for side-entry cable configuration; rear O-ring interface version rated to 1,000 m
* **Material**: PEEK (housing), Stainless Steel 316 (back plate)

!!! note "No dead reckoning on the 4,000 m version"
    The 4,000 m version of the DVL A100 does not output orientation (roll, pitch, and yaw) or dead reckoning. Velocity is measured and reported as normal. The dead reckoning report is not sent over the TCP JSON API or the serial protocol. See [DVL versions without dead reckoning](dead-reckoning.md#dvl-versions-without-dead-reckoning).

### Physical interface versions

The DVL A100 is available in these physical interface versions:

* Side cable entry version with 3 m shielded cable.
* Rear O-ring interface version with 1 m shielded cable.

### Cable dimensions

Cable diameter: 7.8 mm +/- 0.2 mm

The cable diameter is the same for the side-entry, rear O-ring interface and connector versions.

## Mounting holes

Use a rigid mount so the DVL moves with the vehicle or boat. Avoid flexible poles, unsupported brackets, and mounts that can vibrate.

For the mounting holes of both versions, the vehicle mounting interface of the rear O-ring interface version, and standard and precision mounting, see [Mounting interface](mounting-interface.md). Download the [mounting interface drawing (PDF)](https://www.waterlinked.com/web/content/139397?unique=5597169e8d073e75ffc3fbf9d39e7c823f68e866&download=true&access_token=c4317bae-e62f-4f78-8ba2-188e1fab7972). It is also available under *Downloads & Resources* on the [DVL A100 product page](https://www.waterlinked.com/shop/dvl-a100-1377).

## Transducer numbering

Transducer numbering is useful when comparing web GUI or protocol diagnostics with the physical installation.

Mechanical drawings number the transducers from 1 to 4. Protocol messages and diagnostic logs use zero-based transducer `id` values from 0 to 3. See [Transducer numbering and protocol IDs](axes.md#transducer-numbering-and-protocol-ids).

## Transducer beam geometry

Keep all beam paths unobstructed. Avoid mounting locations where brackets, frames, skids, cables, thrusters, propellers, or hull structures can intersect the beam paths.

The DVL A100 beam angle is 22.5 degrees.

## Line of sight

Keep a 65° cone below the transducers free of obstructions. The cone starts at the outer edge of the housing face, and the drawing is to scale.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 420" fill="currentColor" font-size="12" style="max-width: 680px;" role="img" aria-label="DVL A100 line of sight, side view: keep a 65 degree cone below the transducers free">
  <defs><marker id="los-dvla100-a" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z"/></marker><marker id="los-dvla100-b" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto"><path d="M6,0 L0,3 L6,6 Z"/></marker></defs>
  <text x="20" y="24" font-size="14" font-weight="bold">DVL A100 line of sight (side view)</text>
  <text x="20" y="42" font-size="11" opacity="0.75">Mounting side up, transducers facing the seabed. Drawn to scale against the other DVL models.</text>
  <polygon points="268.0,126.0 412.0,126.0 573.8,380.0 106.2,380.0" fill="currentColor" fill-opacity="0.07" stroke="none"/>
  <line x1="268.0" y1="126.0" x2="106.2" y2="380.0" stroke="currentColor" stroke-width="1.4"/>
  <line x1="412.0" y1="126.0" x2="573.8" y2="380.0" stroke="currentColor" stroke-width="1.4"/>
  <path d="M194.7,241.1 A270.5,270.5 0 0 0 485.3,241.1" fill="none" stroke="currentColor" stroke-width="0.8" marker-start="url(#los-dvla100-a)" marker-end="url(#los-dvla100-b)"/>
  <text x="340" y="301.5" text-anchor="middle" font-size="13" font-weight="bold">65°</text>
  <text x="340" y="402.0" text-anchor="middle" font-size="11">Keep this 65° cone free of brackets, frames, cables, thrusters and hull</text>
  <g stroke="currentColor" stroke-width="0.9" stroke-dasharray="5 4" opacity="0.8">
    <line x1="392.2" y1="134.2" x2="467.5" y2="315.9"/>
    <line x1="287.8" y1="134.2" x2="212.5" y2="315.9"/>
    <line x1="392.2" y1="134.2" x2="392.2" y2="194.2" stroke-dasharray="2 3"/>
  </g>
  <path d="M392.2,180.2 A46,46 0 0 0 409.8,176.7" fill="none" stroke="currentColor" stroke-width="0.8"/>
  <text x="416.2" y="198.2" font-size="11">22.5°</text>
  <text x="477.5" y="317.9" font-size="11" opacity="0.85">Beam axis</text>
  <path d="M268.0,88.0 L412.0,88.0 L412.0,126.0 L372.4,142.4 L307.6,142.4 L268.0,126.0 Z" fill="currentColor" fill-opacity="0.18" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
  <g stroke="currentColor" stroke-width="3.2" stroke-linecap="round">
    <line x1="407.2" y1="128.0" x2="377.2" y2="140.4"/>
    <line x1="272.8" y1="128.0" x2="302.8" y2="140.4"/>
  </g>
  <line x1="268.0" y1="76.0" x2="412.0" y2="76.0" stroke="currentColor" stroke-width="0.7" marker-start="url(#los-dvla100-b)" marker-end="url(#los-dvla100-a)"/>
  <text x="340" y="71.0" text-anchor="middle" font-size="11">Ø90 mm</text>
  <line x1="426.0" y1="88.0" x2="426.0" y2="142.4" stroke="currentColor" stroke-width="0.7" marker-start="url(#los-dvla100-b)" marker-end="url(#los-dvla100-a)"/>
  <text x="432.0" y="119.2" font-size="11">34 mm</text>
  <text x="258.0" y="100.0" text-anchor="end" font-size="11" opacity="0.85">Mounting side</text>
  <text x="245.6" y="146.4" text-anchor="end" font-size="11" opacity="0.85">Transducers</text>
</svg>

The DVL needs a clear acoustic path to the seabed or another reflecting surface. Strong turbulence, bubbles, vibration, and operation very close to the surface can reduce signal quality or cause loss of bottom lock.

For boat-mounted installations, consider the flow around the hull and avoid positions where bubbles or aerated water pass across the transducers. For ROV/AUV installations, avoid mounting directly in thruster wash or near moving parts.

## Datasheet

[Datasheet](https://www.waterlinked.com/web/content/108663?unique=39e82f816d08f4d2270df5a9e9f8b6822e9790fe&download=true)
