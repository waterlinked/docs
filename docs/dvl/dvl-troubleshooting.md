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
1. For LED status, see [LED Signals](../dvl/interfaces.md#led-signals).

### Wiring 
1. Check that you have wired your DVL correctly, see [Wiring interface](../interfaces#wiring-interface).
    - 1.1 If you have a custom connector you need to ask the supplier for the correct drawings.
2. Check for damages along the cable and that there are good connection where you have terminated your DVL.
3. Check for short between Negative/Ground and Positive (10-30V).

### Environmental Check
1. The Line of sight should be clear of any obstacles including walls, see [Line of sight](../dvl-a50#line-of-sight).
    - 1.1 One easy way to make sure the Line of sight is clear from any walls is to observe that all beam shows approximately the same distance to the bottom. If some of the beams are flickering or showing another distance it might pick up a reflection from a wall or some other obstacle in the line of sight. Obstacle free radius from the DVL to the wall depending on the distance to the bottom can be calculated with this formula: **Obstacle free radius** = tan(32.5°) × **distance from DVL to bottom**. 
2. If testing in a pool, tank or bucket it should **not** be made out of a **polished metal** or very clean surfaces. This can introduce more noise and make it harder for the DVL to get a bottom lock.
3. Check that there are no motors, echo sunders, pumps, running house. This can create noise in the same frequency as the DVL and have an impact on the acoustic signal.
4. Make sure the environment is not acting on the DVL in a way that makes it pitch and yaw (waves). That will send the acoustic signal in many directions making it hard to achieve a bottom lock.    

## Thermal shutdown - Does the DVL look like it is constantly powering on and off
The DVL has a thermal shutdown mechanism to avoid damage. It will issue a warning before shutting down at 55℃. Once it cools below 50℃, it automatically restarts. If the overheating issue is not addressed, it may repeat this shutdown/restart cycle.

1. Is the DVL in water? If not it will overheat and enter a shutdown/restart cycle.

<!-- ### Obstacle free radius calculator

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        label {
            font-size: 1.2em;
        }

        input[type="number"] {
            padding: 12px;
            width: 150px;
            font-size: 1.2em;
            margin-right: 10px;
            border: 2px solid #4CAF50;
            border-radius: 5px;
            box-shadow: 0px 0px 5px rgba(0, 0, 0, 0.2);
            background-color: #f0f0f0;
        }

        input[type="number"]:focus {
            background-color: #ffffff;
            border-color: #45a049;
        }

        input[type="button"] {
            background-color: #4CAF50;
            color: white;
            border: none;
            padding: 10px 20px;
            font-size: 1em;
            cursor: pointer;
            border-radius: 5px;
        }

        input[type="button"]:hover {
            background-color: #45a049;
        }

        p#result {
            margin-top: 20px;
            font-size: 1.2em;
            color: #333;
        }

        p#error {
            color: red;
            margin-top: 10px;
        }
    </style>
</head>
<body>

    <form>
        <label for="rangeInput">Altitude (0.05 - 125 meters):</label>
        <input type="number" id="rangeInput" name="rangeInput" min="0.05" max="125" step="0.01" required>
        <input type="button" value="Click here to calculate!" onclick="calculateSafetyDistance()">
    </form>

    <p id="result"></p>
    <p id="error"></p>

    <script>
    function calculateSafetyDistance() {
        const rangeInput = document.getElementById('rangeInput');
        const range = parseFloat(rangeInput.value);
        const resultElement = document.getElementById('result');
        const errorElement = document.getElementById('error');
        
        // Clear previous results and error messages
        resultElement.innerHTML = '';
        errorElement.innerHTML = '';
        
        if (range >= 0.05 && range <= 125) {
            const safetyDistance = Math.tan(32.5 * Math.PI / 180) * range;
            resultElement.innerHTML = 'Obstacle free radius: ' + safetyDistance.toFixed(2) + ' meters';
        } else {
            errorElement.innerHTML = 'Please enter a valid range between 0.05 and 125 meters.';
        }
    }
    </script>

</body>
</html> -->


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
