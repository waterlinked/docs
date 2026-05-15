# DVL A100

The DVL A100 is a compact, high-accuracy Doppler Velocity Log for lightweight and integration-friendly platforms.

It is designed for close-range and mid-range operation up to 100 m altitude, with Ethernet and RS232 serial interfaces for vehicle and topside integrations.

The DVL A100 is part of the same product family as the DVL A250. From a web GUI, configuration, protocol, and integration perspective, the two products are documented together where the behavior is shared. The main differences are operating range, frequency, speed limits, size, weight, depth rating, and physical configuration.

<!-- TODO: Add product image of DVL A100. -->

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
* **Depth rating**: 1,000 m
* **Material**: PEEK (housing), Stainless Steel 316 (back plate)

<!-- TODO: Add DVL A100 dimensions drawing. -->

### Physical interface versions

The DVL A100 is available in these physical interface versions:

* Side cable entry version with 3 m shielded cable.
* Rear O-ring interface version with 1 m shielded cable.

<!-- TODO: Add DVL A100 cable dimensions drawing, including side cable entry and rear O-ring interface variants. -->

## Mounting holes

Use a rigid mount so the DVL moves with the vehicle or boat. Avoid flexible poles, unsupported brackets, and mounts that can vibrate.

<!-- TODO: Add DVL A100 mounting holes drawing. -->

## Transducer numbering

Transducer numbering is useful when comparing web GUI or protocol diagnostics with the physical installation.

Mechanical drawings number the transducers from 1 to 4. Protocol messages and diagnostic logs use zero-based transducer `id` values from 0 to 3. See [Transducer numbering and protocol IDs](axes.md#transducer-numbering-and-protocol-ids).

<!-- TODO: Add DVL A100 transducer numbering drawing. -->

## Transducer beam geometry

Keep all beam paths unobstructed. Avoid mounting locations where brackets, frames, skids, cables, thrusters, propellers, or hull structures can intersect the beam paths.

The DVL A100 beam angle is 22.5 degrees.

<!-- TODO: Add DVL A100 transducer beam geometry drawing. -->

## Line of sight

The DVL needs a clear acoustic path to the seabed or another reflecting surface. Strong turbulence, bubbles, vibration, and operation very close to the surface can reduce signal quality or cause loss of bottom lock.

For boat-mounted installations, consider the flow around the hull and avoid positions where bubbles or aerated water pass across the transducers. For ROV/AUV installations, avoid mounting directly in thruster wash or near moving parts.

<!-- TODO: Add DVL A100 line-of-sight drawing. -->
## Datasheet

[Datasheet](https://www.waterlinked.com/web/content/108663?unique=39e82f816d08f4d2270df5a9e9f8b6822e9790fe&download=true)
