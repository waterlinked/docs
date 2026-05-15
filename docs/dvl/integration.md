# Integration

This page helps you choose an interface for integrating our DVLs into a vehicle, boat, or control system.

## Choose an interface

| Use case | Recommended interface |
| --- | --- |
| First setup, diagnostics, configuration, and testing | Ethernet and the web GUI |
| Custom software integration over Ethernet | TCP JSON API |
| Direct vehicle integration over serial | Water Linked serial protocol |
| Existing systems with PD0, PD4, or PD6 support | PD formats |
| Multiple acoustic instruments | Triggering and synchronization |

## TCP JSON API { #ethernet-jsontcp }

Use the TCP JSON API when you want a network data stream, command interface, and easy access from custom software. In customer-facing documentation, Water Linked API refers to this TCP JSON API.

The DVL TCP server is available on port `16171`. See [Network Setup](networking.md#tcp-data-stream).

In our measurements, TCP JSON message latency was typically around 4 ms average, with 2 ms standard deviation and an observed maximum of 13 ms. This is not a hard real-time guarantee; actual latency can depend on network setup, host system, load, and integration method.

Protocol references:

* [DVL A50/A125 TCP JSON API](dvl-json-protocol.md)
* [DVL A100/A250 TCP JSON API](dvl-a250_a100-json-protocol.md)

## Serial Water Linked protocol

Use the Water Linked serial protocol when the vehicle controller expects a direct serial data stream.

Electrical interfaces differ by model:

* DVL A50 and DVL A125 use the same UART electrical interface. See [DVL A50/A125 serial interface](electrical.md#dvl-a50-and-dvl-a125-serial-interface).
* DVL A100 and DVL A250 use RS232. See [DVL A100/A250 serial interface](electrical.md#dvl-a100-and-dvl-a250-serial-interface).

Protocol references:

* [DVL A50/A125 serial protocol](dvl-serial-protocol.md)
* [DVL A100/A250 serial protocol](dvl-a250_a100-serial-protocol.md)

## PD formats { #pd0-pd4-and-pd6 }

Use PD formats only when the receiving system already supports PD0, PD4, or PD6. This can reduce integration work when replacing or adding a DVL to an existing system.

PD4 and PD6 are supported over TCP and serial for all DVL models. PD0 is planned for DVL A100 and DVL A250, but is not available yet.

Protocol references:

* [PD formats](dvl-pd-formats.md)
* [PD6 format](dvl-pd-formats.md#pd6-protocol-tcpserial)
* [PD4 format](dvl-pd-formats.md#pd4-protocol-tcpserial)
* [PD0 status](dvl-pd-formats.md#pd0-protocol)

## Triggering and synchronization

Triggering can be useful when the DVL operates near other acoustic instruments and you want to avoid simultaneous acoustic transmissions.

Triggering and synchronization are handled through protocol or electrical interfaces, not through the web GUI.

### TCP JSON API or serial command trigger

The DVL can queue externally requested pings when acoustic pinging is controlled by command.

See:

* [DVL A50/A125 TCP JSON API trigger ping](dvl-json-protocol.md#trigger-ping)
* [DVL A50/A125 serial trigger ping](dvl-serial-protocol.md#trigger-ping-wcx)
* [DVL A100/A250 TCP JSON API trigger ping](dvl-a250_a100-json-protocol.md#trigger-ping)
* [DVL A100/A250 serial trigger ping](dvl-a250_a100-serial-protocol.md#trigger-ping-wcx)

### RX-line trigger

For DVL A100 and DVL A250, sending a NULL character over the RS232 RX line triggers a pulse on the falling edge.

<!-- TODO: Engineering review: confirm timing requirements and valid baud/configuration assumptions for A100/A250 RX-line triggering. -->

## Diagnostics during integration

If the integration does not behave as expected, collect a diagnostic log from the web GUI and include the integration interface in the support request.

See:

* [DVL diagnostic log](diagnostic-log.md)
* [How to diagnose](how-to-diagnose.md)
