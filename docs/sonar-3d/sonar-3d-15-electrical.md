# Wiring Sonar 3D-15

The tables below shows the pinning of the Sonar 3D-15 interface.

| Interface         | Color         |
| :-----------------| :-------------|
| Negative/Ground   | Black          <span class="swatch c-black"></span>|
| Positive (10-30V) | Red            <span class="swatch c-red"></span>|
| ETH RX+           | Green/White    <span class="swatch c-green-white"></span>|
| ETH RX-           | Green          <span class="swatch c-green"></span>|
| ETH TX-           | Orange         <span class="swatch c-orange"></span>|
| ETH TX+           | Orange/White   <span class="swatch c-orange-white"></span>|
| Shielded wire     | Naked (silver) <span class="swatch c-silver"></span>| 

# IO Boards
The Water Linked IO Board is the easiest solution for testing Water Linked Products like the Sonar 3D-15. They provide an interface for connecting Power and ethernet to the Sonar 3D-15. Read more about how to connect your IO Board to your Water Linked product under "IO-Interface Cards".

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
