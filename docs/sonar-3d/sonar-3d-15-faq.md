# Sonar 3D-15 FAQ
Below are some frequently asked questions about the Sonar 3D-15. Click on a question in the table of content to the right or simply scroll down to read the FAQ's. 

---

## 1. What is the maximum depth rating of the Sonar 3D-15?
The Sonar 3D-15 is rated for depths up to 300 m, ensuring reliable performance in a wide range of underwater environments.

---

## 2. What kind of power supply is recommended?
We recommend using a power supply capable of delivering 60 W peak (surge) at 10–30 V. For optimal performance, a 20 V or higher supply is preferred.

---

## 3. Does the Sonar 3D-15 have a thermal shutdown mechanism?
Yes. The Sonar 3D-15 includes an internal thermal shutdown to prevent damage to its electronics. You will receive a warning in both the GUI and the API if the internal temperature reaches 55 °C, indicating that the unit will shut down the acoustic at 60 °C if it continues to heat up. This will cause you to loose the sonar image. 

**Recommended action:**  
- Once you see the overheat warning (55 °C), check that the Sonar is in water or cooled in any other way.   
- If the temperature reaches 70 °C, the Sonar 3D-15 will shut down to prevent permanent damage and not restart before it reaches 65 °C again, and it must reach 55 °C before you will get the sonar image back. 

---

## 4. What are the default network settings of the Sonar 3D-15?
By default, the Sonar 3D-15 uses **DHCP** to request an address. If no DHCP server answers, it is always accessible on the fallback IP `192.168.194.96`. For a step-by-step guide to using the fallback IP, mDNS, or setting a static IP in the GUI, see [Sonar 3D-15 Networking](sonar-3d-15-networking.md).

---

## 5. Is any software installation required to operate the Sonar 3D-15?
No, there is no software installation needed. Once connected and powered on, you can access the Sonar 3D-15’s built-in GUI through a standard web browser. This allows you to operate and configure the sonar without installing any additional software.

---

## 6. The performance is not as expected?
If the performance is not as expected and you can not find a solution in this documentation, please create a [diagnostic log](../sonar-3d-15-diagnostic-log) with your Sonar 3D-15 and submit a [support ticket](https://waterlinked.com/support) with the Sonar 3D diagnostic log file attached. 

---

## 7. How should I maintain the Sonar 3D-15?
After operating in seawater, brackish water, chlorinated pools, or any medium other than freshwater, rinse the unit thoroughly with fresh water to remove residues and salt deposits. Once dry, wipe the exterior with a clean, dry cloth. Avoid solvents or abrasive cleaners.

---

## 8. What if I need a custom integration?
For advanced integrations, you can use the Sonar 3D-15’s API to develop custom solutions. This requires some programming knowledge but enables control and automation of the Sonar 3D-15’s functionality from your custom system.
