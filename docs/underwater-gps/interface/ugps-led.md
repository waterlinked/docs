# LED Indicators 
Only the topside box and the Locator-U1 have LED indicators.

## Topside

|LED name 	| LED | Description 					 											|
|-----------|:---:|---------------------------------------------------------------------------|
| Power		| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Topside has power 											|
| Ready		| <span class="led led--on" role="img" aria-label="LED solid green"></span> | Solid green: Topside has booted successfully								|
| GPS		| <span class="led led--blink" role="img" aria-label="LED flashing green"></span> <span class="led led--on" role="img" aria-label="LED solid green"></span> | Flashing green: Searching for GPS lock, solid green: Topside has GPS lock |
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

When powered on by screwing on the cap, the Locator-U1 LED shows the GPS lock status:

| LED | Signal | Meaning | Ready to dive? |
|:---:|--------|---------|:--------------:|
| <span class="led led--off" role="img" aria-label="LED off"></span> <span class="led-wave led-wave--off" aria-hidden="true"></span> | **No light** | Power is off. | No |
| <span class="led led--blink" role="img" aria-label="LED flashing once per second"></span> <span class="led-wave led-wave--blink" aria-hidden="true"></span> | **Flashing green light** (once per second) | Searching for GPS lock. | No |
| <span class="led led--on" role="img" aria-label="LED solid green"></span> <span class="led-wave led-wave--on" aria-hidden="true"></span> | **Solid green light** | GPS lock acquired. | **Yes** |
| <span class="led led--blink-slow" role="img" aria-label="LED flashing slowly"></span> <span class="led-wave led-wave--blink-slow" aria-hidden="true"></span> | **Flashing green light** (slow) | GPS lock was acquired but has since been lost. | **Yes** |
| <span class="led led--blink-fast" role="img" aria-label="LED flashing fast"></span> <span class="led-wave led-wave--blink-fast" aria-hidden="true"></span> | **Fast flashing green light** (multiple times per second) | Error. Often the dive time has been exceeded and the pressure sensor needs to dry, or the battery is very low. Charging the Locator-U1 helps the sensor dry more quickly. | No |

When connected to a charger, the LED behavior depends on the serial number (SN):

| SN | LED while charging |
|----|--------------------|
| **0556 and higher** | The Locator-U1 only charges and does not power on. <span class="led led--breathe" role="img" aria-label="LED breathing green"></span> Breathing green: charging. <span class="led led--on" role="img" aria-label="LED solid green"></span> Solid green: fully charged. |
| **0555 and lower** | The Locator-U1 powers on while charging. The LED does **not** show the battery or charging status. |

Always charge the Locator-U1 for at least 7 hours with a 5 V / 2 A wall adapter before use.

See [Locator-U1](../locators/locator-u1.md#led-signals) for full details on the LED signals and [charging](../locators/locator-u1.md#charging).
