# Time

The DVL continously attempts to synchronize time using the Network Time Protocol (NTP).
When not synchronized with NTP, it is also possible to set time manually.

## Supported models

|Model|Support|
|-|-|
|A50|Supported, starting with software release 2.7.2|
|A100|Planned. Not supported in 3.2.0|
|A125|Supported, starting with software release 2.7.2|
|A250|Planned. Not supported in 3.2.0|

See [Software updates](sw-update.md) for update instructions.

## Importance of setting time

The DVL does know the current time when booting, and initial timestamps output from the DVL will be relative to some arbitrary time in the past.
It is recommended to synchronize the DVL's time before using its output.

## NTP server address configuration: auto or custom

The NTP server address can be configured as either "auto" or a specific server address.
When NTP server address is configured as "auto", the DVL will attempt to reach a default pool of internet time servers.
The configuration is persisted across reboots.

## Setting manual time

When the DVL has not yet achieved NTP sync it is possible to set time manually.
This is useful in deployment scenarios without a reachable NTP server, or as a fallback until an NTP server becomes available.
A manually set time will be disregarded if the DVL later achieves NTP sync.

## Time status

The DVL separates between NTP configuration and time status.
Time status consists of the following fields:

|Field|Description|
|-|-|
| `system_time` | system time |
| `ntp_synced` | true if synchronized to NTP source, false otherwise |
| `ntp_synced_to` | address the sonar is synchronized to if NTP is synchronized, "" otherwise |
| `ntp_seconds_since_last_sync` | seconds since last NTP sync if NTP is synchronized |

## NTP Force sync

A NTP force sync operation can be triggered which will attempt to achieve NTP sync within a specified timeout.
Upon achieving sync, or when the timeout expires, the operation will respond with the following fields: 

|Field|Description|
|-|-|
|`success`|true if NTP sync was achieved within timeout, false otherwise|
|`message`|human-readable message|
|`status`|Time status as described [here](#time-status) |

!!! warning
    `success` true means the DVL achieved NTP sync. To assert the DVL is synchronized to a specific NTP server, check the returned status.

!!! warning
    The operation can cause abrupt jumps in system time, and is not recommended for use while reading DVL output.

## Web GUI

On supported models there is a "System time configuration" section in the Configuration page.

## TCP JSON API

Time configuration is available in TCP JSON API `json_v3.3` and up for supported models:

* [DVL A50/A125 TCP JSON time API](./dvl-json-protocol.md#time)

## Serial API

Time configuration is available in serial protocol `2.8.0` and up for supported models:

* [DVL A50/A125 Serial time API](./dvl-serial-protocol.md)