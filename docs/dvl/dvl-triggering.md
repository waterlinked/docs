# DVL triggering

The DVL has different options for triggering acoustic pings to perform a velocity measurement. Triggering can be useful when you need to synchronize the DVL with other sensors.

| Model | Software triggering | Hardware triggering |
| ---- | ---- | ---- |
| A50/A125 | Yes | No |
| A100/A250 | Yes | Yes |

## Hardware triggering

Use the RS232 RX line of the DVL to send a trigger command after enabling hardware triggering in the [configuration](configuration.md#operating-configurations).

Once hardware triggering is enabled, transmit a "NUL" ASCII character (Ctrl + @) to send a ping. The trigger is detected on the falling edge of the signal.

<!-- TODO: Engineering review: confirm whether the documented hardware trigger pulse width is 78.1 s +/- 4.3 microseconds or a different unit before publishing the exact value. -->

You can send this trigger signal as often as needed. If the DVL is already transmitting, it discards the signal.

!!! warning
    Acoustics must be enabled. If acoustics are disabled, hardware triggering will not work.

## Software triggering

Software triggering is available for all DVL models. It triggers a ping over the TCP JSON API or serial protocol. Acoustics must be disabled for this to work.

Software triggering differs from hardware triggering because it is sent as a request to the DVL and placed in a ping queue. The queue can store up to 15 requests, which are executed one after another until the queue is empty.

See the software ping command in [Commands](configuration.md#commands).

Because this method depends on the internal state of the DVL, the ping queue, and Ethernet jitter if Ethernet is used, the exact ping time is less predictable than with hardware triggering.

!!! warning
    Disable acoustics before using software triggering. This is different from hardware triggering.
