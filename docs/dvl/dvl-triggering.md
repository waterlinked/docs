# DVL triggering

The DVL has different options for triggering acoustic pings to perform a velocity measurement. Triggering can be useful when you need to synchronize the DVL with other sensors.

| Model | Software triggering | Hardware triggering |
| ---- | ---- | ---- |
| A50/A125 | Yes | No |
| A100/A250 | Yes | Yes |

## Hardware triggering

Use the RS232 RX line of the DVL to trigger a ping after enabling hardware triggering in the [configuration](configuration.md#operating-configurations).

!!! warning "Hardware triggering must be enabled first"
    Hardware triggering is disabled by default. Until it is enabled, trigger pulses on the RX line are ignored and no ping is sent. Enable it with the hardware trigger setting in the web GUI, or with the `hardware_trigger_enabled` parameter over the [TCP JSON API](dvl-a250_a100-json-protocol.md#configuration-over-json) or [serial protocol](dvl-a250_a100-serial-protocol.md#configuration-over-serial). The setting is kept across reboots.

The DVL measures the width of a positive pulse on the RX wire. The wire idles at a negative voltage. A pulse that goes positive and returns to negative after 78.1 µs ± 4.3 µs is recognized as a trigger. The ping is triggered when the pulse ends, that is when the wire returns to the idle negative level.

For a connection configured as 115200 baud, 8N1, this pulse corresponds to transmitting a `"NUL"` ASCII character (`0x00`, Ctrl + @). On the RS232 wire the start bit and the eight zero data bits are all positive, so they keep the wire positive for nine bit times, and the stop bit returns it to the idle level:

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 250" fill="currentColor" font-size="11" style="max-width: 620px;">
  <defs>
    <marker id="trig-arrow" markerWidth="6" markerHeight="6" refX="5" refY="3" orient="auto">
      <path d="M0,0 L6,3 L0,6 Z"/>
    </marker>
    <marker id="trig-arrow-rev" markerWidth="6" markerHeight="6" refX="1" refY="3" orient="auto">
      <path d="M6,0 L0,3 L6,6 Z"/>
    </marker>
  </defs>
  <text x="20" y="22" font-size="12" font-weight="bold">Voltage on the RS232 RX wire of the DVL</text>
  <g stroke="currentColor" stroke-width="0.5" stroke-dasharray="2 3" opacity="0.5">
    <line x1="130" y1="50" x2="130" y2="150"/>
    <line x1="165" y1="50" x2="165" y2="150"/>
    <line x1="200" y1="50" x2="200" y2="150"/>
    <line x1="235" y1="50" x2="235" y2="150"/>
    <line x1="270" y1="50" x2="270" y2="150"/>
    <line x1="305" y1="50" x2="305" y2="150"/>
    <line x1="340" y1="50" x2="340" y2="150"/>
    <line x1="375" y1="50" x2="375" y2="150"/>
    <line x1="410" y1="50" x2="410" y2="150"/>
    <line x1="445" y1="50" x2="445" y2="150"/>
    <line x1="480" y1="50" x2="480" y2="150"/>
  </g>
  <g font-size="9" text-anchor="middle" opacity="0.8">
    <text x="147" y="62">Start</text>
    <text x="182" y="62">D0</text>
    <text x="217" y="62">D1</text>
    <text x="252" y="62">D2</text>
    <text x="287" y="62">D3</text>
    <text x="322" y="62">D4</text>
    <text x="357" y="62">D5</text>
    <text x="392" y="62">D6</text>
    <text x="427" y="62">D7</text>
    <text x="462" y="62">Stop</text>
  </g>
  <line x1="20" y1="110" x2="600" y2="110" stroke="currentColor" stroke-width="0.5" stroke-dasharray="4 3" opacity="0.6"/>
  <text x="602" y="113" font-size="9" opacity="0.8">0 V</text>
  <polyline points="20,140 130,140 130,80 445,80 445,140 600,140" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linejoin="round"/>
  <text x="22" y="156" font-size="10">Idle: negative voltage (-5 to -15 V)</text>
  <text x="140" y="76" font-size="10">Positive voltage (+5 to +15 V)</text>
  <line x1="445" y1="122" x2="500" y2="172" stroke="currentColor" stroke-width="0.8" marker-start="url(#trig-arrow-rev)"/>
  <text x="470" y="186" font-size="10">End of pulse:</text>
  <text x="470" y="198" font-size="10">ping triggered</text>
  <line x1="130" y1="196" x2="445" y2="196" stroke="currentColor" stroke-width="0.8" marker-start="url(#trig-arrow-rev)" marker-end="url(#trig-arrow)"/>
  <line x1="445" y1="145" x2="445" y2="203" stroke="currentColor" stroke-width="0.5"/>
  <line x1="130" y1="160" x2="130" y2="203" stroke="currentColor" stroke-width="0.5"/>
  <text x="288" y="214" text-anchor="middle" font-size="10">Positive for 78.1 µs ± 4.3 µs</text>
  <text x="300" y="227" text-anchor="middle" font-size="9" opacity="0.8">= 9 bit times at 115200 baud: a NUL byte (0x00), 8N1</text>
  <line x1="20" y1="242" x2="600" y2="242" stroke="currentColor" stroke-width="0.6" marker-end="url(#trig-arrow)"/>
  <text x="596" y="238" text-anchor="end" font-size="9">time</text>
</svg>

Because the trigger is defined by its pulse width, sending a `NUL` character at another baud rate does **not** produce a valid trigger. The tolerance of ± 4.3 µs is half a bit time at 115200 baud.

!!! note "Voltage levels are RS232"
    The drawing shows the voltage on the RS232 wire, which is what you see with an oscilloscope. RS232 idles at a negative voltage and a 0 bit is a positive voltage. If you drive the trigger from a UART logic output, you need an RS232 transceiver in between. In logic terms the pulse is a low period of 78.1 µs, and the trigger is the rising edge at the end of it.

The trigger can be sent as often as needed. If the DVL is already transmitting or receiving, incoming trigger signals are discarded.

Hardware triggering works even when the [serial output is disabled](integration.md#serial-output-is-disabled-by-default-on-dvl-a100a250), which is the default on DVL A100/A250. Disabling the serial output stops only the report stream, not the RX line.

!!! warning

    Acoustics must be enabled. Hardware triggering will not work while acoustics are disabled.

## Software triggering

Software triggering is available for all DVL models. It triggers a ping over the TCP JSON API or serial protocol. Acoustics must be disabled for this to work.

Software triggering differs from hardware triggering because it is sent as a request to the DVL and placed in a ping queue. The queue can store up to 15 requests, which are executed one after another until the queue is empty.

See the software ping command in [Commands](configuration.md#commands).

Because this method depends on the internal state of the DVL, the ping queue, and Ethernet jitter if Ethernet is used, the exact ping time is less predictable than with hardware triggering.

!!! warning
    Disable acoustics before using software triggering. This is different from hardware triggering.
