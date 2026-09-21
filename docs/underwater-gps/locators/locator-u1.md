# Locator-U1

[Buy Locator-U1 here!](https://waterlinked.com/product/locator-u1/)

## Description

The Locator-U1 is a battery-powered, digital hydroacoustic locator device. It includes an internal GPS-based time-sync module, eliminating the need for a tether. This makes it ideal for divers, ROVs lacking convenient power sources, or other underwater applications.

The Locator-U1 has its own pressure sensor and measures its own depth. The topside uses this depth together with the acoustic signal to calculate the position of the Locator-U1.

!!! Note
    You will need GPS lock on the topside as well when using the U1. This is for timing purposes, it will not help to use only external GPS position as this can not be used for time synchronization. It is not enough to only have GPS lock on the U1.

## Before each use

Use this checklist to get the Locator-U1 ready. Each step links to the detailed description further down the page.

| Step | What to do | LED |
|:----:|------------|:---:|
| 1 | [Charge](#charging) the Locator-U1 with a 5 V / 2 A wall adapter, within 24 hours before use. On SN: 0556 and higher the LED turns solid green when the battery is full; on SN: 0555 and lower, charge for 7 hours. | <span class="led led--breathe" role="img" aria-label="LED breathing green"></span> → <span class="led led--on" role="img" aria-label="LED solid green"></span><br><small>SN: 0556 and higher</small> |
| 2 | Unplug the charger. With the cap off, set the [channel](#channel-selection) on the rotary switch to the same channel as in the GUI. | |
| 3 | Check that the O-ring in the cap is clean and undamaged, then [screw the cap on](#powering-on-and-off) to power on. The Locator-U1 searches for GPS lock. | <span class="led led--blink" role="img" aria-label="LED flashing once per second"></span> |
| 4 | Keep the Locator-U1 in open sky until the LED turns solid green. It now has GPS lock and is ready to use. | <span class="led led--on" role="img" aria-label="LED solid green"></span> |
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

4) **Charge the battery**  
   On **SN: 0556 and higher**, the LED shows when the battery is full: charging is finished when the LED stops breathing and is solid green.  
   On **SN: 0555 and lower**, the LED does not show the charging status, so leave the Locator-U1 connected for a full 7 hours.  
   Charging overnight the night before use is a recommended routine.

### LED behavior while charging

The LED behavior while charging depends on the serial number (SN) of your Locator-U1. The serial number is printed on the flat side of the Locator-U1, where the bracket is mounted. Select the tab that matches your unit.

=== "SN: 0556 and higher"

    When connected to a charger, the Locator-U1 only charges. It does **not** power on, does **not** search for GPS, and the LED shows the charging status only:

    | LED | Signal | Meaning |
    |:---:|--------|---------|
    | <span class="led led--breathe" role="img" aria-label="LED breathing green"></span> <span class="led-wave led-wave--breathe" aria-hidden="true"></span> | **Breathing green light** (slowly fading in and out) | The Locator-U1 is charging. |
    | <span class="led led--on" role="img" aria-label="LED solid green"></span> <span class="led-wave led-wave--on" aria-hidden="true"></span> | **Solid green light** | The battery is full. Here solid green means *fully charged*, not GPS lock. |

    Screw the cap on to power the Locator-U1 on. The LED then shows the GPS lock status instead, as described in [LED behavior while in use](#led-signals).

=== "SN: 0555 and lower"

    When connected to a charger, the Locator-U1 powers on and charges at the same time. The LED does **not** indicate charging progress:

    | LED | Signal | Meaning |
    |:---:|--------|---------|
    | <span class="led led--blink" role="img" aria-label="LED flashing green"></span> <span class="led-wave led-wave--blink" aria-hidden="true"></span> | **Flashing green light** | The Locator-U1 is powered on and working normally, for example searching for GPS lock. This does **not** reflect charging status. |
    | <span class="led led--on" role="img" aria-label="LED solid green"></span> <span class="led-wave led-wave--on" aria-hidden="true"></span> | **Solid green light** | The Locator-U1 is powered on and has GPS lock. This does **not** mean it is fully charged. Keep charging for the full 7 hours. |

## Powering on and off

- **To power on** the Locator-U1, securely tighten the cap over the charging port. The LED will begin flashing to indicate that it is searching for a GPS lock. Once the LED stops flashing and becomes solid, the Locator-U1 has acquired a GPS lock and is ready for use.  
  Ensure the O-ring in the cap is undamaged before submerging the device.

- **To power off** the Locator-U1, unscrew the cap until the LED turns off.

## LED behavior while in use { #led-signals }

These signals apply when the Locator-U1 is powered on by screwing on the cap. For the LED while connected to a charger, see [LED behavior while charging](#led-behavior-while-charging).

| LED | Signal | Meaning | Ready to use? |
|:---:|--------|---------|:--------------:|
| <span class="led led--off" role="img" aria-label="LED off"></span> <span class="led-wave led-wave--off" aria-hidden="true"></span> | **No light** | Power is off, or the battery is empty. | No |
| <span class="led led--blink" role="img" aria-label="LED flashing once per second"></span> <span class="led-wave led-wave--blink" aria-hidden="true"></span> | **Flashing green light** (once per second) | Searching for GPS lock. | No |
| <span class="led led--on" role="img" aria-label="LED solid green"></span> <span class="led-wave led-wave--on" aria-hidden="true"></span> | **Solid green light** | GPS lock acquired. | **Yes** |
| <span class="led led--blink-slow" role="img" aria-label="LED flashing slowly"></span> <span class="led-wave led-wave--blink-slow" aria-hidden="true"></span> | **Flashing green light** (slow) | GPS lock was acquired but has since been lost. | **Yes** |
| <span class="led led--blink-fast" role="img" aria-label="LED flashing fast"></span> <span class="led-wave led-wave--blink-fast" aria-hidden="true"></span> | **Fast flashing green light** (multiple times per second) | Error. See [Error indication](#error-indication). | No |

!!! Note
    The animations above illustrate the LED patterns. The exact timing on the Locator-U1 may vary slightly.

### Empty battery

A completely empty battery looks the same as a Locator-U1 that is switched off: the LED stays dark. So if the LED is dark with the cap screwed on, the Locator-U1 most likely needs [charging](#charging).

If the LED also stays dark when the Locator-U1 is connected to the charger, the battery is so deeply discharged that it may be damaged. Leave the Locator-U1 connected to the charger, as this can recover the battery. If the LED is still dark after a full charge, contact [support](https://support.waterlinked.com/en/knowledge).

### Error indication

A fast flashing LED often means one of the following:

- The Locator-U1 has exceeded its [operating time](#operating-time) and the pressure sensor needs to dry. Charging the Locator-U1 helps the sensor dry more quickly.
- The battery is very low. [Charge](#charging) the Locator-U1.

## Channel selection

The channel is selected with the rotary switch inside the cap. Unscrew the cap completely to access the switch. The channel on the Locator-U1 must match the channel selected in the [GUI settings](../interface/ugps-gui.md#settings). Channel 3 is usually a good choice. See the [channel overview](../ugps-sysconfig.md#channel-overview) for the frequency band of each channel.

## Operating time

The Locator-U1 can be used for about 6 hours at a time. After this it needs to be brought to the surface, because all three of the following have run out:

- The pressure sensor needs to dry, otherwise the depth readings become inaccurate.
- The battery needs recharging. How long the battery lasts varies with the water temperature, and is shorter in cold water.
- The GPS time synchronization needs refreshing, which the Locator-U1 does in open sky.

!!! warning
    Do not keep the Locator-U1 submerged for longer than about 6 hours. It then requires charging and time to dry the pressure sensor in order to provide accurate depth readings.

## Troubleshooting

| Problem | What to check |
|---------|---------------|
| The LED is dark when the cap is screwed on | Make sure the cap is fully tightened. If the LED stays dark, see [Empty battery](#empty-battery). |
| LED keeps flashing once per second | The Locator-U1 has not found GPS lock. Move it outdoors with a clear view of the sky. Indoors, a GPS repeater or similar is needed. |
| No signal from the Locator-U1 in the GUI | Check that the Locator-U1 has GPS lock, that the topside has GPS lock, and that the channel on the rotary switch matches the GUI. See also [Warnings](../interface/warnings.md). |
| Fast flashing LED | See [Error indication](#error-indication). |
| Battery runs out sooner than expected | Charge within 24 hours before use with a 5 V / 2 A wall adapter, not a computer. The battery also lasts shorter in cold water. |

## Wiring interface

Since the Locator-U1 is battery powered, its only interface is the charging port, which is a standard USB-C connector.

## Included in package

- Locator-U1  
- USB-C charging cable  
- Mounting bracket  

## Mounting and dimensions { #dimensions }

Each side of the Locator-U1 has three M3 mounting holes, and the included bracket fits these. The serial number is printed on the flat side where the bracket is mounted.

![u1_dimensions](../../img/u1_dimensions.png)

## Datasheet

[Datasheet](https://waterlinked.com/underwater-gps-accessories#Downloads%2FResources)
