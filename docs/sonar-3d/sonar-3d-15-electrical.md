# Wiring Sonar 3D-15

The tables below shows the pinning of the Sonar 3D-15 interface.

| Interface         | Color         |
| :-----------------| :-------------|
| Negative/Ground   | Black         |
| Positive (10-30V) | Red           |
| ETH RX+           | Green/White   |
| ETH RX-           | Green         |
| ETH TX-           | Orange        |
| ETH TX+           | Orange/White  |
| Shielded wire     | Naked (silver)| 

# LED Sonar 3D-15

The table below shows the LED behavior of the Sonar 3D-15.

| LED behavior          | Description                   |
| :---------------------| :-----------------------------|
| No light | Power is off |
| Solid green | Powering on |
| Flashing green, mostly off (slow, about every second) | Power on, acoustics disabled |
| Flashing green, mostly on (slow, about every second)  | Power on, acoustics enabled |
| Flashing green for a few seconds | Diagnostics blink initiated from GUI or API |
| Flashing green (fast, many times a second) | Sonar is in thermal shutdown |

# IO Boards
The Water Linked IO Board is the easiest solution for testing Water Linked Products like the Sonar 3D-15. They provide an interface for connecting Power and ethernet to the Sonar 3D-15. Read more about how to connect your IO Board to your Water Linked product under "IO-Interface Cards".