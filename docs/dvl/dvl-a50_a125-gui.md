# DVL A50/A125 web GUI

This page applies to DVL A50 and DVL A125.

The DVL A50/A125 web GUI can be used to check live status, configure settings, select outputs, collect diagnostic logs, and view software and device information.

## Open the web GUI

1. Connect power and Ethernet to the DVL.
2. Make sure the DVL is submerged before normal operation.
3. Open a web browser and go to the DVL address.
4. See [Network Setup](networking.md) if the web GUI does not open.

## Demo GUI

Use the public [DVL A50/A125 demo GUI](https://dvl.demo.waterlinked.com/#/) to explore the interface without connecting to a DVL.

The demo runs on simulated data. It does not replace testing with your own DVL in water. Hardware status, bottom lock, acoustic conditions, and output integrations must still be verified on the real installation.

## Dashboard { #dashboard-live-data }

Use the dashboard to view the current DVL status, velocity data, bottom lock state, altitude, dead-reckoning information, and other live information.

Open the public [dashboard demo page](https://dvl.demo.waterlinked.com/#/).

### Verify bottom lock

1. Confirm that the DVL is submerged and the transducers have a clear line of sight to the bottom.
2. Open the dashboard.
3. Check that acoustics are enabled.
4. Check that velocity is valid.
5. Check that altitude is stable and reasonable for the test environment.
6. Check the figure of merit (FOM) or uncertainty indicator if shown.

!!! note
    Figure of merit is a confidence indicator for the velocity estimate. A high value means the velocity measurement is less certain.

If velocity is invalid or bottom lock is unreliable, see [How to diagnose](how-to-diagnose.md).

### View velocity and navigation

1. Open the dashboard.
2. Check that velocity is valid before using the values.
3. Review speed, altitude, ping rate, and FOM.
4. Use the horizontal and vertical velocity views to confirm the movement direction.
5. Use the map view only after checking the dead reckoning limitations.

See [Dead reckoning](dead-reckoning.md) for the reference frame and limitations.

!!! warning
    Dead reckoning will drift over time. Do not use the map view as an absolute position reference unless your system also provides an external position reference.

## Outputs

Use the outputs page to configure which data outputs are enabled and how data is sent from the DVL.

Open the public [outputs demo page](https://dvl.demo.waterlinked.com/#/outputs).

1. Open the outputs page.
2. Select the output protocol required by your integration.
3. Configure serial settings if you use the UART interface.
4. Save the configuration.
5. Reconnect or restart the receiving system if required by the integration.

See [Settings and configuration](configuration.md#output-settings), [Integration](integration.md), [DVL A50/A125 TCP JSON API](dvl-json-protocol.md), and [DVL A50/A125 serial protocol](dvl-serial-protocol.md).

## Configuration

Use the configuration page to change DVL settings such as speed of sound, range mode, mounting rotation, water tracking, network settings, and maintenance actions.

Open the public [configuration demo page](https://dvl.demo.waterlinked.com/#/config).

See [Settings and configuration](configuration.md), [Axes](axes.md), [Range mode](range-mode.md), and [Water tracking](water-tracking.md).

## Diagnostics

Use the diagnostics page to view live diagnostic information while the DVL is operating. This can help you see whether status, signal quality, transducer distances, or validity changes when the vehicle moves, thrusters run, or the environment changes.

Open the public [diagnostics demo page](https://dvl.demo.waterlinked.com/#/diagnostic).

See [How to diagnose](how-to-diagnose.md) for symptom-based checks.

## Diagnostic log

The DVL A50/A125 web GUI has a separate diagnostic log page.

Use the diagnostic log page to collect a diagnostic log when troubleshooting or when requested by Water Linked support.

Open the public [diagnostic log demo page](https://dvl.demo.waterlinked.com/#/collect).

See [Diagnostic log](diagnostic-log.md) for collection guidance and the [support package checklist](support-package-checklist.md) before contacting Water Linked support.

## About

Use the About page to view software version, chip ID, product information, release notes, and software update actions if available.

Open the public [About demo page](https://dvl.demo.waterlinked.com/#/about).

Software updates are covered in [Software updates](sw-update.md).
