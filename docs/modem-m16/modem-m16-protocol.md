## Modem-M16 Protocol

You can configure the modem by issuing commands over the serial link. Five user-configurable parameters are available:

1. **Communication Channel**  
2. **Operation Mode**  
3. **Report Request**  
4. **Power Level**
5. **Parrot mode**

Each configuration command requires sending specific characters with a 1-second pause between them, followed by a character that selects the new value. Refer to the relevant section below.

---

### Communication Channel Command

The modem can operate on **12 channels** (1 to 12). Two modems must share the same channel to communicate.

**Procedure:**

1. Send `"c"` (0x63).  
2. Wait **1 second**.  
3. Send another `"c"` (0x63).  
4. Within **2 seconds**, send **one character** (`"1"`–`"c"`) to set the desired channel.

| **Channel** | **Character** | **HEX-Value** |
|:----------:|:-------------:|:-------------:|
| 1          | "1"           | 0x31          |
| 2          | "2"           | 0x32          |
| 3          | "3"           | 0x33          |
| 4          | "4"           | 0x34          |
| 5          | "5"           | 0x35          |
| 6          | "6"           | 0x36          |
| 7          | "7"           | 0x37          |
| 8          | "8"           | 0x38          |
| 9          | "9"           | 0x39          |
| 10         | "a"           | 0x61          |
| 11         | "b"           | 0x62          |
| 12         | "c"           | 0x63          |

**Example (Channel 11):**
1. Send `"c"`  
2. Wait 1 second  
3. Send `"c"` again  
4. Within 2 seconds, send `"b"` (0x62)  

---

### Setting Operational Mode

To toggle between **diagnostic mode** and **transparent serial mode**:

1. Send `"m"` (0x6D).  
2. Wait **1 second**.  
3. Send `"m"` again.  

The modem will switch modes (e.g., if you were in transparent mode, it will switch to diagnostic).

---

### Setting Power Level

To adjust the modem’s power level (1–4):

1. Send `"l"` (0x6C).  
2. Wait **1 second**.  
3. Send `"l"` again.  
4. Within 2 seconds, send one character (`"1"`, `"2"`, `"3"`, or `"4"`).

| **Power Level** | **Character** | **HEX-Value** | **Avg. TX Power (mW)** | **Typical Max Range (m)** |
|:--------------:|:-------------:|:-------------:|:----------------------:|:-------------------------:|
| 1              | "1"           | 0x31          | 390                    | 300                       |
| 2              | "2"           | 0x32          | 555                    | 600                       |
| 3              | "3"           | 0x33          | 790                    | 900                       |
| 4 (Default)    | "4"           | 0x34          | 1105                   | 1000                      |

!!! note
    Maximum range is highly dependent on environmental factors, including noise levels and line-of-sight conditions between modems.

**Example (Set Power Level 3):**
1. Send `"l"` (0x6C).  
2. Wait 1 second.  
3. Send `"l"` (0x6C) again.  
4. Within 2 seconds, send `"3"` (0x33).  

---

### Request Report Command

In **both** diagnostic and transparent modes, you can request a report at any time:

1. Send `"r"` (0x72).  
2. Wait **1 second**.  
3. Send `"r"` (0x72) again.

The modem will immediately generate a diagnostic report.


### Set parrot mode

In parrot mode the modem immediately return the message it just got. This feature can be useful mainly for testing of the modem.

To set parrot mode:

1. Send `"P"` (0x72).  
2. Wait **1 second**.  
3. Send `"P"` (0x72) again.


To reset parrot mode:

1. Send `"p"` (0x72).  
2. Wait **1 second**.  
3. Send `"p"` (0x72) again.
---