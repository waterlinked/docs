# Electrical connection

This page covers electrical connection, LED signals, wiring, shielding, and serial interface for all DVLs.

Most wiring is common across the DVL models. The serial electrical interface differs:

* DVL A50 and DVL A125 use 3.3 V UART, 5 V tolerant.
* DVL A100 and DVL A250 use RS232.

## LED signals

| Visualization | LED signal | Description |
| :---: | :--- | :--- |
| ⚫ | **No green light** | Power is off. |
| 🟢 | **Fixed green light** | The DVL is powering on. Depending on configuration it can take ~30-60 seconds to power on. |
| 🟢⚫⚫⚫ | **Flashing green light** (mostly off, slow) | DVL looking for bottom lock. |
| 🟢🟢🟢⚫ | **Flashing green light** (mostly on, slow) | DVL has bottom lock. |
| 🟢⚫🟢⚫ | **Flashing green light** (fast) | DVL is in [thermal shutdown](how-to-diagnose.md#thermal-shutdown). |

## Wiring interface

Power and Ethernet wiring are common. The brown and brown/white serial pair depends on the DVL model.

### Common power and Ethernet wires

| Interface | Color | Visual |
| :--- | :--- | :---: |
| Negative/Ground | Black | ⬛ |
| Positive (10–30 Vdc) | Red | 🟥 |
| ETH RX+ | Green/White | 🟩⬜ |
| ETH RX- | Green | 🟩 |
| ETH TX- | Orange | 🟧 |
| ETH TX+ | Orange/White | 🟧⬜ |
| Shielded wire | Naked/silver | ⚪ |

### Model-specific serial wires

| Model | Interface | Color | Visual |
| :--- | :--- | :--- | :---: |
| DVL A50/A125 | UART TX | Brown/White | 🟫⬜ |
| DVL A50/A125 | UART RX | Brown | 🟫 |
| DVL A100/A250 | Serial (RS232) TX | Brown/White | 🟫⬜ |
| DVL A100/A250 | Serial (RS232) RX | Brown | 🟫 |

!!! note
    Power must be applied to the power terminals before applying voltage to the serial pins.

## Seacon connector option

The Seacon connector option is available for:

* DVL A50.
* DVL A100 side-entry versions only.
* DVL A250 side-entry versions only.

<!-- TODO: Confirm whether a Seacon connector option is available for DVL A100. -->

### DVL A50/A100/A250 Seacon MCOM8M connector

The table below shows the pinout for the DVL A50/A100/A250 Seacon MCOM8M connector.

| Interface | Pin | Color | Visual |
| :--- | :--- | :--- | :---: |
| Negative/Ground | 1 | Black | ⬛ |
| Positive (10–30 Vdc) | 2 | Red | 🟥 |
| ETH RX+ | 3 | Green/White | 🟩⬜ |
| ETH RX- | 4 | Green | 🟩 |
| ETH TX- | 5 | Orange | 🟧 |
| ETH TX+ | 6 | Orange/White | 🟧⬜ |
| UART TX | 7 | Brown/White | 🟫⬜ |
| UART RX | 8 | Brown | 🟫 |

<!-- TODO: Confirm and publish the DVL A250 side-entry Seacon connector pinout before reusing the A50/A125 table for A250. -->

## Power specifications

| Specification | DVL A50 | DVL A100 | DVL A125 | DVL A250 |
| :--- | :--- | :--- |:--- |:--- |
| Input voltage | 10–30 Vdc | 10–30 Vdc | 10–30 Vdc | 10–30 Vdc |
| Power consumption, average | 4 W | 8 W | 4 W | 8 W |
| Power-on current surge | 35 W | 30 W | 35 W | 30 W |

<!-- TODO: Add or link DVL A50/A125 electrical specifications if they should be published here. -->

## Shielded cable information

Shielded DVL cable helps protect the communication and power lines from external electromagnetic interference (EMI) and radio frequency interference (RFI). The DVL electronics are not internally connected to the shield; it is up to the user to decide whether and how to connect the shield.

!!! note
    For DVL A50, shielded cables were introduced autumn 2024.

    All DVLs with Seacon MCOM8M connector are delivered with unshielded cable that can be grounded.

    All DVL A125 units are delivered with shielded cable.

<!-- TODO: Confirm whether all DVL A250 cable and connector variants use the same shield arrangement. -->

For DVL A100, the side cable entry version has a 3 m shielded cable, and the rear O-ring interface version has a 1 m shielded cable.

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
| Interface | 3.3 V UART, 5 V tolerant |
| Baud rate | 115200 |
| Data/parity/stop | 8N1 |
| Flow control | None |

!!! warning
    There can be a momentary (<10 us) power spike (~5 V) on the UART lines when power is applied to the DVL, which may damage equipment that is not 5 V tolerant.

See the [DVL A50/A125 serial protocol](dvl-serial-protocol.md#serial-protocol).

### DVL A100 and DVL A250 serial interface { #dvl-a100-and-dvl-a250-serial-interface }

DVL A100 and DVL A250 use a standard RS232 serial interface.

| Setting | Value |
| :--- | :--- |
| Interface | RS232 |
| Baud rate | 115200 |
| Data/parity/stop | 8N1 |
| Flow control | None |

See the [DVL A100/A250 serial protocol](dvl-a250_a100-serial-protocol.md#serial-protocol).
