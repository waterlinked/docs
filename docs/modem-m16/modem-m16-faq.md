# Modem M16 FAQ

Below are some frequently asked questions about the Modem M16. Click on a question in the table of contents to the right or simply scroll down to read the FAQs.

---

## 1. Can the M16 modem measure the range/distance between two modems?

No, the modem's uses an unsynchronized method of sending data meaning that an time of flight estimate would give large errors in the range estimations. The acoustic signal is not synced but known to be within some time frame of 25ms. 

However if looking at the [Signal to noise ratio (SNR)](modem-m16-uart-interface.md#packet-structure-of-the-diagnostic-report) you can use it to indicate that the distance between the modems is fare or close. For example would a grater SNR (better signal) indicate that it is most likely close as it has so good signal.  

---

## 2. Do the modem retransmit data packets?

No, the modem do not retransmit data packets. If you need a more robust data link to ensure that packets are received you will have to implement that in your application/driver.  

---