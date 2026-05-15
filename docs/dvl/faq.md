# FAQ

This FAQ applies to DVL A50, DVL A100, DVL A125, and DVL A250 unless a question states otherwise.

## 1. How do I access the web GUI? { #how-do-i-access-the-gui }

Applies to: all DVL models

Connect power and Ethernet, then open the DVL address in a web browser. Ethernet is recommended for first setup because it gives access to the web GUI, diagnostics, configuration, software updates, and the TCP data stream.

See [Network setup](networking.md) for mDNS, fallback IP, direct Ethernet connection, and TCP data stream information.

---

## 2. What should I check if I cannot connect to the web GUI? { #what-should-i-check-if-i-cannot-connect-to-the-gui }

Applies to: all DVL models

Check:

* Power and LED status.
* Ethernet cable and connector condition.
* Computer network configuration.
* Whether mDNS is available on the network.
* The fallback IP address if mDNS does not resolve.
* Whether the DVL is in thermal shutdown.

See [Network setup](networking.md), [DVL electrical connection](electrical.md), and [How to diagnose](how-to-diagnose.md).

---

## 3. Why does the DVL lose connection? { #why-does-the-dvl-lose-connection }

Applies to: all DVL models

Common causes include insufficient power, poor cable or connector contact, thermal shutdown, and network configuration issues.

Check [Network setup](networking.md), [DVL electrical connection](electrical.md), and [How to diagnose](how-to-diagnose.md).

---

## 4. Why does the DVL lose bottom lock? { #why-does-the-dvl-lose-bottom-lock }

Applies to: all DVL models

Bottom lock depends on altitude, bottom conditions, line of sight, acoustic noise, vehicle motion, and range mode. If bottom lock is lost, check that the bottom is within the selected range, all beams have a clear path, and the DVL is not operating in bubbles or disturbed water.

See [Loss of bottom lock](how-to-diagnose.md#loss-of-bottom-lock) and [Installation](installation.md).

---

## 5. Why does the DVL velocity become invalid or drop to zero? { #why-does-the-dvl-velocity-become-invalid-or-drop-to-zero }

Applies to: all DVL models

Velocity can become invalid when the DVL cannot form a valid velocity estimate. Common causes include loss of bottom lock, wrong range mode for the current altitude, blocked beam paths, bubbles, vibration, acoustic interference, or operation outside the conditions where the DVL can track reliably.

See [Invalid velocity](how-to-diagnose.md#invalid-velocity).

---

## 6. How do I download a diagnostic log? { #how-do-i-download-diagnostics }

Applies to: all DVL models

Open the web GUI diagnostics or diagnostic log page, put the DVL in the same environment where the issue occurs, enter a short issue description, create the log, and download it.

See [Diagnostic log](diagnostic-log.md) and [Download diagnostic log](how-to-diagnose.md#download-diagnostics).

---

## 7. What information should I send to Water Linked support? { #what-information-should-i-send-to-water-linked-support }

Applies to: all DVL models

Use the [Support package checklist](support-package-checklist.md). The most useful items are the diagnostic log, DVL model, serial number if available, software version, failure description, mounting description, installation photos, operating altitude, speed, range mode, tracking mode, environment, active acoustic instruments, and relevant web GUI screenshots.

---

## 8. How do I choose range mode? { #how-do-i-choose-range-mode }

Applies to: all DVL models

Use automatic range mode unless you know that the DVL should only search within a limited altitude range. If bottom lock is unreliable, make sure the selected range mode includes the actual altitude.

See [Range mode](range-mode.md).

<!-- TODO: Confirm final DVL A100/A250 range-mode tables before adding model-specific range-mode examples. -->

---

## 9. What is periodic cycling? { #what-is-periodic-cycling }

Applies to: all DVL models

Periodic cycling is a setting that is enabled by default. Every 10 seconds, the DVL checks that the bottom it has locked onto is the actual bottom and that there are no closer reflections that should be treated as the real bottom.

It is useful in reflective environments with many multipath reflections, such as tanks or pools. Some measurements are lost during the validation check. If you operate in open water with stable bottom conditions and need as many measurements as possible, consider turning periodic cycling off.

See [Periodic cycling](configuration.md#periodic-cycling).

---

## 10. What is the difference between bottom tracking and water tracking? { #what-is-the-difference-between-bottom-tracking-and-water-tracking }

Applies to: model-specific

Bottom tracking estimates velocity relative to the seabed or another reflecting surface. Water tracking estimates velocity relative to the water column.

Water tracking can be useful when bottom lock is not available or when velocity relative to the water column is required. It should not be treated as bottom-relative velocity.

See [Water tracking](water-tracking.md).

---

## 11. Can air bubbles affect DVL performance? { #can-air-bubbles-affect-dvl-performance }

Applies to: all DVL models

Yes. Air bubbles can scatter or block the acoustic signal and cause weak signal, noisy measurements, invalid velocity, or loss of bottom lock.

Check for bubbles from thrusters, propellers, pumps, hull turbulence, waves, or the DVL moving in and out of the water. See [Air bubbles](how-to-diagnose.md#air-bubbles) and [Installation](installation.md#thrusters-propellers-hulls-and-bubbles).

---

## 12. Can thrusters or propellers affect DVL performance? { #can-thrusters-or-propellers-affect-dvl-performance }

Applies to: all DVL models

Yes. Thrusters, propellers, hull edges, pumps, and other moving water sources can create turbulence and bubbles in the beam paths. Compare DVL performance with thrusters or propellers off and on, and consider moving the DVL away from disturbed flow if performance changes.

See [Thrusters, propellers, and hull turbulence](how-to-diagnose.md#thrusters-propellers-and-hull-turbulence).

---

## 13. Can mechanical vibration affect DVL performance? { #can-mechanical-vibration-affect-dvl-performance }

Applies to: all DVL models

Yes. Loose brackets, flexible poles, or vibrating mounts can make measurements noisy because the DVL moves relative to the vehicle or boat.

Use a rigid mount and check whether motors, pumps, or thrusters excite the bracket. See [Mechanical vibration and flexible mounts](how-to-diagnose.md#mechanical-vibration-and-flexible-mounts) and [Rigid mounting and vibration](installation.md#rigid-mounting-and-vibration).

---

## 14. Can the DVL be used on a boat? { #can-the-dvl-be-used-on-a-boat }

Applies to: all DVL models

Yes, but the installation should keep the DVL rigidly mounted, fully submerged, and away from aerated or turbulent flow. Verify bottom lock and velocity at the intended boat speed before relying on the data.

See [Boat-mounted installations](how-to-diagnose.md#boat-mounted-installations) and [Boat-mounted use](installation.md#boat-mounted-use).

---

## 15. How close to the water surface can the DVL be mounted? { #how-close-to-the-water-surface-can-the-dvl-be-mounted }

Applies to: all DVL models

The DVL should stay fully submerged during operation. Near the surface, waves, air ingestion, turbulence, and bubbles can affect the acoustic signal. Exact surface-clearance limits depend on the installation and operating conditions.

See [Operation close to the water surface](how-to-diagnose.md#operation-close-to-the-water-surface) and [Operation close to the surface](installation.md#operation-close-to-the-surface).

---

## 16. Can other acoustic instruments interfere with the DVL? { #can-other-acoustic-instruments-interfere-with-the-dvl }

Applies to: all DVL models

Yes. Other acoustic instruments can interfere if they transmit at overlapping times or create strong acoustic noise in the DVL operating environment.

Test the DVL with the other instruments off, then on. If performance changes, consider physical separation, beam geometry, or trigger/synchronization. See [Active acoustic interference from other sensors](how-to-diagnose.md#active-acoustic-interference-from-other-sensors) and [Triggering and synchronization](integration.md#triggering-and-synchronization).

---

## 17. Which interface should I use: Ethernet, serial, PD0, PD4, or PD6? { #which-interface-should-i-use-ethernet-serial-pd0-pd4-or-pd6 }

Applies to: all DVL models

Use Ethernet and the web GUI for first setup, diagnostics, configuration, and testing. Use the Water Linked TCP JSON API over Ethernet for custom software integrations. Use the Water Linked serial protocol for direct vehicle integration over the serial interface.

Use PD4 or PD6 only when the receiving system already supports that format. PD0 is planned for DVL A100 and DVL A250, but is not available yet.

See [Integration overview](integration.md), [PD formats](dvl-pd-formats.md), [DVL electrical connection](electrical.md), and the protocol pages for your model.

---

## 18. Does the DVL have an RS232 interface? { #does-the-dvl-have-an-rs232-interface }

Applies to: model-specific

DVL A50 and DVL A125 do not use RS232. They use a 3.3 V UART electrical interface that is 5 V tolerant.

DVL A100 and DVL A250 use RS232.

The serial data protocol is separate from the electrical interface. See [DVL electrical connection](electrical.md#terminal-serial-interface), [DVL A50/A125 serial protocol](dvl-serial-protocol.md), and [DVL A100/A250 serial protocol](dvl-a250_a100-serial-protocol.md).

---

## 19. What is the latency when using the API over Ethernet? { #what-is-the-latency-when-using-the-api-over-ethernet }

Applies to: all DVL models

In our measurements, TCP JSON message latency was typically around 4 ms average, with 2 ms standard deviation and an observed maximum of 13 ms.

This is not a hard real-time guarantee. Actual latency can depend on network setup, host system, load, and integration method.

See [Integration](integration.md#ethernet-jsontcp), [DVL A50/A125 TCP JSON API](dvl-json-protocol.md), and [DVL A100/A250 TCP JSON API](dvl-a250_a100-json-protocol.md).

---

## 20. How does triggering and synchronization work? { #how-does-triggering-and-synchronization-work }

Applies to: model-specific

Triggering lets an external system control DVL pinging. This can be useful when several acoustic instruments are installed on the same vehicle and should avoid transmitting at the same time.

Triggering and synchronization are handled through the integration interface, not as a web GUI workflow. See [Integration overview](integration.md#triggering-and-synchronization) and the protocol page for your model.

<!-- TODO: Confirm exact timing requirements and supported trigger configurations before publishing detailed trigger setup rules. -->

---

## 21. What is the operating range? { #what-is-the-operating-range }

Applies to: all DVL models

See [Overview](overview.md#dvl-comparison) for model comparison and [Range mode](range-mode.md) for range-mode configuration notes.

---

## 22. What is the velocity output frequency? { #what-is-the-velocity-output-frequency }

Applies to: all DVL models

Velocity output frequency varies with altitude and range mode. See [Range mode](range-mode.md) for the common range-mode concept and model applicability notes.

<!-- TODO: Confirm A100 and A250 range mode values before publishing model-specific output frequency limits. -->

---

## 23. What is the source level or SPL? { #what-is-the-source-level-or-spl }

Applies to: all DVL models

See the product comparison table in [Overview](overview.md). The FAQ does not repeat these values so that specifications are maintained in one place.

<!-- TODO: Confirm A100 and A250 source level/SPL before publishing it in the overview comparison table. -->

---

## 24. Can I test or operate the DVL in air? { #can-i-test-or-operate-the-dvl-in-air }

Applies to: all DVL models

You will not get valid velocity measurements in air. It is possible to power the DVL out of water for a short time, but it warms up quickly. If possible, keep the DVL submerged when powered.

A practical lab setup is to keep the DVL submerged in a small bucket of water.

If the DVL must be powered out of water for a short time, disable acoustics in the web GUI to reduce heating.

---

## 25. Can the DVL overheat? { #can-the-dvl-overheat }

Applies to: all DVL models

Yes. The DVL has thermal shutdown to avoid damage. It issues a warning before shutting down at 55℃. Once it cools below 50℃, it automatically restarts. If the overheating issue is not addressed, it may repeat this shutdown/restart cycle.

Keep the DVL in water when powered for normal operation.

---

## 26. Do I need to calibrate the IMU each time I power on the DVL? { #do-i-need-to-calibrate-the-imu-each-time-i-power-on-the-dvl }

Applies to: all DVL models

No. The calibration is saved in memory.

---

## 27. Will temperature affect the IMU? { #will-temperature-affect-the-imu }

Applies to: all DVL models

Yes. The IMU can perform differently under temperatures that differ significantly from the conditions where it was calibrated.

---

## 28. Why does the yaw angle change rapidly? { #why-does-the-yaw-angle-change-rapidly }

Applies to: all DVL models

Yaw angle in the web GUI may increase or otherwise change rapidly if the gyro has not been calibrated or if the temperature changes.

See:

* [Dead reckoning](dead-reckoning.md#starting-dead-reckoning)

!!! note
    If only velocity output is required, you can ignore yaw drift. Yaw is only relevant if dead reckoning is used.

---

## 29. Can the DVL be used as an ADCP? { #can-the-dvl-be-used-as-an-adcp }

Applies to: all DVL models

No. The DVL algorithms are designed to track reflections from the seafloor or another reflecting surface. An ADCP measures reflections from water-borne particles at various depths, which uses a different processing approach.

---

## 30. Will the DVL work over a soft seabed, such as sand? { #will-the-dvl-work-over-a-soft-seabed-such-as-sand }

Applies to: all DVL models

Yes, the DVL can operate over soft bottoms. Softer seabeds can absorb more acoustic energy, which may reduce the maximum altitude where the DVL can reliably track. The effect varies by environment and may require testing.

---

## 31. How do I update software or firmware? { #how-do-i-update-software-or-firmware }

Applies to: all DVL models

Use the common [Software updates](sw-update.md) page for all DVL models.

---

## 32. Which DVL model should I choose? { #which-dvl-model-should-i-choose }

Applies to: all DVL models

Choose the DVL model based on required altitude range, platform size, depth rating, velocity range, physical interface, and integration requirements.

See [Overview](overview.md#dvl-comparison) for the product comparison table and the model pages for mechanical details.

---

## 33. How should I maintain the DVL? { #how-should-i-maintain-the-dvl }

Applies to: all DVL models

After operating in seawater, brackish water, chlorinated pools, or any medium other than freshwater, rinse the DVL thoroughly with fresh water to remove residues and salt deposits. Once dry, wipe the exterior with a clean, dry cloth. Avoid solvents or abrasive cleaners.
