# Electrical connection

This page covers electrical connection, LED signals, wiring, shielding, and serial interface for all DVLs.

!!! tip "First-time setup"
    New to the DVL? The [Quickstart](quickstart.md) covers the full setup path (mount, wire, connect, open the web GUI). This page is the detailed wiring reference; to get on the network afterwards, see [Network setup](networking.md).

Most wiring is common across the DVL models. The serial electrical interface differs:

* DVL A50 and DVL A125 use 3.3 V UART, 5 V tolerant.
* DVL A100 and DVL A250 use RS232.

## LED signals

| Visualization | LED signal | Description |
| :---: | :--- | :--- |
| <span class="swatch swatch-round c-ledoff"></span> | **No green light** | Power is off. |
| <span class="swatch swatch-round c-ledon"></span> | **Fixed green light** | The DVL is powering on. Depending on configuration it can take ~30-60 seconds to power on. |
| <span class="swatch swatch-round c-ledon"></span> <span class="swatch swatch-round c-ledoff"></span> <span class="swatch swatch-round c-ledoff"></span> <span class="swatch swatch-round c-ledoff"></span> | **Flashing green light** (mostly off, slow) | DVL looking for bottom lock. |
| <span class="swatch swatch-round c-ledon"></span> <span class="swatch swatch-round c-ledon"></span> <span class="swatch swatch-round c-ledon"></span> <span class="swatch swatch-round c-ledoff"></span> | **Flashing green light** (mostly on, slow) | DVL has bottom lock. |
| <span class="swatch swatch-round c-ledon"></span> <span class="swatch swatch-round c-ledoff"></span> <span class="swatch swatch-round c-ledon"></span> <span class="swatch swatch-round c-ledoff"></span> | **Flashing green light** (fast) | DVL is in [thermal shutdown](how-to-diagnose.md#thermal-shutdown). |

## Wiring interface

All DVL models use the same wire colors. The serial TX and RX wires carry a different electrical interface depending on the model. The last column gives the pin number on the Seacon MC8M connector, for the models where that option is available.

<a id="common-power-and-ethernet-wires"></a><a id="model-specific-serial-wires"></a>

| Interface | Color | Visual | Seacon MC8M pin |
| :--- | :--- | :---: | :---: |
| Negative/Ground | Black | <span class="swatch c-black"></span> | 1 |
| Positive (10–30 Vdc) | Red | <span class="swatch c-red"></span> | 2 |
| ETH RX+ | Green/White | <span class="swatch c-green-white"></span> | 3 |
| ETH RX- | Green | <span class="swatch c-green"></span> | 4 |
| ETH TX- | Orange | <span class="swatch c-orange"></span> | 5 |
| ETH TX+ | Orange/White | <span class="swatch c-orange-white"></span> | 6 |
| Serial TX | Brown/White | <span class="swatch c-brown-white"></span> | 7 |
| Serial RX | Brown | <span class="swatch c-brown"></span> | 8 |
| Shielded wire | Naked/silver | <span class="swatch c-silver"></span> | Not connected |

!!! note "Serial interface type"
    * **DVL A50/A125:** the serial wires are a 3.3 V UART, 5 V tolerant.
    * **DVL A100/A250:** the serial wires are RS232.

    The wire colors and pin numbers are the same for both. See [Terminal / serial interface](#terminal-serial-interface) for the settings of each.

!!! note "Power and serial start-up order"
    Connect ground first. The serial ground and the supply ground must be connected before any signal is applied to the serial pins.

    How the serial pins handle being driven before the DVL is powered depends on the model:

    * **DVL A50/A125:** applying power before driving the serial pins is a conservative recommendation. The UART inputs are protected and tolerate being driven before the DVL is powered, so a delay of a few milliseconds before power comes on is not a problem. What damages the UART is a DC voltage above 5 V on TX or RX. Keep the lines at 3.3 V, with 5 V as the absolute maximum.
    * **DVL A100/A250:** the RS232 inputs tolerate being driven while the DVL is unpowered. No particular start-up order is needed.

## Seacon connector option

The Seacon connector option is available for:

* DVL A50.
* DVL A100 side-entry versions only.
* DVL A250 side-entry versions only.

<a id="dvl-a50a100a250-seacon-mc8m-connector"></a>

The pin numbers of the Seacon MC8M connector are in the last column of the [wiring table](#wiring-interface). The serial pins 7 and 8 follow the serial interface type of the model: UART on the DVL A50, RS232 on the DVL A100 and DVL A250.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 345" fill="currentColor" font-size="12" style="max-width: 640px;" role="img" aria-label="Seacon MC8M connector, face view of the male pins on the DVL cable, with pin numbers and signals">
  <text x="20" y="26" font-size="14" font-weight="bold">MC8M connector, face view of the male pins on the DVL cable</text>
  <text x="20" y="44" font-size="11" opacity="0.75">Pin fill shows the wire color. The mating female connector shows the same positions mirrored.</text>
  <circle cx="230" cy="190" r="112" fill="currentColor" fill-opacity="0.10" stroke="currentColor" stroke-width="2"/>
  <circle cx="230" cy="190" r="102" fill="none" stroke="currentColor" stroke-width="0.8" opacity="0.6"/>
  <circle cx="230.0" cy="176.0" r="15" fill="#1a1a1a" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="230.0" cy="176.0" r="7.5" fill="#ffffff" stroke="#1a1a1a" stroke-width="0.8"/>
  <text x="230.0" y="180.0" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a1a">1</text>
  <circle cx="285.2" cy="134.8" r="15" fill="#d32f2f" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="285.2" cy="134.8" r="7.5" fill="#ffffff" stroke="#1a1a1a" stroke-width="0.8"/>
  <text x="285.2" y="138.8" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a1a">2</text>
  <circle cx="308.0" cy="190.0" r="15" fill="#ffffff" stroke="currentColor" stroke-width="1.6"/>
  <rect x="293.8" y="187.0" width="28.5" height="6" fill="#2e7d32"/>
  <circle cx="308.0" cy="190.0" r="15" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="308.0" cy="190.0" r="7.5" fill="#ffffff" stroke="#1a1a1a" stroke-width="0.8"/>
  <text x="308.0" y="194.0" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a1a">3</text>
  <circle cx="285.2" cy="245.2" r="15" fill="#2e7d32" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="285.2" cy="245.2" r="7.5" fill="#ffffff" stroke="#1a1a1a" stroke-width="0.8"/>
  <text x="285.2" y="249.2" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a1a">4</text>
  <circle cx="230.0" cy="268.0" r="15" fill="#ef6c00" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="230.0" cy="268.0" r="7.5" fill="#ffffff" stroke="#1a1a1a" stroke-width="0.8"/>
  <text x="230.0" y="272.0" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a1a">5</text>
  <circle cx="174.8" cy="245.2" r="15" fill="#ffffff" stroke="currentColor" stroke-width="1.6"/>
  <rect x="160.6" y="242.2" width="28.5" height="6" fill="#ef6c00"/>
  <circle cx="174.8" cy="245.2" r="15" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="174.8" cy="245.2" r="7.5" fill="#ffffff" stroke="#1a1a1a" stroke-width="0.8"/>
  <text x="174.8" y="249.2" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a1a">6</text>
  <circle cx="152.0" cy="190.0" r="15" fill="#ffffff" stroke="currentColor" stroke-width="1.6"/>
  <rect x="137.8" y="187.0" width="28.5" height="6" fill="#5d4037"/>
  <circle cx="152.0" cy="190.0" r="15" fill="none" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="152.0" cy="190.0" r="7.5" fill="#ffffff" stroke="#1a1a1a" stroke-width="0.8"/>
  <text x="152.0" y="194.0" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a1a">7</text>
  <circle cx="174.8" cy="134.8" r="15" fill="#5d4037" stroke="currentColor" stroke-width="1.6"/>
  <circle cx="174.8" cy="134.8" r="7.5" fill="#ffffff" stroke="#1a1a1a" stroke-width="0.8"/>
  <text x="174.8" y="138.8" text-anchor="middle" font-size="10" font-weight="bold" fill="#1a1a1a">8</text>
  <rect x="400" y="94" width="18" height="12" rx="2" fill="#1a1a1a" stroke="currentColor" stroke-width="0.8"/>
  <text x="428" y="104" font-weight="bold">1</text>
  <text x="446" y="104">Negative/Ground</text>
  <rect x="400" y="124" width="18" height="12" rx="2" fill="#d32f2f" stroke="currentColor" stroke-width="0.8"/>
  <text x="428" y="134" font-weight="bold">2</text>
  <text x="446" y="134">Positive (10–30 Vdc)</text>
  <rect x="400" y="154" width="18" height="12" rx="2" fill="#ffffff" stroke="currentColor" stroke-width="0.8"/>
  <rect x="401" y="158" width="16" height="4" fill="#2e7d32"/>
  <text x="428" y="164" font-weight="bold">3</text>
  <text x="446" y="164">ETH RX+</text>
  <rect x="400" y="184" width="18" height="12" rx="2" fill="#2e7d32" stroke="currentColor" stroke-width="0.8"/>
  <text x="428" y="194" font-weight="bold">4</text>
  <text x="446" y="194">ETH RX-</text>
  <rect x="400" y="214" width="18" height="12" rx="2" fill="#ef6c00" stroke="currentColor" stroke-width="0.8"/>
  <text x="428" y="224" font-weight="bold">5</text>
  <text x="446" y="224">ETH TX-</text>
  <rect x="400" y="244" width="18" height="12" rx="2" fill="#ffffff" stroke="currentColor" stroke-width="0.8"/>
  <rect x="401" y="248" width="16" height="4" fill="#ef6c00"/>
  <text x="428" y="254" font-weight="bold">6</text>
  <text x="446" y="254">ETH TX+</text>
  <rect x="400" y="274" width="18" height="12" rx="2" fill="#ffffff" stroke="currentColor" stroke-width="0.8"/>
  <rect x="401" y="278" width="16" height="4" fill="#5d4037"/>
  <text x="428" y="284" font-weight="bold">7</text>
  <text x="446" y="284">Serial TX</text>
  <rect x="400" y="304" width="18" height="12" rx="2" fill="#5d4037" stroke="currentColor" stroke-width="0.8"/>
  <text x="428" y="314" font-weight="bold">8</text>
  <text x="446" y="314">Serial RX</text>
  <text x="230" y="324" text-anchor="middle" font-size="11" opacity="0.8">The cable shield is not connected to the connector.</text>
</svg>

## Power specifications

| Specification | DVL A50 | DVL A100 | DVL A125 | DVL A250 |
| :--- | :--- | :--- |:--- |:--- |
| Input voltage | 10–30 Vdc | 10–30 Vdc | 10–30 Vdc | 10–30 Vdc |
| Power consumption, average | 4 W | 8 W | 4 W | 8 W |
| Power-on current surge | 35 W | 30 W | 35 W | 30 W |

## Shielded cable information

Shielded DVL cable helps protect the communication and power lines from external electromagnetic interference (EMI) and radio frequency interference (RFI). The DVL electronics are not internally connected to the shield; it is up to the user to decide whether and how to connect the shield.

!!! note
    For DVL A50, shielded cables were introduced autumn 2024.

    All DVL A125 units are delivered with shielded cable.

### Connecting the shield

For optimal performance, especially when mounted on an ROV (Remotely Operated Vehicle) or AUV (Autonomous Underwater Vehicle), connect the shield to reduce the impact of interference on communication and power signals. The most common connection methods are:

1. **Chassis ground**: Connect the shield to the chassis of the ROV/AUV. This gives the shield a path to ground for noise and interference, and the vehicle chassis often acts as a common grounding reference.
2. **Common ground**: Connect the shield to the common electrical ground of the ROV/AUV. This may be used when the electrical and signal systems are designed to share a common ground.

### Recommendation

We recommend connecting the shield to the **chassis ground** of the ROV or AUV if possible. If your system design uses a common electrical ground, that option can also be considered.

Ground the shield at one end only to avoid ground loops, unless your system design requires grounding at both ends.

## Terminal / serial interface

### DVL A50 and DVL A125 serial interface { #dvl-a50-and-dvl-a125-serial-interface }

DVL A50 and DVL A125 use the same 3.3 V UART interface, 5 V tolerant.

| Setting | Value |
| :--- | :--- |
| Interface | 3.3 V UART, 5 V tolerant (5 V absolute maximum) |
| Baud rate | 115200 |
| Data/parity/stop | 8N1 |
| Flow control | None |

!!! warning
    There can be a momentary (<10 us) power spike (~5 V) on the UART lines when power is applied to the DVL, which may damage equipment that is not 5 V tolerant.

The serial output is enabled by default. See the [DVL A50/A125 serial protocol](dvl-serial-protocol.md#serial-protocol).

### DVL A100 and DVL A250 serial interface { #dvl-a100-and-dvl-a250-serial-interface }

DVL A100 and DVL A250 use a standard RS232 serial interface.

| Setting | Value |
| :--- | :--- |
| Interface | RS232 |
| Baud rate | 115200 |
| Data/parity/stop | 8N1 |
| Flow control | None |

!!! note "Serial output is disabled by default"
    DVL A100 and DVL A250 do not send reports over RS232 until the serial output is enabled in the web GUI or with the `wcp` command over serial. Serial commands and hardware triggering work regardless. See [Serial output is disabled by default on DVL A100/A250](integration.md#serial-output-is-disabled-by-default-on-dvl-a100a250).

See the [DVL A100/A250 serial protocol](dvl-a250_a100-serial-protocol.md#serial-protocol).
