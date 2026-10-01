# Underwater GPS FAQ

Below are some frequently asked questions about the Underwater GPS. Click on a question in the table of content to the right or simply scroll down to read the FAQ's. 

---

## 1. The heading is drifting rapidly
In dynamic environments, such as in a boat at sea with rapid change of angles, the heading has to be set frequently in [Settings](../underwater-gps/interface/ugps-gui.md#settings). In harsh wether this has to be done up to every minute. In such conditions it is advised to use an external compass to get accurate positioning data from the UGPS. If the UGPS is permanently installed on one boat, the boats compass can be used. Otherwise an [external portable compass](../underwater-gps/integration/external-gps.md) can be implemented.

---


## 2. Can I set the speed of sound?
Yes, If you have the R300 version you can set the speed of sound in the "settings" menu in the GUI.

!!! Note
    If you have the R100 version you can't change the speed of sound. The option to change the speed of sound is still present, but you will get an error message saying "Bad request"


---

## 3. My UGPS system is not performing well
If your UGPS system does not perform as expected, you should contact Waterlinkes technical support team through the [support portal](https://waterlinked.com/support) in Waterlinked's home pages on the internet.

To help the support team analyzing your systems behaviour, you should record a diagnostic logfile. This can easily be done by opening the Diagnostics window in the UGPS GUI. At the bottom of the page there is an option that allows you to record a diagnostic report. The file should preferably be recorded in the moment or circumstance as your system is failing. Attach the diagnostic report file you recorded to your request. The file contains valuable information that will help the support team analyse your system. 


!!! Note
    The logfile must be downloaded to your computer and sent to customer support as an attachment.


---

## 4. My UGPS Topside is newer, but R2/R3 are fitted and I measure 12 V on the Locator connector. Should I remove them?
No. This question concerns the "Modify Interface Electronics" step of the [BlueROV2 Locator-A1 integration guide](../underwater-gps/integration/bluerov-integration-a1.md#modify-interface-electronics).

On the updated Interface Electronics, the positions R2 and R3 are populated with small inductors instead of the original 0 ohm resistors. The PCB designators still read R2 and R3. The inductors reduce the loading of the PLC signal by the 12 V supply, but they still provide a DC connection. Approximately 12 V DC between pins 1 and 2 of the "Locator" bulkhead connector is therefore expected on a powered unit with the updated configuration.

Populated R2/R3 positions and a 12 V reading are both consistent with the updated design. Neither observation by itself indicates the original configuration or justifies removing the components. The documented integration with the BlueROV2 Integration Kit works with the updated configuration as delivered.

If you cannot identify the hardware configuration of your unit with certainty, contact [Water Linked Support](https://waterlinked.com/support) with the serial number of your UGPS Topside before modifying the board.

---
