# DVL A50/A125 TCP JSON API

The DVL TCP JSON API sends JSON messages over TCP on port 16171. This page applies to DVL A50 and DVL A125.

## Terminology

* DVL - Doppler Velocity Log - Uses hydro-acoustic beams to measure the velocity at which the DVL is moving across a surface (typically an unmoving one such as the sea bottom), and the distance to this surface.
* ACK - Acknowledgement. The command issued was successful.
* NAK - Negative acknowledgement. The command issued failed.
* Ping - A pulse of sound sent by the DVL
* Time of validity - Timestamp of the surface reflection ('center of ping')
* Time of transmission - Timestamp taken directly before sending data over the serial or TCP protocols. The difference between time of transmission and time of validity includes both the time for the acoustic wave to travel from the surface from which it was reflected back to the DVL, and the decoding and processing of this signal internally in the DVL.

## Version

This document describes TCP JSON API version `json_v3.3` (major.minor):

- MAJOR version increments represent incompatible API changes
- MINOR version increments represent additional backwards-compatible functionality

### Version history overview

| Software release | Ethernet protocol version | Main protocol improvements |
| -- | -- | -- |
| 2.7.2 | json_v3.3 | Add TCP JSON time API. Add get_version_info command |
| 2.7.1 | json_v3.2 | Add water tracking mode and tracking mode field in velocity reports |
| 2.6.1 | json_v3.1 | Serial baud rate configurable. Add PD4 format support in serial 'wcp' command. Some serial protocol names [changed](dvl-serial-protocol.md#change-serial-output-protocol-wcp). |
| 2.5.2 | json_v3.1 | Add PD4 format support (experimental)
| 2.4.4 | json_v3.1 | Change gyro calibration to store persistently. Note: gyro calibration commands now take up to 15 seconds.
| 2.4.0 | json_v3.1 | Add ability to trigger pings (TCP JSON API/serial), add configuration for periodic cycling (TCP JSON API/serial)
| 2.2.1 | json_v3 | Add serial output protocol configuration, range mode configuration and calibrate gyro command, Fix missing line ending in configuration (TCP JSON API), fix dark mode enabled naming inconsistency (TCP JSON API), change speed of sound and mounting rotation offset from integer to float
| 2.1.0 | json_v3 | Add configuration, add time_of_validity/time_of_transmission, add covariance (TCP JSON API)
| 2.0.8 | json_v2 | Add position estimation, Add output of orientation angles
| 1.6.0 | - | Initial (velocity only)


## TCP JSON API { #json-protocol-tcp }

### Overview

The DVL supports sending velocity, transducer, and position updates using the Transmission Control Protocol (TCP). The DVL runs a TCP server on port 16171.

The format of each packet is JSON.

In our measurements, TCP JSON message latency was typically around 4 ms average, with 2 ms standard deviation and an observed maximum of 13 ms. This is not a hard real-time guarantee; actual latency can depend on network setup, host system, load, and integration method. See [Integration](integration.md#ethernet-jsontcp).

### PD formats over TCP

PD4 and PD6 are also supported over TCP for all DVL models. See [PD formats](dvl-pd-formats.md) for the canonical PD format descriptions.

### Velocity-and-transducer report

A velocity-and-transducer report is sent for each velocity calculation of the DVL. The rate depends on the altitude of the DVL (distance to the sea bottom or other reflecting surface), but will be in the range 2-15 Hz.

The X, Y, and Z axes are with respect to [body frame](axes.md#body-frame) of the DVL, or the [vehicle frame](axes.md#vehicle-frame) if the DVL is mounted on a vehicle at an angle, specified as a 'mounting rotation offset', from the forward axis of the vehicle.

The messages are delimited by newline.

| Variable | Description |
|----------|-------------|
| time | Milliseconds since last velocity report (ms) |
| vx | Velocity in x direction (m/s) |
| vy | Velocity in y direction (m/s) |
| vz | Velocity in z direction (m/s) |
| fom | Figure of merit, a measure of the accuracy of the velocities (m/s) |
| covariance | Covariance matrix for the velocities. The figure of merit is calculated from this (entries in (m/s)^2) |
| altitude | Distance to the reflecting surface along the Z axis (m) |
| transducers | Is a list containing information from each transducer: [`id`, velocity (m/s), distance (m), rssi (dBm), nsd (dBm), `beam_valid` (True/False)] |
| velocity_valid | If true, the DVL has a lock on the reflecting surface, and the altitude and velocities are valid (True/False) |
| status | 8 bit status mask. Bit 0 is set to 1 for high temperature and DVL will soon enter thermal shutdown. Remaining bits are reserved for future use. |
| time_of_validity | Timestamp of the surface reflection, aka 'center of ping' (Unix timestamp in microseconds) |
| time_of_transmission | Timestamp from immediately before sending of the report over TCP (Unix timestamp in microseconds) |
| tracking_mode | Active tracking mode. `bottom` for bottom tracking, `water` for [water tracking](water-tracking.md). Added in `json_v3.2` |
| format | Format type and version for this report: `json_v3.1` |
| type | Report type: `velocity` or `velocity_water` |

!!! note "Transducer numbering and protocol IDs"
    Mechanical/transducer diagrams number the transducers from 1 to 4. In protocol messages and diagnostic logs, the transducer `id` uses zero-based numbering from 0 to 3. The `id` is therefore the transducer number minus 1.

Example of TCP report (indented for legibility)

```json
{
  "time": 106.3935775756836,
  "vx": -3.713480691658333e-05,
  "vy": 5.703703573090024e-05,
  "vz": 2.4990416932269e-05,
  "fom": 0.00016016385052353144,
  "covariance": [
    [
      2.4471841442164077e-08,
      -3.3937477272871774e-09,
      -1.6659699175747278e-09
    ],
    [
      -3.3937477272871774e-09,
      1.4654466085062268e-08,
      4.0409570134514183e-10
    ],
    [
      -1.6659699175747278e-09,
      4.0409570134514183e-10,
      1.5971971523143225e-09
    ]
  ],
  "altitude": 0.4949815273284912,
  "transducers": [
    {
      "id": 0,
      "velocity": 0.00010825289791682735,
      "distance": 0.5568000078201294,
      "rssi": -30.494251251220703,
      "nsd": -88.73271179199219,
      "beam_valid": true
    },
    {
      "id": 1,
      "velocity": -1.4719001228513662e-05,
      "distance": 0.5663999915122986,
      "rssi": -31.095735549926758,
      "nsd": -89.5116958618164,
      "beam_valid": true
    },
    {
      "id": 2,
      "velocity": 2.7863150535267778e-05,
      "distance": 0.537600040435791,
      "rssi": -27.180519104003906,
      "nsd": -96.98075103759766,
      "beam_valid": true
    },
    {
      "id": 3,
      "velocity": 1.9419496311456896e-05,
      "distance": 0.5472000241279602,
      "rssi": -28.006759643554688,
      "nsd": -88.32147216796875,
      "beam_valid": true
    }
  ],
  "velocity_valid": true,
  "status": 0,
  "tracking_mode": "bottom",
  "format": "json_v3.3",
  "type": "velocity",
  "time_of_validity": 1638191471563017,
  "time_of_transmission": 1638191471752336
}
```

### Dead reckoning report

A dead reckoning report outputs the current speed, position, and orientation of the DVL as calculated by [dead reckoning](dead-reckoning.md), with respect to a [frame](dead-reckoning.md#frame) defined by the axes of the DVL's [body frame](axes.md#body-frame), or [vehicle frame](axes.md#vehicle-frame) if a mounting rotation offset is set, at the start of the dead reckoning run. The expected update rate is 5 Hz.



Variable    | Description
------------|-------------
ts          | Time stamp of report (Unix timestamp in seconds)
x           | Distance in X direction (m)
y           | Distance in Y direction (m)
z           | Distance in downward direction (m)
std         | Standard deviation (figure of merit) for position (m)
roll        | Rotation around X axis (degrees)
pitch       | Rotation around Y axis (degrees)
yaw         | Rotation around Z axis, i.e. heading (degrees)
type        | Report type: `position_local`
status      | Reports if there are any issues with the DVL (0 if no errors, 1 otherwise)
format      | Format type and version for this report: `json_v3`


Example of a dead reckoning report.

```json
{
  "ts": 49056.809,
  "x": 12.43563613697886467,
  "y": 64.617631152402609587,
  "z": 1.767641898933798075,
  "std": 0.001959984190762043,
  "roll": 0.6173566579818726,
  "pitch": 0.6173566579818726,
  "yaw": 0.6173566579818726,
  "type": "position_local",
  "status": 0,
  "format": "json_v3.3"
}

```

### Reset dead reckoning

Dead reckoning can be reset by issuing the `reset_dead_reckoning` command:

```json
{"command": "reset_dead_reckoning"}
```

If the request is successfully received the response will have 'success' set to 'true'. The dead reckoning will have a delay of approximately 50ms until the positioning values being zeroed out. If the response is unsuccessful, the 'success' will be 'false' and a non-empty describing text will be returned in 'error_message'.

```json
{
  "response_to":"reset_dead_reckoning",
  "success": true,
  "error_message": "",
  "result": null,
  "format": "json_v3.3",
  "type": "response"
}
```

### Calibrate gyro

The gyro can be calibrated by issuing the `calibrate_gyro` command:

```json
{"command":"calibrate_gyro"}
```

The response will be as follows if the calibration is successful. If unsuccessful, `success` will be `false`, and a non-empty `error_message` will be provided.

```json
{
  "response_to": "calibrate_gyro",
  "success": true,
  "error_message": "",
  "result": null,
  "format": "json_v3.3",
  "type": "response"
}
```

### Trigger ping

In setups where multiple acoustic sensors are used it can be useful to control the pinging of each acoustic sensor individually. By setting the configuration `acoustic_enabled = false` the pinging of the DVL can be externally controlled. Up to 15 external trigger commands can be queued by issuing the `trigger_ping` command. The DVL will execute each ping in quick succession until no more commands are in the queue.

See [Integration](integration.md#triggering-and-synchronization) for guidance on using triggering with other acoustic instruments.

```json
{"command":"trigger_ping"}
```

The response will be as follows if the command is accepted. If the queue is full, `success` will be `false`, and a non-empty `error_message` will be provided.

```json
{
  "response_to": "trigger_ping",
  "success": true,
  "error_message": "",
  "result": null,
  "format": "json_v3.3",
  "type": "response"
}
```

### Get version info

Get version info by issuing the `get_version_info` command.

```
{"command":"get_version_info"}
```

A successful response looks like this:

```
{
  "response_to": "get_version_info",
  "success": true,
  "error_message": "",
  "result": {
    "chipid": "0xf1440c09140b04",
    "hardware_revision": 4,
    "product_id": 21035,
    "product_name": "DVL A50",
    "variant": "standard",
    "version_short": "2.7.2",
    "version": "2.7.2 (v2.7.1b-10-g44e26c7.2026-05-29T12:51:02.882778)",
    "is_ready": true
  },
  "format": "json_v3.3",
  "type": "response"
}
```

### Time

#### Setting NTP configuration

Set [NTP configuration](./time.md#ntp-server-address-configuration-auto-or-custom) by issuing the `set_time_ntp` command with a `ntp_address` parameter. Set `ntp_address` either to the address of a NTP server, or as "auto".

```json
{
  "command": "set_time_ntp",
  "parameters": {
    "ntp_address": "192.168.0.10"
  }
}
```

A successful response looks like this:

```json
{
  "response_to": "set_time_ntp",
  "success": true,
  "error_message": "",
  "result": null,
  "format": "json_v3.3",
  "type": "response"
}
```

#### Getting NTP configuration

Get [NTP configuration](./time.md#ntp-server-address-configuration-auto-or-custom) by issuing the `get_time_ntp` command.

```json
{
  "command": "get_time_ntp"
}
```

A successful response looks like this:

```json
{
  "response_to": "get_time_ntp",
  "success": true,
  "error_message": "",
  "result": {
    "ntp_address": "auto"
  },
  "format": "json_v3.3",
  "type": "response"
}
```

#### Setting manual time

Set time manually by issuing the `set_time_manual` command with the `now` parameter as a RFC3339 timestamp string.

For more information see [Setting manual time](./time.md#setting-manual-time).

```json
{
  "command": "set_time_manual",
  "parameters": {
    "now": "2026-04-20T09:04:13Z"
  }
}
```

A successful response looks like this:

```json
{
  "response_to": "set_time_manual",
  "success": true,
  "error_message": "",
  "result": null,
  "format": "json_v3.3",
  "type": "response"
}
```

In the event the DVL is already synchronized via NTP, the response will look like this:

```json
{
  "response_to": "set_time_manual",
  "success": false,
  "error_message": "Manual time not allowed when NTP is synchronized",
  "result": null,
  "format": "json_v3.3",
  "type": "response"
}
```

#### Getting time status

Get [time status](./time.md#time-status) by issuing the `get_time_status` command.

```json
{
  "command": "get_time_status"
}
```

The response contains the following fields:

|Field|Description|
|-|-|
| `system_time` | system time in RFC3339 |
| `ntp_synced` | true if synchronized to NTP source, false otherwise |
| `ntp_synced_to` |address the sonar is synchronized to if NTP is synchronized, "" otherwise |
| `ntp_seconds_since_last_sync` | seconds since last NTP sync, or null if not synchronized |

Here is an example response where the DVL is not synchornized with NTP:

```json
{
  "response_to": "get_time_status",
  "success": true,
  "error_message": "",
  "result": {
    "system_time": "2026-04-20T08:48:25Z",
    "ntp_synced": false,
    "ntp_synced_to": "",
    "ntp_seconds_since_last_sync": null
  },
  "format": "json_v3.3",
  "type": "response"
}
```

Here is an example response where the DVL has achieved sync with NTP:

```json
{
  "response_to": "get_time_status",
  "success": true,
  "error_message": "",
  "result": {
    "system_time": "2026-04-20T08:48:25Z",
    "ntp_synced": true,
    "ntp_synced_to": "192.168.0.10",
    "ntp_seconds_since_last_sync": 5
  },
  "format": "json_v3.3",
  "type": "response"
}
```

#### Forcing NTP sync

A [forced NTP sync](./time.md#ntp-force-sync) can be triggered by issuing the `force_sync_ntp` command with the `timeout_seconds` as an integer timeout in seconds.

```json
{
  "command": "force_sync_ntp",
  "parameters": {
    "timeout_seconds": 10
  }
}
```

This will trigger a forced NTP sync in the DVL. The DVL will wait up to `timeout_seconds` for sync to be achieved, finally responding with the following fields:

|Field|Description|
|-|-|
|`success`|true if NTP sync was achieved within timeout, false otherwise. Important: callers that want to achieve sync with a specific address should check the returned status|
|`message`|human-readable message|
|`status`|[time status response body](#getting-time-status)|

Here is an example response where the DVL achieved NTP sync:

```json
{
  "response_to": "force_sync_ntp",
  "success": true,
  "error_message": "",
  "result": {
    "success": true,
    "message": "NTP force-sync successful",
    "status": {
      "system_time": "2026-04-20T09:04:13Z",
      "ntp_synced": true,
      "ntp_synced_to": "192.168.0.10",
      "ntp_seconds_since_last_sync": 0
    }
  },
  "format": "json_v3.3",
  "type": "response"
}
```

Here is an example response where the DVL did not achieve NTP sync:

```json
{
  "response_to": "force_sync_ntp",
  "success": true,
  "error_message": "",
  "result": {
    "success": false,
    "message": "NTP force-sync not successful within timeout",
    "status": {
      "system_time": "2026-04-20T09:04:13Z",
      "ntp_synced": false,
      "ntp_synced_to": "",
      "ntp_seconds_since_last_sync": null
    }
  },
  "format": "json_v3.3",
  "type": "response"
}
```

### Configuration over TCP JSON API { #configuration-over-json }

#### Configuration parameters

| Variable | Description |
|----------|-------------|
| speed_of_sound | Speed of sound (1000-2000 m/s). Integer  |
| mounting_rotation_offset | See the definition of the [vehicle frame](axes.md#vehicle-frame) of the DVL. Typically 0, but can be set to be non-zero if the forward axis of the DVL is not aligned with the forward axis of a vehicle on which it is mounted (0-360 degrees). Integer |
| acoustic_enabled | `true` for normal operation of the DVL,`false` when the sending of acoustic waves from the DVL is disabled (e.g. to save power or slow down its heating up in air) |
| dark_mode_enabled | `false` when the LED operates as [normal](electrical.md#led-signals), `true` for no blinking of the LED (e.g. if the LED is interfering with a camera) |
| range_mode | `auto` when operating as normal, otherwise see [range mode configuration](range-mode.md)  or activate water tracking |
| periodic_cycling_enabled | `true` to enable [periodic cycling](configuration.md#periodic-cycling), `false` to disable it |

#### Fetching current configuration

The current configuration of the DVL can be obtained by issuing the `get_config` command:

```json
{"command": "get_config"}
```

If the configuration is successfully fetched, the response will be in the following format. If not, `success` will be false, a non-empty `error_message` string will be provided, and `result` will be `null`.


```json
{
  "response_to":"get_config",
  "success":true,
  "error_message":"",
  "result":{
    "speed_of_sound":1475.00,
    "acoustic_enabled":true,
    "dark_mode_enabled":false,
    "mounting_rotation_offset":20.00,
    "range_mode":"auto",
    "periodic_cycling_enabled":true
  },
  "format":"json_v3.3",
  "type":"response"
}
```

#### Setting configuration parameters

Setting of configuration parameters can be carried out by issuing a `set_config` in the following format, including those parameters which are to be set:

```json
{"command":"set_config","parameters":{"speed_of_sound":1480}}
```

If the parameters are successfully set, the response will be in the following format. If not, `success` will be false, and a non-empty `error_message` string will be provided.


```json
{
  "response_to": "set_config",
  "success": true,
  "error_message": "",
  "result" :null,
  "format": "json_v3.3",
  "type": "response"
}
```

#### Activating water tracking

Water tracking is enabled by setting `range_mode` to `wt`:

```json
{"command":"set_config","parameters":{"range_mode":"wt"}}
```

#### Deactivate water tracking

Water tracking is deactivated by setting `range_mode` to `auto`:

```json
{"command":"set_config","parameters":{"range_mode":"auto"}}
```
