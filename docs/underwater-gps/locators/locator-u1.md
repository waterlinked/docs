# Locator-U1

[Buy Locator-U1 here!](https://waterlinked.com/product/locator-u1/)

## Description

The Locator-U1 is a battery-powered, digital hydroacoustic locator device. It includes an internal GPS-based time-sync module, eliminating the need for a tether. This makes it ideal for divers, ROVs lacking convenient power sources, or other underwater applications.

Before deployment, the Locator-U1 must obtain a GPS lock. The integrated status LED indicates the GPS lock status and, on units with SN: 0556 and higher, the charging status. Once locked, the Locator-U1 can operate for around 6 hours before it needs to resync with GPS.

A rotary switch is located inside the cap, allowing you to select the channel on which the Locator transmits. The same channel must be set in the Water Linked Underwater GPS GUI. Each side of the Locator has three M3 mounting holes, and a standard bracket is included.

!!! Note
    You will need GPS lock on the topside as well when using the U1. This is for timing purposes, it will not help to use only external GPS position as this can not be used for time synchronization. It is not enough to only have GPS lock on the U1.

## Before each dive

Use this checklist to get the Locator-U1 ready. Each step links to the detailed description further down the page.

| Step | What to do | LED |
|:----:|------------|:---:|
| 1 | [Charge](#charging) the Locator-U1 for at least 7 hours with a 5 V / 2 A wall adapter, within 24 hours before use. On SN: 0556 and higher, the LED breathes while charging and turns solid when fully charged. | <span class="led led--breathe" role="img" aria-label="LED breathing green"></span> → <span class="led led--on" role="img" aria-label="LED solid green"></span><br><small>SN: 0556 and higher</small> |
| 2 | Unplug the charger. With the cap off, set the [channel](#channel-selection) on the rotary switch to the same channel as in the GUI. | <span class="led led--off" role="img" aria-label="LED off"></span> |
| 3 | Check that the O-ring in the cap is clean and undamaged, then [screw the cap on](#powering-on-and-off) to power on. The Locator-U1 searches for GPS lock. | <span class="led led--blink" role="img" aria-label="LED flashing once per second"></span> |
| 4 | Keep the Locator-U1 in open sky until the LED turns solid green. It now has GPS lock and is ready to dive. | <span class="led led--on" role="img" aria-label="LED solid green"></span> |
| 5 | Make sure the topside also has GPS lock, then deploy. Recover the Locator-U1 within about [6 hours](#operating-time). | |

## Charging

The Locator-U1 has an internal rechargeable battery. Use the included USB-C cable and a 5 V / 2 A (or higher) wall adapter to charge it. Always fully charge the Locator-U1 before each operation.

!!! warning
    Do not use your computer to charge the locator. A computer USB port does not supply enough power to charge the Locator-U1.

1) **Remove the cap**  
   Unscrew the cap completely to access the USB-C charging port.

2) **Insert the USB-C cable**  
   Plug one end of the cable into the Locator-U1’s charging port.

3) **Connect to a suitable power source**  
   Attach the other end of the cable to a wall adapter providing at least 5 V / 2 A.

4) **Charge for 7 hours**  
   Leave the Locator-U1 connected for a full 7 hours to ensure a complete charge. You can then disconnect the cable and use the Locator-U1. Charging overnight the night before use is a recommended routine.

### LED Behavior While Charging

The LED behavior while charging depends on the serial number (SN) of your Locator-U1. Select the tab that matches your unit.

=== "SN: 0556 and higher"

    When connected to a charger, the Locator-U1 only charges. It does **not** power on, and the LED shows the charging status:

    | LED | Signal | Meaning |
    |:---:|--------|---------|
    | <span class="led led--breathe" role="img" aria-label="LED breathing green"></span> <span class="led-wave led-wave--breathe" aria-hidden="true"></span> | **Breathing green light** (slowly fading in and out) | The Locator-U1 is charging. |
    | <span class="led led--on" role="img" aria-label="LED solid green"></span> <span class="led-wave led-wave--on" aria-hidden="true"></span> | **Solid green light** | The Locator-U1 is fully charged. |

    When the Locator-U1 is powered on normally by screwing on the cap, the LED behaves as described in [LED Signals](#led-signals).

=== "SN: 0555 and lower"

    When connected to a charger, the Locator-U1 powers on and charges at the same time. The LED does **not** indicate charging progress:

    | LED | Signal | Meaning |
    |:---:|--------|---------|
    | <span class="led led--blink" role="img" aria-label="LED flashing green"></span> <span class="led-wave led-wave--blink" aria-hidden="true"></span> | **Flashing green light** | The Locator-U1 is powered on and working normally, for example searching for GPS lock. This does **not** reflect charging status. |
    | <span class="led led--off" role="img" aria-label="LED off"></span> <span class="led-wave led-wave--off" aria-hidden="true"></span> | **No light** | The battery is too low to power on, but the Locator-U1 is still charging. Once it has enough power, the LED starts flashing. |
    | <span class="led led--on" role="img" aria-label="LED solid green"></span> <span class="led-wave led-wave--on" aria-hidden="true"></span> | **Solid green light** | The Locator-U1 is powered on and has GPS lock. This does **not** mean it is fully charged. Keep charging for the full 7 hours. |

## Powering On and Off

- **To power on** the Locator-U1, securely tighten the cap over the charging port. The LED will begin flashing to indicate that it is searching for a GPS lock. Once the LED stops flashing and becomes solid, the Locator-U1 has acquired a GPS lock and is ready for use.  
  Ensure the O-ring in the cap is undamaged before submerging the device.

- **To power off** the Locator-U1, unscrew the cap until the LED turns off.

## LED Signals

These signals apply when the Locator-U1 is powered on by screwing on the cap. For the LED while connected to a charger, see [LED Behavior While Charging](#led-behavior-while-charging).

| LED | Signal | Meaning | Ready to dive? |
|:---:|--------|---------|:--------------:|
| <span class="led led--off" role="img" aria-label="LED off"></span> <span class="led-wave led-wave--off" aria-hidden="true"></span> | **No light** | Power is off. | No |
| <span class="led led--blink" role="img" aria-label="LED flashing once per second"></span> <span class="led-wave led-wave--blink" aria-hidden="true"></span> | **Flashing green light** (once per second) | Searching for GPS lock. | No |
| <span class="led led--on" role="img" aria-label="LED solid green"></span> <span class="led-wave led-wave--on" aria-hidden="true"></span> | **Solid green light** | GPS lock acquired. | **Yes** |
| <span class="led led--blink-slow" role="img" aria-label="LED flashing slowly"></span> <span class="led-wave led-wave--blink-slow" aria-hidden="true"></span> | **Flashing green light** (slow) | GPS lock was acquired but has since been lost. | **Yes** |
| <span class="led led--blink-fast" role="img" aria-label="LED flashing fast"></span> <span class="led-wave led-wave--blink-fast" aria-hidden="true"></span> | **Fast flashing green light** (multiple times per second) | Error. See [Error indication](#error-indication). | No |

!!! Note
    The animations above illustrate the LED patterns. The exact timing on the Locator-U1 may differ slightly.

### Error indication

A fast flashing LED often means one of the following:

- The Locator-U1 has exceeded its dive time and the pressure sensor needs to dry. Charging the Locator-U1 helps the sensor dry more quickly.
- The battery is very low. [Charge](#charging) the Locator-U1.

## Channel selection

The channel is selected with the rotary switch inside the cap. Unscrew the cap completely to access the switch. The channel on the Locator-U1 must match the channel selected in the [GUI settings](../interface/ugps-gui.md#settings). Channel 3 is usually a good choice. See the [channel overview](../ugps-sysconfig.md#channel-overview) for the frequency band of each channel.

## Operating time

!!! warning
    The Locator-U1 can only be submerged for about 6 hours. It then requires charging and time to dry the pressure sensor in order to provide accurate depth readings.

After getting GPS lock, the Locator-U1 keeps its time synchronization for around 6 hours. After this it needs to be brought to the surface to get a new GPS lock.

## Troubleshooting

| Problem | What to check |
|---------|---------------|
| No LED when the cap is screwed on | Make sure the cap is fully tightened. If the LED stays off, the battery may be empty: [charge](#charging) the Locator-U1 for 7 hours. |
| LED keeps flashing once per second | The Locator-U1 has not found GPS lock. Move it outdoors with a clear view of the sky. Indoors, a GPS repeater or similar is needed. |
| No signal from the Locator-U1 in the GUI | Check that the Locator-U1 has GPS lock, that the topside has GPS lock, and that the channel on the rotary switch matches the GUI. See also [Warnings](../interface/warnings.md). |
| Fast flashing LED | See [Error indication](#error-indication). |
| Battery runs out sooner than expected | Charge for at least 7 hours within 24 hours before use, with a 5 V / 2 A wall adapter, not a computer. |

## Wiring Interface

Since the Locator-U1 is battery powered, its only interface is the charging port, which is a standard USB-C connector.

## Included in Package

- Locator-U1  
- USB-C charging cable  
- Mounting bracket  

## Dimensions

![u1_dimensions](../../img/u1_dimensions.png)

## Datasheet

[Datasheet](https://waterlinked.com/underwater-gps-accessories#Downloads%2FResources)
