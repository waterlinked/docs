# Integration
This document describes an overview of how the underwater modem can be operated. The modem can be controlled using a 3.3V UART or RS422 connection. It is offering two primary operational modes (transparent mode and diagnostic mode), four different power levels, user-selectable communication channels, and a possibility to set the modem in parrot mode for testing.

For details of the protocol used to implement the settings, see [Modem-M16-Protocol](../modem-m16/modem-m16-protocol.md)

---

## Interface overview

The Modem-M16 has a 3.3 volt UART interface and a RS422 interface with the following configuration:

| Settings         | Value  |
| :--------------- | :----- |
| Baud rate        | 9600   |
| Data parity stop | 8N1    |
| Flow control     | None   |


Users can switch between **3.3V TTL UART** or **RS422** for physical interfacing. Through this serial link, you can:

- Set operational modes  
- Change communication channels  
- Request diagnostic reports  
- Adjust power levels for transmission range/power consumption  
- Set modem in parrot mode for testing

---

## Settings Interface

You can configure the modem by issuing commands over the serial link. Five user-configurable parameters are available:

1. **Communication Channel**  
2. **Operation Mode**  
3. **Power Level**
4. **Report Request**  
5. **Parrot mode**

Each configuration command requires sending specific characters with a 1-second pause between them, followed by a character that selects the new value. For details on how to send the commands, see the configuration protocol:[Modem-M16-Protocol](../modem-m16/modem-m16-protocol.md)

---

### Communication Channel

The modem can operate on **12 channels** (1 to 12). This allows for several modems to be used at the same time. Two modems must share the same channel to communicate.
There are two ways to implement communication between several modems. You can have several sending modems that transmit on different channels, and one receiving modem that switch between the channels to listen for messages, or you can have several sending and receiving modems, where every two modems are sending and listening to each other on the same channel.


### Operational Modes

The modem supports two main operational modes:

**Transparent Serial Mode**  

   - Processes and transmits only **2 bytes** of data per packet.  
   - Each transmission takes ~1.6 seconds (acoustic wave duration).  
   - Data beyond the first 2 bytes in a transmission is discarded.

**Diagnostic Mode**

   - Sends detailed status reports, the same report that can be retrieved with the "request report" command, including:  
     - Transport Block (TB)  
     - Bit Error Rate (BER)  
     - Signal & Noise Power  
     - LDPC/CRC Validity  
     - Firmware Revision  
     - Time Since Power-Up  
     - FPGA Chip ID, Hardware Revision  
     - Communication Channel  
     - TX-Complete Status  
     - Power Level Setting  
   - Still limited to **2 bytes** of payload per transmission (discarding any additional data).  
   - Reports are triggered automatically when:
     1. A new packet is received (TB Valid bit is set)  
     2. A transmission completes (TX Complete bit is set)  
     3. 4 seconds have elapsed since the last report  

!!! note
    You can also request a **diagnostic report** while in transparent mode. See the [Request Report Command](#request-report) section.

---

### Power Levels

The modem has four power levels where 1 is the weakest and 4 is the strongest level. If you need to save power and do not require the signal to travel a long distance, you might want to choose a lower power level.
By default the modem is set to maximal power and range. Up to 1000m.

| **Power Level** | **Avg. TX Power (mW)** | **Typical Max Range (m)** |
|:--------------:|:----------------------:|:-------------------------:|
| 1              | 390                    | 300                       |
| 2              | 555                    | 600                       |
| 3              | 790                    | 900                       |
| 4 (Default)    | 1105                   | 1000                      |


!!! note
    Maximum range is highly dependent on environmental factors, including noise levels and line-of-sight conditions between modems.

---

### Request Report

The diagnostic report provided by this command is the same as the report retrieved every fourth second in diagnostic mode. 

In **both** diagnostic and transparent modes, you can request a report at any time.

When a command is sent the modem will immediately generate a diagnostic report.

For details of the structure of the diagnostic report and how it can be decoded see [Diagnostic report](../modem-m16/modem-m16-diagnostic-report.md)

---

### Parrot mode

A modem can be set to parrot mode, which might be useful for tests. When a modem is in parrot mode it always immediately returns the acoustic message it receives. 
This can typically be used in range tests with one modem set to parrot mode and one modem sending an acoustic message and wait for it to be returned.

!!! note
   Do not forget to reset parrot mode after use.

---

## Ensuring Successful Transmission & Optimization

### Diagnostic Mode
A report is sent immediately after each transmission.  
Monitor the **TX_COMPLETE** bit in the report to know when the modem is ready for the next 2-byte packet. This approach maximizes overall throughput.

### Transparent Serial Mode
Send 2 bytes, then wait at least **1.6 seconds** (the transmission duration) before sending the next 2 bytes to avoid data loss.

---

## Flash Memory Considerations
Changing the **modem mode**, **channel**, or **power level** initiates a **flash write operation**, which takes about **1 second**. During this time:

- The modem will **not respond** to commands.  
- **Do not power off** the modem to avoid corrupting settings.

Once the flash write completes, the modem resumes normal operation with the updated configuration.


## Firmware Release Notes

Below is a summary of the new features introduced in every firmware release:

| **FW release (ASCII/HEX)** | **Description**                                              |
|:--------------------------:|:-------------------------------------------------------------|
| **o/6f**                   | Initial firmware release                                     |
| **V/56**                   | Added power-level configuration for extended battery runtime and reduced range |

---
