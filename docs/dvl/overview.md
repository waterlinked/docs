# Overview
At Water Linked we pride ourselves on building the Worlds smallest DVLs in their respective categories. Our DVLs combine everything that is important in the smallest possible formfactor: Prize and Performance!

## What is a DVL?
A DVL estimates velocity relative to the seafloor by sending acoustic waves from four angled transducers and measuring the frequency shift (Doppler effect) of the returned echoes. By combining measurements from all four transducers over time, the DVL can accurately estimate both the speed and direction of movement.

![dvl_a50](../img/WL-21035-3_DVL-A50_Side4_1600_crop.jpg)

## DVL comparison

Here is a quick overview of the differences between the DVL models:

| Feature | DVL A50 | DVL A100* | DVL A125 | DVL A250 |
| :--- | :--- | :--- | :--- | :--- |
| **Altitude range**** | 5 cm to 50 m |5 cm to 100 m | 5 cm to 125 m| 30 cm to 250 m |
| **Maximum velocity** | 3.75 m/s | 5 m/s | 9 m/s | 15 m/s |
| **Frequency** | 1 MHz | 625 kHz | 420 kHz | 250 kHz |
| **Water tracking** | Yes | Planned | Yes | Planned |
| **Diameter / height** | 66 mm / 25 mm | 90 mm / 34 mm | 125 mm / 30 mm | 149 mm / 40 mm |
| **Weight in air / water** | 170 g / 105 g | 200 g / 125 g | 750 g / 500 g | 1650 g / 750 g |
| **Power consumption** | 4 W (average) | 8 W (average) | 4 W (average) | 8 W (average) |
| **Serial protocol** | UART TTL (3.3 V, 5 V tolerant) | RS232 | UART TTL (3.3 V, 5 V tolerant) | RS232 |
| **IMU output** | No | Planned | No | Planned |
| **Ping triggering** | Software | Soft- and Hardware | Software | Soft- and Hardware |
| **Cable entry** | Side entry | Side entry or rear O-ring interface | Side entry | Side entry or rear O-ring interface |
| **Communication** | Ethernet and UART TTL | Ethernet and serial RS232 | Ethernet and UART TTL | Ethernet and serial RS232 |
| **Source level (dB re 1 μPa @ 1 m)** | 200 |  | 209 |  |
| **Depth rating** | 300 m or 600 m| 1000 m | 1000 m or 4000 m| 4000 m for side-entry cable configuration; rear O-ring interface version rated to 1000 m |
| **Main use case** | Compact platforms where size and payload capacity are limited and operations are conducted close to the bottom | Compact platforms where size and payload capacity are limited but require more range than the A50 | Long-range and deep-water subsea operations in high-pressure environments | Long-range and deep-water subsea operations where large operating altitudes are required |

*Coming Q4 2026

**Under ideal conditions
<!-- TODO: Confirm DVL A100 and DVL A250 source level/SPL before publishing source level/SPL in this comparison table. Keep SPL values in this overview only; FAQ should link here instead of repeating values. -->

<!-- ## DVL A50 and DVL A125 comparison

The DVL A50 and DVL A125 share the same general web GUI, configuration, electrical, and integration documentation. The main differences are operating range, frequency, velocity limit, depth rating, and physical size.

## DVL A100 and DVL A250 comparison

The DVL A100 and DVL A250 share the same general web GUI, configuration, electrical, and integration documentation. The main differences are operating range, frequency, velocity limit, depth rating, and physical size.

| Feature | DVL A100 | DVL A250 |
| :--- | :--- | :--- |
| **Altitude range** | 5 cm to 100 m | 30 cm to 250 m |
| **Maximum velocity** | 5 m/s | 15 m/s |
| **Frequency** | 625 kHz | 250 kHz |
| **Depth rating** | 1,000 m | 4,000 m for side-entry cable configuration; rear O-ring interface version rated to 1,000 m |
| **Diameter / height** | 90 mm / 34 mm | 149 mm / 40 mm |
| **Weight in air / water** | 0.2 kg / 0.125 kg | 1.65 kg / 0.75 kg |
| **Communication** | Ethernet and serial RS232 | Ethernet and serial RS232 |
| **Protocols** | TCP JSON API, serial protocol, PD4, PD6. PD0 planned. | TCP JSON API, serial protocol, PD4, PD6. PD0 planned. |
| **Main use case** | Compact platforms where size and payload capacity are limited | Long-range and deep-water subsea operations where large altitudes are required | -->

<!-- TODO: Update the comparison when PD0 becomes available for DVL A100/A250. -->




## A50

* [DVL A50 Documentation & Installation](dvl-a50.md)

The [DVL A50](dvl-a50.md) is one of the world's smallest commercially available Doppler Velocity Logs.

The A50 established a new market standard with its high performance, ultra-small 4-beam setup, open interface protocol, and low cost.

## A100

* [DVL A100 Documentation & Installation](dvl-a100.md)

The [DVL A100](dvl-a100.md) is a compact, high-accuracy Doppler Velocity Log for lightweight and integration-friendly platforms.

The A100 supports close-range and mid-range operation up to 100 m altitude and shares web GUI, configuration, electrical, protocol, and integration documentation with the DVL A250 where behavior is identical.

## A125

* [DVL A125 Documentation & Installation](dvl-a125.md)

The [DVL A125](dvl-a125.md) is the next step up from the [DVL A50](dvl-a50.md), providing better performance at greater distances while still keeping a small form factor relative to competing DVLs.

The DVL A125 builds on the DVL A50 with increased performance, a small 4-beam setup, an open interface protocol, and mid-to-low cost.

## A250

* [DVL A250 Documentation & Installation](dvl-a250.md)

The [DVL A250](dvl-a250.md) is the most capable DVL in the lineup, delivering long-range performance while maintaining a compact and efficient design.

Operating at lower frequency for extended reach, the A250 enables reliable velocity measurements at distances up to 250 m, making it suitable for demanding subsea operations.

The DVL A250 combines high performance, a compact 4-beam setup, open interface protocol, and a competitive cost, making it a powerful solution for larger vehicles and deep-water applications.
