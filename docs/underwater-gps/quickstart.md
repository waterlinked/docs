# Quickstart

## Intro
The UGPS system consists of three components:

 - [The UGPS Topside](../underwater-gps/ugps-topside.md)

 - Baseline: [Antenna](../underwater-gps/antenna.md) or [receivers](../underwater-gps/receiver-d1.md)

 - Locator: 
 You can choose between three different locators: [Locator-A1](../underwater-gps/locators/locator-a1.md), [Locator-D1](../underwater-gps/locators/locator-d1.md) and [locator-U1](../underwater-gps/locators/locator-u1.md)

 In addition you need a [power supply](../underwater-gps/power-supply.md)


## A quick guide on how to start using the Underwater GPS system:

* Power on the topside unit
* Connect your computer to the Underwater GPS topside box
* Attach the locator (unless you are using the wireless U1) and the antenna/receivers to the topside box
* Deploy the antenna or receivers in water, in such a way that it will have line of sight to the locator when it is deployed.
* Attach the locator to the unit you want to track (eg. ROV/diver etc.)
* If using a locator U1, make sure it has GPS lock before it is deployed into water (steady green LED).
* Open up the GUI and adjust the settings. Make sure to select the correct locator and channel.
* Configure antenna/receiver placement in the GUI
* Set heading

!!! Tip
    If you are using a locator U1, make sure it is charged for at least 7 hours with a 5V/2A charger (not a computer) within 24 hours before use, and that it is adjusted to your preferred channel. Choosing channel 3 is usually good advice.

## Power on the topside unit

Start by connecting power to the UGPS G2 topside box using your prefered [power supply](../underwater-gps/power-supply.md). Make sure to place the box where there are good GPS signals. The GPS receiver in the topside box will begin receiving signals and achieve a lock whilst we setup the rest of the system.

If you are using the Locator-U1, make sure it is fully charged and set to the chosen channel, then power it on now as well. It too will acquire a GPS lock whilst we setup the rest of the system.

If you are inside, use of a GPS repeater or similar will be necessary.

## Connect to the Underwater GPS topside box

Connect to the WiFi access point **UnderwaterGPS** on your PC/tablet/smartphone. The WiFi password is **waterlinked**. Navigate to [http://192.168.7.1/](http://192.168.7.1/) in a web browser to access the Underwater GPS web GUI.

For alternative ways to connect to the topside, see [Networking](../underwater-gps/network-settings.md)

## Deploy locator and antenna/receivers

### Locator

Attach the locator ([U1](../underwater-gps/locators/locator-u1.md), [A1](../underwater-gps/locators/locator-a1.md), or [D1](../underwater-gps/locators/locator-d1.md)) to your vehicle. The [BlueROV2 integration guide](../underwater-gps/integration/bluerov-integration.md) may be helpful if integrating an A1 or D1 locator with a vehicle tether.

If using an A1 or D1 locator, connect it to the 'Locator' bulkhead on the UGPS G2 topside box. The U1 connector is wireless, which means that this step can be omitted.

![pelicase_connectors](../img/pelicase_g2_connectors.png)

### Antenna

Unfold the [antenna](../underwater-gps/antenna.md) and lock the mast straight using the latches on the folding joints. Avoid the cable being pinched at the joints. Secure the three arms in place using the thumb screw. Place the antenna in water at the desired location. Secure the antenna using the RAM Mount components included with the antenna.

Connect the antenna to the bulkhead marked 'Receiver 1/Antenna' on the UGPS G2 topside box (see the above picture).

!!! Tip
	If the RAM Mount components included with the antenna do not meet your needs, many alternative RAM Mount Arms and Bases are [available](https://www.rammount.com/shop-all/popular-components/c-size).

### Loose receivers

Before deploying the [receivers](../underwater-gps/receiver-d1.md) in the water, add a piece of tape to each receiver cable at the desired depth, to make [configuration](#configure-antennareceiver-placement-and-search-range) easier. Place the receivers in the water at the desired location, and connect one to each of the four bulkheads 'Receiver 1', 'Receiver 2', 'Receiver 3', and 'Receiver 4' of the UGPS G2 topside box (see the above picture).

!!! Tip
    Add a weight just above each receiver to improve stability in the water.

## Select locator and channel in the GUI

Select the correct locator type in the [GUI settings](../underwater-gps/interface/ugps-gui.md#settings), and choose which channel to listen on. Channel 2 is the default. If using a [Locator-U1](../underwater-gps/locators/locator-u1.md), ensure that its channel (set by completely unscrewing the lid and turning the dial inside) is set to the same channel as you configure in the GUI.

!!! Note
    If you are using the Locator-A1, depth information needs to be provided to the topside unit by means of the UGPS [API](../underwater-gps/integration/api.md). You can ignore this if following the [BlueROV2 integration guide](../underwater-gps/integration/bluerov-integration.md).

## Configure antenna/receiver placement and search range

Provide the correct placement of the antenna/receivers relative to the topside box in the [GUI settings](../underwater-gps/interface/ugps-gui.md#settings), and, if using an antenna, specify if it has been rotated from the default indicated in the GUI.

Specifically, for the antenna, enter the position and optionally the rotational angle manually under **Advanced settings**.

![antenna_configuration_g2](../img/antenna_configuration_g2.png)

If using loose receivers, either drag and drop each receiver to its position, or enter the positions manually.

![receiver_configuration_g2](../img/receiver_configuration_g2.png)

Limit the search area by changing its radius, direction or sector size in the GUI

![search_configuration_g2](../img/search_configuration_g2.png)

!!! Tip
    Reducing the search area can improve the performance of the system, and we recommend to do this as far as possible, even if operating in a small area such as a tank or pool.

## Set heading

In the top bar of the GUI you will see a warning about missing heading. Click the link, click to zero the gyros, then set compass heading to a reference heading (e.g. from an analogue compass, compass app, or boat compass).

!!! Note
The topside does not have an integrated compass. An IMU will keep track of the heading based on the initially stated heading in the configuration. In a static environment setting the heading once will be enough, but in a more dynamic environment the IMU will drift over time and the heading will need a regular update. If operating in more demanding environments it is recommended to use an external compass to keep the heading updated. 

!!! info
    Setting the heading replaces IMU calibration as of release 3.3.0.

You are now ready to explore the underwater world while knowing where you are!
