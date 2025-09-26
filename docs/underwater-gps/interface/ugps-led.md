# LED Indicators 
Only the topside box and the Locator U1 has LED indicators.

Here is a broken [link](http://dennelinken.fungererikke)

## Topside

|LED name 	| Description 					 											|
|-----------|---------------------------------------------------------------------------|
| Power		| Solid green: Topside has power 											|
| Ready		| Solid Green: Topside has booted successfully								|
| GPS		| Blinking green: Searching for GPS lock, solid green: Topside has GPS lock |
| LED 1		| Solid green: Firmware successfully loaded									|
| LED 2		| Not in use																|
| Locator	| Solid green: Locator D1 is connected										|
| Receiver 1| Solid green: Receiver 1 connected											|
| Receiver 2| Solid green: Receiver 2 connected											|
| Receiver 3| Solid green: Receiver 3 connected											|
| Receiver 4| Solid green: Receiver 4 connected											|

!!! Note 
	There is **No** indication when the **Antenna** is connected.

!!! Note
	*NC*: Not Connected.

	*DNC*: Do Not Connect, pins used for production.

	**GND**: Boldface indicate power lines (12 V, 3.3 V, VIN, GND).


## Locator-U1

- **No green light**  
  Power is off; the Locator-U1 is not ready for diving.

- **Flashing green light (once per second)**  
  The Locator-U1 is searching for GPS lock and is not ready to dive.

- **Fixed green light**  
  The Locator-U1 has GPS lock and is ready to dive.

- **Flashing green light (slow)**  
  The Locator-U1 previously had GPS lock but lost it. It is still ready to dive.

- **Fast flashing green light (multiple times per second)**  
  Error indication. The Locator-U1 is not ready to dive. This often happens if the device has exceeded its dive time and the pressure sensor requires drying, or if the battery power is very low. Charging the Locator helps to dry the sensor more quickly.


!!! Note
	The LED does not say anything about the battery status of the Locator-U1. The locator always needs to be charged for at least 7 hours with a proper 5V/2A charger befor use.