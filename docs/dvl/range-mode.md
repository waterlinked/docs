# Range mode

Range mode configuration can instruct the DVL to search for bottom lock in a limited altitude range. This can improve performance when the expected minimum and maximum altitude are known, for example in a river, pool, tank, or other constrained environment.

## Model applicability

The range-mode concept applies to all DVLs. The table below documents the currently published A50/A125 range modes.

<!-- TODO: Confirm final DVL A100 and DVL A250 range mode altitude boundaries and update this page with a model-specific table or model column. -->

On supported models, the same configuration parameter can also enable [water tracking](water-tracking.md).

## Configuration format

| Range specifier | Behavior |
| -- | -- |
| `auto` | The DVL searches for bottom lock in its full operational area. This is the default. |
| `=a` | The DVL is locked to range mode `a`, where `a` is a number from `0` to `4`. |
| `a<=b`| The DVL searches for bottom lock from range mode `a` through range mode `b`. |
| `wt` | Enable water tracking on supported software and models. See [Water tracking](water-tracking.md). (Only A50/A125)|

## DVL A50/A125/A100 range modes

| Range mode | Lower altitude (m) | Upper altitude (m) | Update rate per second (Hz) |
| -- | -- | -- | -- |
| 0 | 0.05 | 0.6 | 15 |
| 1 | 0.3 | 3.0 | 10 |
| 2 | 1.5 | 14 | 5 - 6 |
| 3 | 7.7 | 36 | 7 - 8 |
| 4 | 15 | max | 2 - 4 |
| wt | 1.5 | 4.5 | 2 |



## DVL A250 range modes


| Range mode | Lower altitude (m) | Upper altitude (m) | Update rate per second (Hz) |
| -- | -- | -- | -- |
| 0 | 0.3 | 3.0 | 10 |
| 1 | 1.5 | 14 | 5 - 6 |
| 2 | 7.7 | 72 | 7 - 8 |
| 3 | 15 | max | 2 - 4 |

## Set with TCP JSON API or serial protocol

### TCP JSON API
* [DVL A50/A125 TCP JSON API configuration](dvl-json-protocol.md#configuration-over-json)
* [DVL A100/A250 TCP JSON API configuration](dvl-a250_a100-json-protocol.md#configuration-over-json)

### Serial
* [DVL A50/A125 serial configuration](dvl-serial-protocol.md#setting-configuration-parameters)
* [DVL A100/A250 serial configuration](dvl-a250_a100-serial-protocol.md#setting-configuration-parameters)
