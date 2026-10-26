# Wiring interface

The tables below shows the pinning of the Modem-M16 interface. Depending on which type is used, the wires may have different colors. 

| Interface             | Colour (OEM)  | Colour (Standard) | Colour (Extended)|
| :---------------------| :---------------- | :---------------  | :---------------  |
| VIN                   | Orange (3V - 4.2V) <span class="swatch c-orange"></span>| Orange (3V - 4.2V) <span class="swatch c-orange"></span>| Orange (10V - 30V) <span class="swatch c-orange"></span>|
| GND                   | Orange-White       <span class="swatch c-orange-white"></span>| Orange-White       <span class="swatch c-orange-white"></span>| Orange-White       <span class="swatch c-orange-white"></span>|
| UART RX               | Blue               <span class="swatch c-blue"></span>| Blue               <span class="swatch c-blue"></span>| NA                |
| UART TX               | Blue-White         <span class="swatch c-blue-white"></span>| Blue-White         <span class="swatch c-blue-white"></span>| NA                |
| Shutdown (Active Low) | Green              <span class="swatch c-green"></span>| Green              <span class="swatch c-green"></span>| NA                |
| RS422 RX+             | NA                | NA                | Blue               <span class="swatch c-blue"></span>|
| RS422 RX-             | NA                | NA                | Blue-White         <span class="swatch c-blue-white"></span>|
| RS422 TX+             | NA                | NA                | Green              <span class="swatch c-green"></span>|
| RS422 TX-             | NA                | NA                | Green-White <span class="swatch c-green-white"></span> |

Maximum power consumption for package transmit is in range 390 mW to 1105 mW

!!! Note 
    Shutdown line can be used to control the ON/OFF state of the Modem. 
    If Shutdown is left floating, the Modem is ON. If Shutdown is short to GND, the modem is OFF. 
    Shutdown line can be controlled by an external open-drain, open-collector or relay device.
    DO NOT apply voltage to Shutdown line.

    The boot up time when powered on or toggling the shutdown line is approximately 12 ms.  




## Wiring OEM/Standard
![Standard](../img/modem_m16_standard_connection.png)
## Wiring Extended (RS422)
![Extended](../img/modem_m16_extended_connection.png)
