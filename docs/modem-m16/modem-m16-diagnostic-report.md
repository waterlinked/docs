# Diagnostic report
This document describes the structure of the diagnostic report and how to decode it.

## Packet Structure of the Diagnostic Report

When in diagnostic mode (or upon a report request in transparent mode), the modem sends an **18-byte** report. The byte layout is:

| **Byte (bit)** | **Field**              | **Description**                                                                                 |
|:--------------:|:-----------------------|:-----------------------------------------------------------------------------------------------:|
| 0 (0:7)        | `START_OF_FRAME (SOF)` | “$” (0x24)                                                                                      |
| 1:2 (0:15)     | `TB`                   | Transport block containing 2 bytes of received data.                                            |
| 3 (0:7)        | `BER`                  | Bit error rate                                                                                  |
| 4 (0:7)        | `SIGNAL_POWER`         | Relative signal power (0–255)                                                                   |
| 5 (0:7)        | `NOISE_POWER`          | Relative noise power (0–255)                                                                    |
| 6:7 (0:15)     | `PACKET_VALID`         | Indicates packet integrity: LDPC decode + CRC successful                                        |
| 8 (0:7)        | `PACKET_INVALID`       | CRC check failed                                                                                |
| 9 (0:7)        | `GIT_REV`              | Firmware revision (Git commit hash, 8-bit)                                                      |
| 10:12 (0:23)   | `TIME_FROM_BOOT`       | Time since power-up in 10 ms increments                                                         |
| 13:14 (0:15)   | `CHIP_ID`              | FPGA chip ID                                                                                    |
| 15 (0:1)       | `HW_REV`               | Hardware revision (2 bits)                                                                      |
| 15 (2:5)       | `CHANNEL`              | Active communication channel (1–12)                                                             |
| 15 (6)         | `TB_VALID`             | Transport block valid bit; indicates new TB data                                                |
| 15 (7)         | `TX_COMPLETE`          | Indicates that a transmission has finished                                                      |
| 16 (0)         | `DIAGNOSTIC_MODE`      | 1 if in diagnostic mode; 0 otherwise                                                            |
| 16 (1)         | `RESERVED`             | Reserved bit                                                                                    |
| 16 (2:3)       | `POWER_LEVEL`          | Current power level (0 = L4, 1 = L3, 2 = L2, 3 = L1)                                            |
| 16 (4:7)       | `RESERVED`             | Reserved bits                                                                                   |
| 17 (0:7)       | `END_OF_FRAME (EOF)`   | New line (“\n”)                                                                                 |

!!! warning
    **Signal Power & Noise Power**  
    - Both range from 0 to 255.  
    - When the modem is idle (not transmitting or receiving), **Signal Power** reflects the background noise floor, which should match **Noise Power**.  
    - **During** packet decoding, `SIGNAL_POWER` should be **greater** than `NOISE_POWER` for a successful decode.

    **Practical Tip**  
    - Record the Noise Power while idle as your baseline (noise floor).  
    - Compare that with Signal Power during active communication.  
    - The bigger the gap, the better the link quality. (Could be closer to each other)

---

## Example Python Report Parser

```python
def decode_packet(packet: bytes) -> Optional[Dict[str, Any]]:
    """
    Decode a packet received from the modem.

    Parameters
    ----------
    packet : bytes
        The raw packet (18 bytes) starting with '$' (0x24) and ending with '\n' (0x0A).

    Returns
    -------
    Optional[Dict[str, Any]]
        A dictionary with decoded values if valid, or None otherwise.
    """
    if len(packet) != 18 or packet[0] != ord('$') or packet[-1] != ord('\n'):
        return None

    # The 16 bytes after the '$' and before the '\n'
    data = packet[1:17]
    decoded = struct.unpack("<HBBBHBBBBBHBB", data)

    decoded_dict = {
        "TR_BLOCK": decoded[0],
        "BER": decoded[1],
        "SIGNAL_POWER": decoded[2],
        "NOISE_POWER": decoded[3],
        "PACKET_VALID": decoded[4],
        "PACKET_INVALID": decoded[5],
        "GIT_REV": decoded[6].to_bytes(1, "little"),
        "TIME": (decoded[9] << 16) | (decoded[8] << 8) | decoded[7],
        "CHIP_ID": decoded[10],
        "HW_REV": decoded[11] & 0b00000011,
        "CHANNEL": (decoded[11] & 0b00111100) >> 2,
        "TB_VALID": (decoded[11] & 0b01000000) >> 6,
        "TX_COMPLETE": (decoded[11] & 0b10000000) >> 7,
        "DIAGNOSTIC_MODE": decoded[12] & 0b00000001,
        "LEVEL": (decoded[12] & 0b00001100) >> 2,
    }

    return decoded_dict
```