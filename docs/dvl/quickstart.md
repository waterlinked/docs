# Quickstart guide

This guide helps you connect and access the GUI for all DVLs.

## 1. Unbox and inspect

Check that the DVL, cable, and any interface hardware are undamaged.

## 2. Keep the DVL in water

The DVL should be submerged before it is powered. This prevents overheating and is required for valid velocity measurements.

!!! tip
    Keep the DVL in a bucket of water when using it on a workbench.

## 3. Mount the DVL

Secure the DVL to your vehicle using the mounting holes and make sure the transducers have a clear line of sight to the bottom.

See [Installation](installation.md) for common guidance on orientation, line of sight, vibration, bubbles, turbulence, and boat-mounted use cases.

| Model | Mounting and dimensions |
| :--- | :--- |
| DVL A50 | [DVL A50](dvl-a50.md) |
| DVL A100 | [DVL A100](dvl-a100.md#dimensions) |
| DVL A125 | [DVL A125](dvl-a125.md) |
| DVL A250 | [DVL A250](dvl-a250.md#dimensions) |

## 4. Connect power and Ethernet

Wire the DVL according to the correct electrical interface for your model, then connect Ethernet to your computer or network. Ethernet is the recommended interface for first setup because it gives access to the web GUI, diagnostics, configuration, software updates, and the TCP data stream.

Serial is available for vehicle integrations where a direct serial data stream is required.

| Model | Electrical interface | Recommended interface | Optional serial interface |
| :--- | :--- | :--- | :--- |
| DVL A50 | [Electrical connection](electrical.md) | Ethernet | UART TTL |
| DVL A100 | [Electrical connection](electrical.md) | Ethernet | RS232 |
| DVL A125 | [Electrical connection](electrical.md) | Ethernet | UART TTL |
| DVL A250 | [Electrical connection](electrical.md) | Ethernet | RS232 |

## 5. Configure network

Configure your computer to reach the DVL over Ethernet. See [Network Setup](networking.md) for mDNS, fallback IP, static IP, and TCP information.

## 6. Access the web GUI

Open the DVL web GUI in a web browser.

| Model | Web GUI documentation |
| :--- | :--- |
| DVL A50/A125 | [web GUI](dvl-a50_a125-gui.md) |
| DVL A100/A250 | [web GUI](dvl-a250_a100-gui.md) |

## 7. Need help?

Check out [How to diagnose](how-to-diagnose.md) and [FAQ](faq.md).
