# Diagnostic log

A diagnostic log contains DVL logs and measurements that help Water Linked support investigate issues such as loss of bottom lock, invalid velocity, weak signal, communication problems, or unexpected behavior.

## When to collect a diagnostic log

Collect a diagnostic log when:

* Water Linked support requests it.
* The DVL loses bottom lock unexpectedly.
* Velocity becomes invalid or drops out.
* Measurements are weak or noisy.
* You experience communication or web GUI issues.

## How to collect a diagnostic log

1. Put the DVL in the same environment where the issue occurs.
2. Open the DVL web GUI.
3. Open the diagnostic log or diagnostics page for your DVL model.
4. Follow the instructions in the web GUI to create and download the diagnostic log.
5. Send the diagnostic log to Water Linked support together with relevant installation and test information.

## Demo GUI links

* [DVL A50/A125 diagnostic log demo](https://dvl.demo.waterlinked.com/#/collect)
* [DVL A100/A250 diagnostics demo](https://dvl2.demo.waterlinked.com/#diagnostics)

For more context on the web GUI pages, see [DVL A50/A125 web GUI](dvl-a50_a125-gui.md) and [DVL A100/A250 web GUI](dvl-a250_a100-gui.md).

## What to include when contacting support

Use the [support package checklist](support-package-checklist.md) when preparing a support request.

See [How to diagnose](how-to-diagnose.md) for troubleshooting guidance before contacting support.

!!! note "Transducer numbering and protocol IDs"
    Mechanical/transducer diagrams number the transducers from 1 to 4. In protocol messages and diagnostic logs, the transducer `id` uses zero-based numbering from 0 to 3. The `id` is therefore the transducer number minus 1.
