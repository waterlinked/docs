# DVL A250

The [DVL A250](https://www.waterlinked.com/shop/dvl-a250-1372) is the most capable DVL in the lineup, delivering long-range performance while maintaining a compact and efficient design.

Operating at lower frequency for extended reach, the A250 enables reliable velocity measurements at distances up to 250 m, making it suitable for demanding subsea operations.

The DVL A250 combines high performance, a compact 4-beam setup, open interface protocol, and a competitive cost, making it a powerful solution for larger vehicles and deep-water applications.

## Dimensions and FOV

Use the mechanical information together with the common [Installation](installation.md) guidance. Verify dimensions, mounting hole placement, cable routing, and line of sight against the latest product drawing or datasheet.

### Dimensions

* **Diameter**: 149 mm
* **Height**: 40 mm
* **Weight in air**: 1.65 kg
* **Weight in water**: 0.75 kg
* **Depth rating**: 4,000 m for side-entry cable configuration; rear O-ring interface version rated to 1,000 m
* **Material**: PEEK (housing), Stainless Steel 316 (back plate)

Use the drawings below as mechanical reference for the two A250 interface variants.

### Rear O-ring interface version

![DVL A250 rear O-ring interface mechanical drawing](../img/dvl_a250_back_entry_drawing.png)

### Side cable entry version

![DVL A250 side cable entry mechanical drawing](../img/dvl_a250_front_side_drawing.png)

### Cable dimensions

Cable diameter: 7.8 mm +/- 0.2 mm

The cable diameter is the same for the side-entry, rear O-ring interface and connector versions.

The DVL A250 is available with side-entry cable and rear O-ring interface options. A Seacon connector option is available for side-entry versions only.

## Mounting holes

Use a rigid mount so the DVL moves with the vehicle or boat. Avoid flexible poles, unsupported brackets, and mounts that can vibrate.

Use the mechanical drawings above as the reference for mounting-hole placement.

For the vehicle mounting interface of the rear O-ring interface version, and for standard and precision mounting, see [Mounting interface](mounting-interface.md). Download the [mounting interface drawing (PDF)](https://www.waterlinked.com/web/content/139407?unique=665890810fa69948df7214dd54462d724ea2cfa3&download=true&access_token=09b5afbd-8fe6-4ded-b0f7-fc3bb5f165c2). It is also available under *Downloads & Resources* on the [DVL A250 product page](https://www.waterlinked.com/shop/dvl-a250-1372).

## Transducer numbering

Transducer numbering is useful when comparing web GUI or protocol diagnostics with the physical installation.

Mechanical drawings number the transducers from 1 to 4. Protocol messages and diagnostic logs use zero-based transducer `id` values from 0 to 3. See [Transducer numbering and protocol IDs](axes.md#transducer-numbering-and-protocol-ids).

## Transducer beam geometry

Keep all beam paths unobstructed. Avoid mounting locations where brackets, frames, skids, cables, thrusters, propellers, or hull structures can intersect the beam paths.

The beam angle is 22.5° from vertical.

## Line of sight

Keep a 65° cone below the transducers free of obstructions. The cone starts at the outer edge of the housing face, and the drawing is to scale.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 420" fill="currentColor" font-size="12" style="max-width: 680px;" role="img" aria-label="DVL A250 line of sight, side view: keep a 65 degree cone below the transducers free">
  <defs><marker id="los-dvla250-a" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto"><path d="M0,0 L6,3 L0,6 Z"/></marker><marker id="los-dvla250-b" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto"><path d="M6,0 L0,3 L6,6 Z"/></marker></defs>
  <text x="20" y="24" font-size="14" font-weight="bold">DVL A250 line of sight (side view)</text>
  <text x="20" y="42" font-size="11" opacity="0.75">Mounting side up, transducers facing the seabed. Drawn to scale against the other DVL models.</text>
  <polygon points="220.8,124.8 459.2,124.8 621.8,380.0 58.2,380.0" fill="currentColor" fill-opacity="0.07" stroke="none"/>
  <line x1="220.8" y1="124.8" x2="58.2" y2="380.0" stroke="currentColor" stroke-width="1.4"/>
  <line x1="459.2" y1="124.8" x2="621.8" y2="380.0" stroke="currentColor" stroke-width="1.4"/>
  <path d="M154.5,229.0 A345.3,345.3 0 0 0 525.5,229.0" fill="none" stroke="currentColor" stroke-width="0.8" marker-start="url(#los-dvla250-a)" marker-end="url(#los-dvla250-b)"/>
  <text x="340" y="301.0" text-anchor="middle" font-size="13" font-weight="bold">65°</text>
  <text x="340" y="402.0" text-anchor="middle" font-size="11">Keep this 65° cone free of brackets, frames, cables, thrusters and hull</text>
  <g stroke="currentColor" stroke-width="0.9" stroke-dasharray="5 4" opacity="0.8">
    <line x1="426.4" y1="138.4" x2="500.4" y2="317.0"/>
    <line x1="253.6" y1="138.4" x2="179.6" y2="317.0"/>
    <line x1="426.4" y1="138.4" x2="426.4" y2="198.4" stroke-dasharray="2 3"/>
  </g>
  <path d="M426.4,184.4 A46,46 0 0 0 444.0,180.9" fill="none" stroke="currentColor" stroke-width="0.8"/>
  <text x="450.4" y="202.4" font-size="11">22.5°</text>
  <text x="510.4" y="319.0" font-size="11" opacity="0.85">Beam axis</text>
  <path d="M220.8,88.0 L459.2,88.0 L459.2,124.8 L393.6,152.0 L286.4,152.0 L220.8,124.8 Z" fill="currentColor" fill-opacity="0.18" stroke="currentColor" stroke-width="1.6" stroke-linejoin="round"/>
  <g stroke="currentColor" stroke-width="3.2" stroke-linecap="round">
    <line x1="451.3" y1="128.1" x2="401.5" y2="148.7"/>
    <line x1="228.7" y1="128.1" x2="278.5" y2="148.7"/>
  </g>
  <line x1="220.8" y1="76.0" x2="459.2" y2="76.0" stroke="currentColor" stroke-width="0.7" marker-start="url(#los-dvla250-b)" marker-end="url(#los-dvla250-a)"/>
  <text x="340" y="71.0" text-anchor="middle" font-size="11">Ø149 mm</text>
  <line x1="473.2" y1="88.0" x2="473.2" y2="152.0" stroke="currentColor" stroke-width="0.7" marker-start="url(#los-dvla250-b)" marker-end="url(#los-dvla250-a)"/>
  <text x="479.2" y="124.0" font-size="11">40 mm</text>
  <text x="210.8" y="100.0" text-anchor="end" font-size="11" opacity="0.85">Mounting side</text>
  <text x="191.5" y="156.0" text-anchor="end" font-size="11" opacity="0.85">Transducers</text>
</svg>

The DVL needs a clear acoustic path to the seabed or another reflecting surface. Strong turbulence, bubbles, vibration, and operation very close to the surface can reduce signal quality or cause loss of bottom lock.

For boat-mounted installations, consider the flow around the hull and avoid positions where bubbles or aerated water pass across the transducers. For ROV/AUV installations, avoid mounting directly in thruster wash or near moving parts.

## Datasheet

[Datasheet](https://www.waterlinked.com/web/content/108461?unique=7dbba77aaa00fa0f5a38e5d998abe18965f4ddbe&download=true)
