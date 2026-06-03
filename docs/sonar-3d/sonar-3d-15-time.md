# Time

The sonar continously attempts to synchronize time using the Network Time Protocol (NTP).
When not synchronized with NTP, it is also possible to set time manually.

## Supported versions

Supported on Sonar 3D-15 starting with release 1.7.1

See [Software Updates](./sonar-3d-15-software-update.md) for update instructions.

## Importance of setting time

The sonar does know the current time when booting, and initial timestamps output from the sonar will be relative to some arbitrary time in the past.
It is recommended to synchronize the sonar's time before using its output.

## NTP server address configuration: auto or custom

The NTP server address can be configured as either "auto" or a specific server address.
When NTP server address is configured as "auto", the sonar will attempt to reach a default pool of internet time servers.
The configuration is persisted across reboots.

## Setting manual time

When the sonar has not yet achieved NTP sync it is possible to set time manually.
This is useful in deployment scenarios without a reachable NTP server, or as a fallback until an NTP server becomes available.
A manually set time will be disregarded if the sonar later achieves NTP sync.

## Time status

The sonar separates between NTP configuration and time status.
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
    `success` true means the sonar acieved NTP sync. To assert the sonar is synchronized to a specific NTP server, check the returned status.

!!! warning
    The operation can cause abrupt jumps in system time, and is not recommended for use while reading sonar output.

## Web GUI

On supported versions there is a "Time" section in the Config page.

## HTTP API

The HTTP API allows configuration and inspection of time on the sonar. See [HTTP API](./sonar-3d-15-api.md#http-api).