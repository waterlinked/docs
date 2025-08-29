# Wiring interface

The tables below shows the pinning of the Modem-M16 interface. Depending on which type is used, the wires may have different colors. 

| Interface             | Colour (OEM)  | Colour (Standard) | Colour (Extended)|
| :---------------------| :---------------- | :---------------  | :---------------  |
| VIN                   | Orange (3V - 4.2V)| Orange (3V - 4.2V)| Orange (10V - 30V)|
| GND                   | Orange-White      | Orange-White      | Orange-White      |
| UART RX               | Blue              | Blue              | NA                |
| UART TX               | Blue-White        | Blue-White        | NA                |
| Shutdown (Active Low) | Green             | Green             | NA                |
| RS422 RX+             | NA                | NA                | Blue              |
| RS422 RX-             | NA                | NA                | Blue-White        |
| RS422 TX+             | NA                | NA                | Green             |
| RS422 TX-             | NA                | NA                | Green-White       |

Maximum power consumption for package transmit is in range 390 mW to 1105 mW

!!! Note 
Shutdown line can be used to control the ON/OFF state of the Modem. 
If Shutdown is left floating, the Modem is ON. If Shutdown is short to GND, the modem is OFF. 
Shutdown line can be controlled by an external open-drain, open-collector or relay device.
DO NOT apply voltage to Shutdown line. 


## Wiring OEM/Standard
![Standard](../img/modem_m16_standard_connection.png)
## Wiring Extended (RS422)
![Extended](../img/modem_m16_extended_connection.png)
