# Water tracking

Water tracking is a mode where the DVL estimates velocity relative to the water column instead of the sea bottom. It can be useful when the DVL cannot get bottom lock, or when the movement of the water itself is relevant.

## Supported models

| Model | Water tracking |
| :--- | :--- |
| DVL A50 | Supported |
| DVL A100 | Planned, not available yet |
| DVL A125 | Supported |
| DVL A250 | Planned, not available yet |

Water tracking requires a software version with water tracking support. See [Software updates](sw-update.md) for update instructions. For DVL A100 and DVL A250, water tracking is planned but not available yet.

## Mode of operation

Water tracking uses acoustic reflections from the water column, approximately `1.5 m to 4.5 m` below the DVL. It is intended for use when the distance to the bottom is more than 4.5 m.

When the bottom is within the normal bottom-tracking range of the DVL, water-tracking velocity estimates can be affected by bottom reflections. With fast currents the velocity estimate can become invalid, and with slow currents the estimate can be biased toward the bottom-relative velocity.

The maximum measurable velocity in water tracking mode is 7.5 m/s.

Update rate is `2 Hz`.

!!! warning
    Dead reckoning performance with water tracking is untested and can give large errors.

## Web GUI

The dashboard shows the active tracking mode. On supported software, the tracking mode can be selected from the configuration page.

The diagnostic page still shows spatial velocity, per-transducer velocity, and validity. In water tracking mode, the acoustic signal view shows signal strength and noise as separate time-based graphs.

## Enable water tracking

Water tracking is enabled by setting `range_mode` to `wt`. Select the interface you integrate with:

=== "TCP JSON API"

    Available in TCP JSON API version `json_v3.2` and up for supported models. Use the TCP JSON API configuration method for your model:

    * [DVL A50/A125 TCP JSON API configuration](dvl-json-protocol.md#configuration-over-json)
    * DVL A100/A250 TCP JSON API configuration is planned for water tracking and is not available yet.

    Enable water tracking by setting `range_mode` to `wt`:

    ```json
    {"command":"set_config","parameters":{"range_mode":"wt"}}
    ```

    Set `range_mode` back to `auto` to return to automatic bottom tracking:

    ```json
    {"command":"set_config","parameters":{"range_mode":"auto"}}
    ```

    Water tracking does not introduce a separate report type. The DVL continues to use the normal velocity-and-transducer report, with the field `"type"` showing the active tracking mode. When water tracking is active, the report describes velocity relative to the water column rather than velocity relative to the bottom and the `"type"` will be `"velocity_water"`.

    See the TCP JSON API for your model for the report fields:

    * [DVL A50/A125 TCP JSON API velocity-and-transducer report](dvl-json-protocol.md#velocity-and-transducer-report)
    * DVL A100/A250 TCP JSON API water-tracking report fields are planned and are not available yet.

=== "Serial API"

    Available in serial protocol >= `2.7.0` for supported models. Use the serial configuration method for your model:

    * [DVL A50/A125 serial configuration](dvl-serial-protocol.md#configuration-over-serial)
    * DVL A100/A250 serial configuration for water tracking is planned and is not available yet.

    Enable water tracking by setting `range_mode` to `wt` using the `wcs` command:

    ```text
    wcs,,,,,wt,
    ```

    Set `range_mode` back to `auto` to return to automatic bottom tracking:

    ```text
    wcs,,,,,auto,
    ```

    Water tracking introduces a serial report called `wrs`, which is similar to the `wrz` report but does not include altitude data. Use this data when water tracking is activated.

    ```text
    wrs,[vx],[vy],[vz],[valid],[fom],[covariance],[time_of_validity],[time_of_transmission],[time],[status]
    ```

    See the serial protocol for your model for the report format:

    * [DVL A50/A125 serial velocity report](dvl-serial-protocol.md#velocity-report-wrs)
    * DVL A100/A250 serial water-tracking reports are planned and are not available yet.
