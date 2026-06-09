# Installation

This page gives common installation guidance for all our DVLs. Use it together with the mechanical and electrical page for your specific model.

!!! tip "First-time setup"
    For the full end-to-end path (mount, wire, connect, open the web GUI), follow the [Quickstart](quickstart.md). This page covers mounting and placement; see also [Electrical](electrical.md) and [Network setup](networking.md).

## Before installation

1. Check that the DVL, cable, connector, and mounting hardware are undamaged.
2. Review the model-specific dimensions, mounting holes, and line-of-sight drawings.
3. Plan cable routing so the cable is protected from strain, sharp bends, and moving parts.
4. Confirm the electrical interface for your model:
    * [DVL electrical connection](electrical.md)
    * [DVL A50/A125 serial interface](electrical.md#dvl-a50-and-dvl-a125-serial-interface)
    * [DVL A100/A250 serial interface](electrical.md#dvl-a100-and-dvl-a250-serial-interface)

## Clear line of sight

The DVL needs a clear acoustic path from each transducer to the seabed or other reflecting surface.

When mounting the DVL:

* Keep all beam paths free from brackets, vehicle frames, payloads, hulls, skids, and cables.
* Make sure the DVL is not looking into a wall, tank side, or nearby structure during testing.
* Check the web GUI or protocol output to see whether the transducers report similar and reasonable distances in a flat test area.

See the model pages for line-of-sight drawings:

* [DVL A50 line of sight](dvl-a50.md#line-of-sight)
* [DVL A100 line of sight](dvl-a100.md#line-of-sight)
* [DVL A125 line of sight](dvl-a125.md#line-of-sight)
* [DVL A250 line of sight](dvl-a250.md#line-of-sight)

<!-- TODO: Add final DVL A100 line-of-sight asset when available. -->
<!-- TODO: Add final DVL A250 line-of-sight asset when available. -->

## Mounting orientation

Velocity and dead reckoning output use the configured vehicle frame. If the DVL is not mounted with its forward direction aligned with the vehicle forward direction, configure the mounting rotation offset.

See [Axes](axes.md) for the common DVL axis convention and mounting rotation offset.

!!! warning
    Incorrect mounting rotation can make valid DVL data appear to point in the wrong direction.

## Rigid mounting and vibration

Use a rigid mount so the DVL moves with the vehicle or boat. Avoid flexible poles, long unsupported brackets, loose fasteners, or mounts that can vibrate.

Mechanical vibration can make the velocity estimate noisy or unstable. If measurements look noisy:

1. Check that the DVL cannot move relative to the vehicle.
2. Check for loose fasteners or flexing brackets.
3. Compare measurements with thrusters or motors off and on.

## Thrusters, propellers, hulls, and bubbles

Air bubbles and turbulent flow can reduce signal quality and cause invalid velocity or loss of bottom lock.

When possible:

* Mount the DVL away from strong turbulence from thrusters, propellers, pumps, and hull edges.
* Avoid positions where bubbles pass across the transducers.
* Avoid mounting directly behind a propeller or thruster wash.
* Consider the vehicle direction of travel and where bubbles will move during operation.

No strict minimum distance is specified here because it depends on the vehicle, speed, water flow, and installation.

## Boat-mounted use

For boat-mounted installations, consider flow and bubbles around the hull:

* Avoid mounting where the hull creates strong aerated flow.
* Avoid locations that come out of the water in waves or when the boat pitches and rolls.
* Use a rigid pole or bracket that does not vibrate.
* Keep the DVL submerged and stable during measurements.
* Check bottom lock at the expected boat speed before relying on the data.

## Operation close to the surface

Operation close to the water surface can be affected by bubbles, waves, and changing submersion. Keep the DVL fully submerged and avoid positions where waves or vehicle motion expose the transducers to air.

If the DVL loses bottom lock near the surface, check for:

* Bubbles passing across the transducers.
* Waves causing pitch and roll.
* The DVL or mounting bracket moving relative to the vehicle.
* Beam paths that intersect the hull, dock, tank wall, or other nearby structures.

## Other acoustic instruments

Other acoustic instruments can interfere with DVL measurements if they transmit at the same time or in a similar frequency range.

If several acoustic instruments are used together:

1. Test each instrument by itself first.
2. Check DVL performance with the other instruments active.
3. Use trigger or synchronization options when needed. See [Integration](integration.md#triggering-and-synchronization).

## Grounding, power, and cable considerations

Follow the electrical page for your model:

* [DVL electrical connection](electrical.md)
* [DVL A50/A125 serial interface](electrical.md#dvl-a50-and-dvl-a125-serial-interface)
* [DVL A100/A250 serial interface](electrical.md#dvl-a100-and-dvl-a250-serial-interface)

General checks:

* Use an adequate power supply for the model.
* Protect the cable from strain and abrasion.
* Keep power and communication wiring away from high-noise wiring when practical.
* Follow the shield grounding guidance in the electrical documentation.

## First water test

1. Keep the DVL submerged before powering it for normal operation.
2. Open the web GUI and check that the DVL is connected.
3. Confirm that acoustics are enabled.
4. Check that the DVL gets bottom lock in a simple test environment.
5. Check velocity, altitude, and transducer distances.
6. If the output looks wrong, verify mounting rotation, range mode, line of sight, bubbles, vibration, and acoustic interference.

See [How to diagnose](how-to-diagnose.md) if the DVL does not behave as expected.
