# DVL triggering

The DVL has different options for triggering acoustic pings to perform a velocity measurement. Triggering can be useful when you need to synchronize the DVL with other sensors.

| Model | Software triggering | Hardware triggering |
| ---- | ---- | ---- |
| A50/A125 | Yes | No |
| A100/A250 | Yes | Yes |

## Hardware triggering

Use the RS232 RX line of the DVL to trigger a ping after enabling hardware triggering in the [configuration](configuration.md#operating-configurations).

The trigger is detected on the **falling edge** of the RX signal. The signal must then remain low for approximately **78.1 µs** before returning high.

For a UART connection configured as **115200 baud, 8N1**, this pulse corresponds to transmitting a `"NUL"` ASCII character (`0x00`, Ctrl + @).

Because the trigger is defined by its **pulse timing**, sending a `NUL` character at another baud rate may not produce a valid trigger.

The trigger can be sent as often as needed. If the DVL is already transmitting or receiving, incoming trigger signals are discarded.

!!! warning

    Acoustics must be enabled. Hardware triggering will not work while acoustics are disabled.

## Software triggering

Software triggering is available for all DVL models. It triggers a ping over the TCP JSON API or serial protocol. Acoustics must be disabled for this to work.

Software triggering differs from hardware triggering because it is sent as a request to the DVL and placed in a ping queue. The queue can store up to 15 requests, which are executed one after another until the queue is empty.

See the software ping command in [Commands](configuration.md#commands).

Because this method depends on the internal state of the DVL, the ping queue, and Ethernet jitter if Ethernet is used, the exact ping time is less predictable than with hardware triggering.

!!! warning
    Disable acoustics before using software triggering. This is different from hardware triggering.
