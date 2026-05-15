# DVL A100/A250 web GUI

This page applies to DVL A100 and DVL A250.

The DVL A100/A250 web GUI can be used to check live status, configure settings, view diagnostics, collect diagnostic logs, and view software and device information.

## Open the web GUI

1. Connect power and Ethernet to the DVL.
2. Make sure the DVL is submerged before normal operation.
3. Open a web browser and go to the DVL address:
    * `http://waterlinked-dvl` when mDNS is available.
    * `http://192.168.194.95` when using the fallback IP.
4. See [Network Setup](networking.md) if the web GUI does not open.

## Demo GUI

Use the public [DVL A100/A250 demo GUI](https://dvl2.demo.waterlinked.com/) to explore the interface without connecting to a DVL.

The demo runs on simulated data. It does not replace testing with your own DVL in water. Hardware status, bottom lock, acoustic conditions, and output integrations must still be verified on the real installation.

## Dashboard { #velocity-and-navigation }

Use the dashboard to view the current DVL status, velocity data, bottom lock state, dead-reckoning information, and other live information.

Open the public [dashboard demo page](https://dvl2.demo.waterlinked.com/).

### Verify bottom lock

1. Confirm that the DVL is submerged and the transducers have a clear line of sight to the bottom.
2. Open the dashboard.
3. Check that acoustics are enabled.
4. Check that velocity is valid.
5. Check that altitude and transducer distances are stable and reasonable for the test environment.
6. If you use the data stream for integration, compare the web GUI status with the TCP JSON API or serial output.

!!! note
    A DVL can be connected and healthy without having bottom lock. Bottom lock also depends on altitude, bottom conditions, acoustic noise, range mode, and vehicle motion.

If velocity is invalid or bottom lock is unreliable, see [How to diagnose](how-to-diagnose.md).

### View velocity and navigation

1. Open the dashboard.
2. Check that velocity is valid before using the values.
3. Review horizontal velocity, vertical velocity, altitude, and transducer validity.
4. Use figure of merit or uncertainty indicators as a confidence check when they are available.
5. Use the local map/dead-reckoning view only after checking the dead reckoning limitations.

See [Dead reckoning](dead-reckoning.md) for the reference frame and limitations.

!!! warning
    Dead reckoning will drift over time. Do not use the map view as an absolute position reference unless your system also provides an external position reference.

## Configuration

Use the configuration page to change DVL settings such as speed of sound, range mode, mounting rotation, network settings, and maintenance actions.

Open the public [configuration demo page](https://dvl2.demo.waterlinked.com/#config).

See [Settings and configuration](configuration.md), [Axes](axes.md), [Range mode](range-mode.md), and [Water tracking](water-tracking.md).

Gyro calibration is not needed for DVL A100/A250.

<!-- TODO: Confirm final DVL A100/A250 web GUI label and workflow for water tracking. -->

<!--## Outputs

The DVL A100/A250 web GUI does not have a separate Outputs page.

Use the configuration page and the protocol references for output configuration until the final GUI labels are confirmed.

See [Settings and configuration](configuration.md#output-settings), [Integration](integration.md), [DVL A100/A250 TCP JSON API](dvl-a250_a100-json-protocol.md), and [DVL A100/A250 serial protocol](dvl-a250_a100-serial-protocol.md).-->

<!-- TODO: Confirm final DVL A100/A250 web GUI label and workflow for output configuration. -->

## Diagnostics and diagnostic log { #diagnostics-and-support }

Use the diagnostics page to view live diagnostic information and collect a diagnostic log when troubleshooting or when requested by Water Linked support.

Open the public [diagnostics demo page](https://dvl2.demo.waterlinked.com/#diagnostics).

See [Diagnostic log](diagnostic-log.md) for collection guidance, [How to diagnose](how-to-diagnose.md) for symptom-based checks, and the [support package checklist](support-package-checklist.md) when preparing a support request.

## About

Use the About page to view software version, chip ID, product information, and software update actions if available.

Open the public [About demo page](https://dvl2.demo.waterlinked.com/#about).

Software updates are covered in [Software updates](sw-update.md).
