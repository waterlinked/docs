# LED Indicators 
Only the topside box and the Locator-U1 have LED indicators.

## Topside

|LED name 	| LED | Description 					 											|
|-----------|:---:|---------------------------------------------------------------------------|
| Power		| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Topside has power 											|
| Ready		| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Topside has booted successfully								|
| GPS		| <span class="led led--blink" role="img" aria-label="LED flashing green"></span> <span class="led led--on" role="img" aria-label="LED solid green"></span> | Flashing green: Searching for GPS lock, solid green: Topside has GPS lock. The topside uses GPS both for its own position and to synchronize its clock |
| LED 1		| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Firmware successfully loaded									|
| LED 2		| <span class="led led--off" role="img" aria-label="LED off"></span> | Not in use																|
| Locator	| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Locator D1 is connected										|
| Receiver 1| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Receiver 1 connected											|
| Receiver 2| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Receiver 2 connected											|
| Receiver 3| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Receiver 3 connected											|
| Receiver 4| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Receiver 4 connected											|

!!! Note 
	There is **No** indication when the **Antenna** is connected.

!!! Note
	*NC*: Not Connected.

	*DNC*: Do Not Connect, pins used for production.

	**GND**: Boldface indicate power lines (12 V, 3.3 V, VIN, GND).


## Locator-U1

When powered on by screwing on the cap, the LED of the Locator-U1 shows whether its clock is synchronized with GPS time. The Locator-U1 uses GPS only for this time synchronization, not to find its own position.

| LED | Signal | Meaning | Ready to use? |
|:---:|--------|---------|:--------------:|
| <span class="led led--off" role="img" aria-label="LED off"></span> <span class="led-wave led-wave--off" aria-hidden="true"></span> | **No light** | Power is off, or the battery is empty. | No |
| <span class="led led--blink" role="img" aria-label="LED flashing once per second"></span> <span class="led-wave led-wave--blink" aria-hidden="true"></span> | **Flashing green light** (once per second) | Searching for a GPS signal. The clock is not synchronized yet. | No |
| <span class="led led--on" role="img" aria-label="LED solid green"></span> <span class="led-wave led-wave--on" aria-hidden="true"></span> | **Solid green light** | The clock is synchronized with GPS time. | **Yes** |
| <span class="led led--blink-slow" role="img" aria-label="LED flashing slowly"></span> <span class="led-wave led-wave--blink-slow" aria-hidden="true"></span> | **Flashing green light** (slow) | The GPS signal has been lost, for example because the Locator-U1 is in the water. The time synchronization is still valid, so the Locator-U1 keeps working. | **Yes** |
| <span class="led led--blink-fast" role="img" aria-label="LED flashing fast"></span> <span class="led-wave led-wave--blink-fast" aria-hidden="true"></span> | **Fast flashing green light** (multiple times per second) | Error. Often the operating time has been exceeded and the pressure sensor needs to dry; charging the Locator-U1 helps the sensor dry more quickly. It can also be another internal failure. | No |

When connected to a charger, the LED behavior depends on the serial number (SN):

| SN | LED while charging |
|----|--------------------|
| **0556 and higher** | The Locator-U1 only charges and does not power on. <span class="led led--breathe" role="img" aria-label="LED breathing green"></span> Breathing green: charging. <span class="led led--on" role="img" aria-label="LED solid green"></span> Solid green: fully charged. |
| **0555 and lower** | The Locator-U1 powers on while charging. The LED does **not** show the battery or charging status. |

Charge the Locator-U1 with a 5 V / 2 A wall adapter before use: on SN: 0556 and higher until the LED is solid green, on SN: 0555 and lower for at least 7 hours.

The serial number is printed on the flat side of the Locator-U1, where the bracket is mounted. See [Locator-U1](../locators/locator-u1.md#led-signals) for full details on the LED signals and [charging](../locators/locator-u1.md#charging).
