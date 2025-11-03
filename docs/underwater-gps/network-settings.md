# Network Settings
The Underwater GPS GUI is web based, and can be accessed using your favorite web browser. Connect to the system through either of the methods listed below.

!!! Note
    We currently support and recommend Chrome, Firefox, Safari and Edge. </br>
    Internet Explorer is not supported as of now.

## WiFi

The local Underwater GPS WiFi is configured as:

|            |               |
| ---------- | :------------ |
| Mode     : | Access Point  |
| SSID     : | UnderwaterGPS |
| Password : | waterlinked   |
| Security : | WPA2-Personal | 

To connect to the UGPS over it's local wifi
- Power on the UGPS and wait for GPS lock and the Ready LED to be lit.
- Connect to the UnderwaterGPS GUI on: [http://192.168.7.1/](http://192.168.7.1/)

## Ethernet

At power-up, the Master-D1 reads the IP switch settings. The ethernet network mode depends on the switch position.

| Network mode             | Direction            | IP switch position |
| ------------------------ | :------------------- | :------------------- |
| Configurable             | UP                   | ![](../img/IP_switch_configurable.png) |
| Static IP 192.168.194.94 | DOWN                 | ![](../img/IP_switch_static_192.png) |

### Configurable mode
In the configurable mode the UGPS will receive an IP adress from the local router and can be reached on the assigned IP address.

### Fallback or static IP
The UGPS can always be reached on its static IP adress. 

Before turning the UGPS on:

- Connect the UGPS ethernet directly to your computer
- Set the switch in the static IP position 

Then:

- Power on the UGPS and wait for GPS lock and the Ready LED to be lit.
- Configure your computer to static IP on the same subnet as the UGPS.
For example: If the IP address of the UGPS is 192.168.194.94 the host computer needs to be configured to a different 192.168.194.x address e.g. 192.168.194.100.
- Connect to the UnderwaterGPS GUI on: [http://192.168.194.94/](http://192.168.194.94/)

!!! Note
    With blueOS the static IP is 192.168.2.94