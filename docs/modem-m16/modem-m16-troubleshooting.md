# Troubleshooting: no response from the modem

Use this guide if the Modem M16 does not answer on the serial port, for example if you get no report, no reply to configuration commands, or nothing is received.

The most common cause is that the modem does not get enough power. A modem can answer when it is connected one way, and stop answering when it is moved to another board or adapter. This is often because the new board cannot deliver enough current.

Work through the steps in order. Each step removes one possible cause.

## 1. Power the modem from its own supply

Do not power the modem from the VCC or 3.3 V pin of a USB-to-UART adapter, a development board or a single-board computer. These pins are often not made for the current the modem needs when it transmits, and the voltage can drop or be at the wrong level.

Power the modem from a separate lab power supply or battery that can deliver the power below:

| Version                      | VIN (orange <span class="swatch c-orange" aria-hidden="true"></span>) | Transmit (Tx) | Receive (Rx) | Recommended test supply          |
| :--------------------------- | :------------ | :------------ | :----------- | :------------------------------- |
| UART (OEM, Standard, Flange) | 3.0–4.2 V DC  | < 1.1 W       | < 250 mW     | 3.3 V, at least 0.5 A            |
| RS422 (Extended)             | 10–30 V DC    | < 2.0 W       | < 400 mW     | 12 V, able to deliver over 2.0 W |

Source: the [Modem M16 product page](https://www.waterlinked.com/shop/modem-m16-186). At 3.3 V, 1.1 W is about 330 mA.

!!! Warning
    Do not connect 5 V to VIN on a UART version. 3.0–4.2 V is the allowed range.

If you use a lab power supply with a current limit, set the limit high enough. A current limit that is too low makes the voltage drop when the modem transmits.

## 2. Use a suitable converter for the data lines

Connect the modem to your computer with a converter that matches the interface:

* **UART versions:** a USB-to-UART converter with **3.3 V logic level**. If the converter has a 3.3 V / 5 V jumper, set it to 3.3 V. The UART is 3.3 V TTL, see [Interface overview](modem-m16-integration.md).
* **RS422 version (Extended):** a USB-to-RS422 converter.

Connect only the data lines and GND from the converter:

| Modem M16 wire (UART)  | Connect to                                               |
| :--------------------- | :------------------------------------------------------- |
| VIN, orange <span class="swatch c-orange" aria-hidden="true"></span> | + of the separate supply                                 |
| GND, orange-white <span class="swatch c-orange-white" aria-hidden="true"></span> | GND of the separate supply **and** GND of the converter  |
| UART RX, blue <span class="swatch c-blue" aria-hidden="true"></span> | TX of the converter                                      |
| UART TX, blue-white <span class="swatch c-blue-white" aria-hidden="true"></span> | RX of the converter                                      |
| Shutdown, green <span class="swatch c-green" aria-hidden="true"></span> | Leave floating (not connected)                           |

The GND of the supply and the GND of the converter must be connected together. Without a common GND the data lines do not work.

For the RS422 wire colours, see [Wiring interface](modem-m16-wiring.md).

!!! Note
    Leave the Shutdown line (green <span class="swatch c-green" aria-hidden="true"></span>) floating. If it is connected to GND, the modem is off. Do not apply a voltage to it.

## 3. Test with the Water Linked M16 driver

Before you test with your own software, test with our [Modem-M16-Driver](https://github.com/waterlinked/Modem-M16-Driver) on GitHub. It is known to work, so it tells you if the problem is in the hardware setup or in your own code.

* **Windows:** download `gui.exe` from the [latest release](https://github.com/waterlinked/Modem-M16-Driver/releases), see [GUI](modem-m16-gui.md). Select the COM port of the converter and connect.
* **Linux or Python:** follow the installation steps in the [README of the Modem-M16-Driver repository](https://github.com/waterlinked/Modem-M16-Driver#installation), and run `sending_examples.py`. Enter the serial port when asked (for example `/dev/ttyUSB0`).

Then request a report. The GUI has a button for this. In `sending_examples.py` the report is requested first and printed.

* **You get a report:** the modem, the power and the wiring work. If your own software still gets no answer, compare it with the driver. A common mistake is the timing: configuration commands, such as the report request, must be sent with almost exactly 1 second between the two characters, see [Protocol](modem-m16-protocol.md).
* **You get no report:** go back to step 1 and 2. Measure the voltage on VIN while you request the report. It must stay within the range in the table above.

## 4. Test communication between two modems

When both modems give a report, test that they can talk to each other:

* Put both modems in water, for example in the same bucket.
* Set both modems to the same channel.
* Send two bytes from one modem and check that the other modem receives them.

See [Quickstart](modem-m16-quickstart.md) for the default settings.

## 5. Contact support

If the modem still does not answer, submit a [support ticket](https://waterlinked.com/support) with:

* The serial number and version of the modem (UART or RS422).
* How the modem is powered: the supply or battery, its voltage and how much current it can deliver.
* The voltage you measured on VIN while you requested a report.
* The converter or board you use for the data lines, and its logic level.
* A photo or drawing of the wiring.
* What the M16 driver showed (a screenshot of the GUI or the output of `sending_examples.py`).
