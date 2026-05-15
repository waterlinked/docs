# Settings and configuration

Use settings when the DVL installation, operating environment, or integration interface changes. Avoid changing settings during an operation unless you understand how the change affects velocity output, bottom lock, and dead reckoning.

## Open settings

Open the DVL web GUI and go to the settings or configuration page for your model family:

* DVL A50/A125: [preview the configuration interface on the demo site](https://dvl.demo.waterlinked.com/#/config)
* DVL A100/A250: [preview the configuration interface on the demo site](https://dvl2.demo.waterlinked.com/#config)

Configuration can also be performed by protocol:

* [DVL A50/A125 TCP JSON API configuration](dvl-json-protocol.md#configuration-over-json)
* [DVL A50/A125 serial configuration](dvl-serial-protocol.md#configuration-over-serial)
* [DVL A100/A250 TCP JSON API configuration](dvl-a250_a100-json-protocol.md#configuration-over-json)
* [DVL A100/A250 serial configuration](dvl-a250_a100-serial-protocol.md#configuration-over-serial)

For DVL A50/A125, output protocol settings are also available in a separate [preview of the output configuration on the demo site](https://dvl.demo.waterlinked.com/#/outputs). 

## Operating configurations

| Setting | Use |
| --- | --- |
| Speed of sound | Set the speed of sound for the water conditions. |
| Mounting rotation offset | Align DVL output with the vehicle frame. See [Axes](axes.md). |
| Acoustic enabled | Enable or disable acoustic pinging. |
| Dark mode | Disable the LED to avoid interference with cameras. |
| Range mode | Limit the altitude range used when searching for bottom lock. See [Range mode](range-mode.md). |
| Periodic cycling | Periodically validate that the DVL is locked to the real bottom. See [Periodic cycling](#periodic-cycling). |
| Water tracking | Use velocity relative to the water column instead of the bottom when supported. See [Water tracking](water-tracking.md). |
| Hardware trigger | Activate [hardware triggering](dvl-triggering.md#hardware-triggering). Only for A100/A250. |

!!! warning
    Incorrect speed of sound, mounting rotation, range mode, tracking mode, or output protocol settings can cause the DVL data to appear incorrect, even when the hardware is functioning properly.

## Periodic cycling

Periodic cycling is available on all DVL models.

When periodic cycling is enabled, the DVL checks every 10 seconds that the bottom it has locked onto is the actual bottom. The check verifies whether there are closer reflections that should be treated as the real bottom.

Periodic cycling is enabled by default. It is useful in reflective environments with many multipath reflections, such as tanks or pools.

The drawback is that some measurements are lost during the validation check. If you operate in open water with stable bottom conditions and need as many measurements as possible, consider turning periodic cycling off. If multipath or reflections are a concern, keeping periodic cycling on can improve bottom validation.

To change periodic cycling:

1. Open the settings or configuration page for your DVL model.
2. Find the periodic cycling setting.
3. Turn it on or off for the operating environment.
4. Save the configuration.

You can also configure periodic cycling with the `periodic_cycling_enabled` parameter over the TCP JSON API or serial protocol.

## Output settings

Use output settings when an external system needs a specific serial protocol, TCP JSON API, or PD format.

1. Choose the protocol required by the receiving system.
2. Configure serial settings if the integration uses the serial interface.
3. Save the configuration.
4. Reconnect or restart the receiving system if required by the integration.

Electrical interfaces differ by model:

* DVL A50 and DVL A125 use a 3.3 V UART interface that is 5 V tolerant.
* DVL A100 and DVL A250 use RS232.

See [DVL electrical connection](electrical.md#terminal-serial-interface) and [Integration](integration.md) before connecting external equipment.


## Commands

Actions that can be performed on the DVL.

| Command | Use |
| --- | --- |
| Reset dead reckoning | Reset the origin and attitude from the current DVL position and attitude. See [Dead reckoning](dead-reckoning.md). |
| Calibrate gyro | Calibrate the gyro. Only for A50/A125. |
| Trigger ping | Tell the DVL to send a single ping. This has more latency than hardware triggering. |

## Network and maintenance

| Setting | Use |
| --- | --- |
| Network configuration | Use DHCP or a static IP address. See [Network Setup](networking.md). |
| System time configuration | Configure NTP or set time manually. |
| Factory reset | Reset all configuration. Reboot is required. |
| Reboot | Restart the DVL. |
