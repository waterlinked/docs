# Dead reckoning

## Introduction

All our DVLs run a dead-reckoning algorithm that estimates the orientation and position of the DVL. This uses the velocities calculated by the DVL and its integrated IMU/AHRS.

## Starting dead reckoning

Reset dead reckoning before using the local position estimate.

For DVL A50/A125:

1. Calibrate the gyroscope by pressing *More -> Calibrate gyro* in the [web GUI](dvl-a50_a125-gui.md) while the DVL is stationary.
2. Click the **Reset** button ![](../img/dvl_gui_icon_reset.png) in the [dashboard](dvl-a50_a125-gui.md#dashboard-live-data), or send a reset command over the [TCP JSON API](dvl-json-protocol.md#reset-dead-reckoning) or [serial protocol](dvl-serial-protocol.md#reset-dead-reckoning-wcr).

For DVL A100/A250, gyro calibration is not needed. Reset commands over the [TCP JSON API](dvl-a250_a100-json-protocol.md#reset-dead-reckoning) or [serial protocol](dvl-a250_a100-serial-protocol.md#reset-dead-reckoning-wcr) are included for backward compatibility and do not affect dead reckoning on DVL A100/A250.

## Frame

The position, speed, roll, pitch, and yaw angles output by the dead-reckoning algorithm are relative to the frame defined at time zero: the time of the last reset, or startup if no reset has been performed. This frame is defined by the axes of the [vehicle frame](axes.md#vehicle-frame).

## Speed and position

The speed and position of the DVL are calculated by integrating its acceleration, corrected by the velocity it calculates with acoustic signal processing. A Kalman filter is used; the [roll, pitch, and yaw angles](#orientation) output by the DVL are also part of the input.

When the DVL cannot determine velocity, speed and position are predicted only from acceleration. This will result in large errors, indicated by an increase in the figure of merit (FOM), which is an estimated standard deviation of the position in the X-Y plane.

!!! note
    When the DVL is powered on in the air, its position will drift significantly. This should be ignored, and dead reckoning should be [started](#starting-dead-reckoning) in water when ready.

The position of the DVL can be viewed in the web GUI dashboard or fetched by API:

* [DVL A50/A125 web GUI dashboard](dvl-a50_a125-gui.md#dashboard-live-data)
* [DVL A100/A250 web GUI dashboard](dvl-a250_a100-gui.md#velocity-and-navigation)
* [DVL A50/A125 TCP JSON API](dvl-json-protocol.md#dead-reckoning-report)
* [DVL A100/A250 TCP JSON API](dvl-a250_a100-json-protocol.md#dead-reckoning-report)

## Orientation

The orientation of the DVL is based on the accelerometer and gyroscope measurements from its IMU/AHRS. The orientation is represented by roll, pitch, and yaw angles, and can be viewed in the web GUI dashboard or fetched by API.

- Roll is a rotation around the X axis of the DVL
- Pitch is a rotation around the Y axis of the DVL
- Yaw is a rotation around the Z axis of the DVL

For orientation to function correctly, the DVL must be deployed in accordance with its [axis conventions](axes.md).

!!! note
    A small tilt in the DVL mounting, though it will result in almost no position error with respect to the X and Y axes, may lead to a significant error with respect to the Z axis. This change will be a projection of the true horizontal position onto the Z axis. For example, when the DVL is mounted with 5&#176; tilt and the horizontal displacement of the DVL is 100 m since the last reset, the total displayed distance in the X, Y plane will be 99.6 m, and the Z position will be &pm;9 m.

When dead reckoning is [reset](#starting-dead-reckoning), the roll, pitch, and yaw angles are set to zero.

## Yaw drift

!!! note
    For DVL A50/A125, yaw drift can be decreased to 0.1-0.3&#176; per minute by [calibration](#starting-dead-reckoning) of the gyroscope. For DVL A100/A250, gyro calibration is not needed.
