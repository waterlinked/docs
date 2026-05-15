# Software resources

This page lists Water Linked software resources that may be useful when integrating DVL products.

## GitHub organization

Water Linked publishes software examples, tools, and integration resources on GitHub:

https://github.com/waterlinked

The repositories below were identified from the Water Linked GitHub organization and checked against repository descriptions or README files on 2026-05-07. Repository availability, names, and APIs may change over time. Check each repository README before using it in an integration.

## DVL software repositories

| Repository | Description | Typical use | Maintained |
| --- | --- | --- | --- |
| [waterlinked_dvl](https://github.com/waterlinked/waterlinked_dvl) | C++ library and ROS 2 driver for Water Linked DVL devices, including DVL A50 and DVL A125. | ROS 2 integration, C++ integration, and starting from the included library examples. | Yes |
| [dvl-python](https://github.com/waterlinked/dvl-python) | Example code for working with the Water Linked DVL serial protocol and TCP JSON API. | Legacy Python examples for reading DVL protocol data over serial or TCP. Use together with the current protocol documentation. | No |
| [dvl-a50-ros-driver](https://github.com/waterlinked/dvl-a50-ros-driver) | Archived ROS 1 package for the Water Linked DVL A50. | Legacy ROS 1 integrations that still depend on the original DVL A50 driver. | No |

## Examples and integration helpers

Use these repositories as starting points when you need code-level integration examples:

* [waterlinked_dvl](https://github.com/waterlinked/waterlinked_dvl) for ROS 2 and C++ projects using DVL A50 or DVL A125.
* [dvl-python](https://github.com/waterlinked/dvl-python) for legacy Python examples using the DVL serial protocol and TCP JSON API.
* [dvl-a50-ros-driver](https://github.com/waterlinked/dvl-a50-ros-driver) for legacy ROS 1 projects using DVL A50.

Where a repository README states model support, use that scope as the source of truth. For other DVL models or custom integrations, use the protocol documentation and the integration guide linked below.


## Related resources

* [DVL integration guide](integration.md)
* [DVL A50/A125 TCP JSON API](dvl-json-protocol.md)
* [DVL A100/A250 TCP JSON API](dvl-a250_a100-json-protocol.md)
* [DVL A50/A125 serial protocol](dvl-serial-protocol.md)
* [DVL A100/A250 serial protocol](dvl-a250_a100-serial-protocol.md)
* [PD formats](dvl-pd-formats.md)
* [PD integration overview](integration.md#pd0-pd4-and-pd6)
* [Electrical connection](electrical.md)
* [Network setup](networking.md)
* [DVL diagnostic log](diagnostic-log.md)
* [How to diagnose](how-to-diagnose.md)

## Notes

Software repositories are provided as integration aids. They may not cover every DVL model, software version, or customer platform. For production integrations, verify behavior against the current DVL protocol documentation and the README in the repository you plan to use.
