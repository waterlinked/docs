# Quickstart Guide
To start using the Modem-M16 you need 

- a connection between the Modem and your computer
- a serial connection interface

---

To send and receive data between two Modem-M16's:

- both modems has to be in water (or less than 5 cm apart in air)
- both modems must be connected to a computer
- both modems need to be configured to the same channel.
- A sufficient power level must be used.

For an overview of the modems setting see [Modem M16 Settings interface](../modem-m16/modem-m16-integration.md#settings-interface)
For implemetation of the modems settings see [Modem M16 Protocol](../modem-m16/modem-m16-protocol.md)

---

By default the Modem M16 is delivered with the following settings:

- **Operational Mode:** Transparent serial mode  
- **Communication Channel:** 1  
- **Power level/Range Mode:** 4

---

## How to connect to the Modem-M16

For wiring details see: [Modem-M16 Wiring](../modem-m16/modem-m16-wiring.md)


### Connect using UART:
- Connect VIN to a 3.3V power source, and ground to ground/VOUT
- Connect to your computer for instance using a UART to USB cable. 

### Connect using RS422:
- Connect VIN to a 12V (10-30V) power supply, and ground to ground/VOUT.
- Connect to your computer using an RS422 to USB serial converter.

### Open up a user interface to interact with the modem
Open up a serial interface on your computer. This is typically Minicom on Linux and Putty on Windows.

It is also possible to use the designated GUI that can be installed on your computer. An installation guide is available here: [Basic GUI for easy implementation](../modem-m16/modem-m16-gui.md)  

---

## Configure the Modem-M16
When you are connected to a modem and have an open user interface, you will be able to read and write to configure the modem.
The most basic configurations you need to know about are:

**Operational mode**
There are two operational modes:
- Transparent mode, that only processes and transmits two bytes of data
- Diagnostic mode, that processes and transmits two bytes of data, and sends a detailed status report of the modem.

**Changing channel**
For two modems to be able to communicate, they need to be configured on the same channel.

**Range mode**
The modem have four different range modes or power levels, numbered 1 to 4, where 1 have the shortest range and 4 have the longest range. Shorter range uses less power during operation.

More information about the serial protocol and possible configurations of the M16, can be found here: [M16-serial-protocol](../modem-m16/modem-m16-protocol.md)

---

## Start communicating between two modems
To be able to see what you send and receive on the modems you will have to open up one interface for each modem. Adjust the com/tty ports as necessary.

Begin sending data using either the GUI or the serial protocol; the modems will relay up to 2 bytes each ~1.6 seconds.

---

## Make your own interface that suits your needs
Use the serial protocol [M16-serial-protocol](../modem-m16/modem-m16-protocol.md), and the Example Python Report Parser (described under Protocol) to create your own application that suites your needs.

---

