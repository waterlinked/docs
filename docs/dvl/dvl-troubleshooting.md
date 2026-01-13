# DVL Troubleshooting

## Is my DVL faulty?

Below is a small list to check if your DVL is not performing as expected or you are experiencing any issues. It starts with the basic before moving on to more advanced troubleshooting. When you come to the point of failure or if the troubleshooting do not help, please submit a support ticket to our support team through our [Support portal](https://waterlinked.com/support). Please write what you are experiencing and how you tested/used the DVL when you experienced the issue. 

In the Support Portal please describe the test environment or test setup you have used and how the DVL is mounted. If possible, open the DVL GUI and go to Diagnostic Log in the left menu. Press the Create Diagnostic Report button. This will automatically record a log file that you can download to your computer. Please add the [Diagnostic reports](gui/diagnostic-report.md) and pictures of the test setup in the support portal. This will help our support team greatly! 

If the troubleshooting guide do not help, please check out [FAQ DVL](../dvl/faq.md)!  

### Check if DVL is powered
1. Put the DVL under water and power it on with an adequate power supply.
    * Does the DVL pull any current? Expected current consumption: Approximate average 260mA at 18V
    * Does the LED turn on?

### LED
1. For LED status, see [LED Signals](interfaces.md#led-signals).

### Wiring 
1. Check that you have wired your DVL correctly, see [Wiring interface](interfaces.md#wiring-interface).
    - 1.1 If you have a custom connector you need to ask the supplier for the correct drawings.
2. Check for damages along the cable and that there are good connection where you have terminated your DVL.
3. Check for short between Negative/Ground and Positive (10-30V).

### Environmental Check
1. The Line of sight should be clear of any obstacles including walls, see [Line of sight](dvl-a50.md#line-of-sight).
    - 1.1 One easy way to make sure the Line of sight is clear from any walls is to observe that all beam shows approximately the same distance to the bottom. If some of the beams are flickering or showing another distance it might pick up a reflection from a wall or some other obstacle in the line of sight. Obstacle free radius from the DVL to the wall depending on the distance to the bottom can be calculated with this formula: **Obstacle free radius** = tan(32.5°) × **distance from DVL to bottom**. 
2. If testing in a pool, tank or bucket it should **not** be made out of a **polished metal** or very clean surfaces. This can introduce more noise and make it harder for the DVL to get a bottom lock.
3. Check that there are no motors, echo sunders, pumps, running hose. This can create noise in the same frequency as the DVL and have an impact on the acoustic signals.
4. Make sure the environment is not acting on the DVL in a way that makes it pitch and yaw (waves). That will send the acoustic signals in many directions making it hard to achieve a bottom lock.    

## Thermal Shutdown
The DVL has a thermal shutdown mechanism to avoid damage. It will issue a warning before shutting down at 55℃. Once it cools below 50℃, it automatically restarts. If the overheating issue is not addressed, it may repeat this shutdown/restart cycle.

1. Is the DVL in water? If not it will overheat and enter a shutdown/restart cycle.

## GUI
1. Connect your DVL yo Ethernet by following the Network documentation, see [Setup Network](networking.md#networking). Use the [Fallback IP](networking.md#fallback-ip) if you are struggling. 

2. You are able to access and see the Dashboard like displayed in our [Web Demo](https://dvl.demo.waterlinked.com/#/diagnostic).

3. Check that you have the latest software, see [Software Updates](sw-update.md#software-updates)


## Collecting data
Assuming you have checked the above and that your testing environment will not affect the performance of the DVL, you can now start collecting data!

1. Go into the [Diagnostic report](gui/diagnostic-report.md) and collect data. Fill the description with relevant information of the test environment and observed issue.
2. Take picture of the test environment and how DVL is mounted to bracket or ROV.
3. If there are known issues under certain conditions/setup please perform these tests as well and collect diagnostic reports.  
4. Open a ticker through our support portal [Support portal](https://waterlinked.com/support) where you upload the diagnostic reports, pictures with a description of your issue. 
