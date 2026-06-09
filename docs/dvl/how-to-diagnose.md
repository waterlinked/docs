# How to diagnose

This page applies to all our DVLs unless otherwise noted.

Use this guide when the DVL is not performing as expected, cannot get bottom lock, reports invalid velocity, or produces noisy measurements.

**Jump to a symptom:**

* [Invalid velocity](#invalid-velocity)
* [Loss of bottom lock](#loss-of-bottom-lock)
* [Weak signal or noisy measurements](#weak-signal-or-noisy-measurements)
* [Air bubbles](#air-bubbles)
* [Thrusters, propellers, and hull turbulence](#thrusters-propellers-and-hull-turbulence)
* [Mechanical vibration and flexible mounts](#mechanical-vibration-and-flexible-mounts)
* [Operation close to the water surface](#operation-close-to-the-water-surface)
* [Obstructed beam paths / line of sight](#obstructed-beam-paths-line-of-sight)
* [Active acoustic interference from other sensors](#active-acoustic-interference-from-other-sensors)
* [Thermal shutdown](#thermal-shutdown)

## Before contacting support

1. Confirm that the DVL is powered and submerged.
2. Check the LED status:
    * [LED signals](electrical.md#led-signals)
3. Check wiring and cable condition:
    * [DVL electrical connection](electrical.md)
    * [DVL A50/A125 serial interface](electrical.md#dvl-a50-and-dvl-a125-serial-interface)
    * [DVL A100/A250 serial interface](electrical.md#dvl-a100-and-dvl-a250-serial-interface)
4. Open the web GUI:
    * [DVL A50/A125 web GUI](dvl-a50_a125-gui.md)
    * [DVL A100/A250 web GUI](dvl-a250_a100-gui.md)
5. Confirm that the software is up to date:
    * [Software updates](sw-update.md)
6. Review [Installation](installation.md) for mounting, bubbles, vibration, and acoustic interference.
7. Use the [Support package checklist](support-package-checklist.md) before contacting Water Linked support.

## Download diagnostic log { #download-diagnostics }

Download a diagnostic log when bottom lock is unreliable, velocity is invalid, the web GUI reports warnings, or Water Linked support asks for one.

Use the common [Diagnostic log](diagnostic-log.md) page for collection instructions and model-specific demo links.

See the [Support package checklist](support-package-checklist.md) before contacting Water Linked support.

## Invalid velocity

Invalid velocity means the DVL does not currently have a valid velocity estimate. Check:

* The DVL is submerged.
* Acoustics are enabled.
* The DVL has a clear line of sight to the seabed.
* The selected range mode includes the current altitude.
* The vehicle or boat speed is reasonable for the operating conditions.
* Bubbles, vibration, and acoustic interference are not affecting the measurement.

If the DVL is in water tracking mode, remember that velocity is relative to the water column, not the bottom. See [Water tracking](water-tracking.md).

## Loss of bottom lock

Bottom lock depends on altitude, bottom conditions, beam paths, acoustic noise, and vehicle motion.

If bottom lock is lost:

1. Check that the bottom is within the operating range.
2. Check that range mode is not too restrictive. See [Range mode](range-mode.md).
3. Check that all beam paths are unobstructed.
4. Check for bubbles and turbulence.
5. Check for other active acoustic instruments.
6. Review [periodic cycling](configuration.md#periodic-cycling), especially in reflective tanks, pools, or open-water tests where every measurement matters.
7. Test in a simpler environment if possible.

## Weak signal or noisy measurements

Weak or noisy measurements can be caused by soft bottoms, acoustic reflections, bubbles, vibration, and other acoustic sources.

Practical checks:

* Compare signal quality with thrusters or motors off and on.
* Test away from tank walls, dock structures, or polished metal surfaces.
* Check whether transducer distances are stable and similar in a flat test area.
* Collect a diagnostic log while the issue is present.

## Air bubbles

Air bubbles can block or scatter the acoustic signal.

Check for bubbles from:

* Thrusters and propellers.
* Hull turbulence.
* Pumps and hoses.
* Waves or surface aeration.
* The DVL moving in and out of the water.

If bubbles are present, try a calmer test condition or a mounting location with cleaner water flow.

## Thrusters, propellers, and hull turbulence

Thrusters, propellers, and hull edges can create turbulent or aerated water. This can reduce signal quality and cause invalid velocity.

When testing:

1. Check DVL output with thrusters or propellers stopped.
2. Check again at the expected operating speed.
3. If performance changes significantly, consider moving the DVL away from the turbulent flow.

Do not assume a fixed safe distance; the required separation depends on the vehicle, speed, and water flow.

## Mechanical vibration and flexible mounts

The DVL should be mounted rigidly to the vehicle or boat. Flexible poles, loose brackets, or vibrating mounts can make measurements noisy.

Check:

* Fasteners are tight.
* The DVL cannot move relative to the vehicle.
* Poles or brackets do not visibly vibrate.
* Motors, pumps, or thrusters are not exciting the mount.

## Operation close to the water surface

Near the surface, waves and bubbles can affect acoustic measurements. The DVL should stay fully submerged during operation.

Check:

* Waves are not exposing the transducers to air.
* The DVL is not passing through surface bubbles.
* Boat pitch, roll, or heave is not making the beam paths unstable.

## Boat-mounted installations

For boat-mounted DVLs:

* Use a rigid mount.
* Keep the DVL submerged at the expected operating speed.
* Avoid aerated flow from the hull or propeller.
* Check for vibration in the pole or bracket.
* Verify bottom lock and velocity at the intended speed before relying on the data.

See [Installation](installation.md#boat-mounted-use).

## Obstructed beam paths / line of sight

The DVL needs a clear acoustic path from each transducer to the bottom.

Check model-specific line-of-sight information:

* [DVL A50 line of sight](dvl-a50.md#line-of-sight)
* [DVL A100 line of sight](dvl-a100.md#line-of-sight)
* [DVL A125 line of sight](dvl-a125.md#line-of-sight)
* [DVL A250 line of sight](dvl-a250.md#line-of-sight)

<!-- TODO: Add final DVL A100 line-of-sight asset when available. -->
<!-- TODO: Add final DVL A250 line-of-sight asset when available. -->

If one beam shows a different distance or flickers more than the others, check whether that beam is seeing a wall, frame, skid, cable, or other obstruction.

## Active acoustic interference from other sensors

Other acoustic instruments can interfere with DVL measurements, especially if they transmit at the same time.

Check:

1. Run the DVL with other acoustic instruments off.
2. Run the DVL with the other instruments on.
3. If performance changes, consider trigger or synchronization. See [Integration](integration.md#triggering-and-synchronization).

## Thermal shutdown

The DVL has a thermal shutdown mechanism to avoid damage. It issues a warning before shutting down at 55℃. Once it cools below 50℃, it automatically restarts. If the overheating issue is not addressed, it may repeat this shutdown/restart cycle.

If thermal shutdown occurs, confirm that the DVL is submerged and that acoustics are disabled when the DVL must be powered out of water for a short time.

## What to send to Water Linked support

Submit a [support ticket](https://waterlinked.com/support) with the information listed in the [Support package checklist](support-package-checklist.md).
