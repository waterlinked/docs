# DVL A50/A125 changelog

This page applies to DVL A50 and DVL A125.

See [Software updates](./sw-update.md) for more information on software updates.

## 2.7.1 (2026-04)

- Add water tracking support for DVL A125
- Fix DVL can get stuck in an incorrect range mode if periodic cycling is disabled

## 2.7.0 (2026-03)

- Beta release only
- Add water tracking support for DVL A50
- Update serial output command (wcs) to include water tracking velocity
- Update serial protocol to version 2.7.0
- Update JSON protocol version to v3.2
- Production optimization

## 2.6.4 (2025-06)

- Improved signal to noise performance

## 2.6.3 (2025-04)

- Adjust DHCP timing to request IP address more frequently

## 2.6.2 (2024-12)

- Add serial baud rate configuration
- Fix FOM calculation error (introduced in 2.4.0)
- Fix NTP configuration to be persistent following reboot
- Fix PD6 to output configured speed of sound instead of 1475 m/s
- Fix PD6 string to output time of validity instead of time of transmission
- Fix an issue which could cause the user interface to stop responding
- Fix chip id not correctly sent over serial
- Update serial output command (wcg) to include configuration for PD4
- Update serial protocol to version 2.6.0
- Update serial protocols 'Latest' to 'WL - Serial V2' and 'Backward compatible' to 'WL - Serial V1+V2' for clarity
- [Beta] Add PD4 protocol support

## 2.6.1 (2024-11)

- Beta release only
- Add serial baud rate configuration
- Fix FOM calculation error (introduced in 2.4.0)
- Fix NTP configuration to be persistent following reboot
- Fix PD6 to output configured speed of sound instead of 1475 m/s
- Fix PD6 string to output time of validity instead of time of transmission
- Fix an issue which could cause the user interface to stop responding
- Update serial output command (wcg) to include configuration for PD4
- Update serial protocol to version 2.6.0
- Update serial protocols 'Latest' to 'WL - Serial V2' and 'Backward compatible' to 'WL - Serial V1+V2' for clarity
- [Beta] Add PD4 protocol support"

Known issues:

- "Chip id not correctly sent over serial"

## 2.6.0 (2024-08)

- Beta release only
- Add serial baud rate configuration
- Fix NTP configuration to be persistent following reboot
- Fix PD6 to output configured speed of sound instead of 1475 m/s
- Fix PD6 string to output time of validity instead of time of transmission
- Update serial output command (wcg) to include configuration for PD4
- Update serial protocol to version 2.6.0
- Update serial protocols 'Latest' to 'WL - Serial V2' and 'Backward compatible' to 'WL - Serial V1+V2' for clarity

## 2.5.2 (2024-05)

- Improve velocity calculation
- Fix issue that causes Ethernet connectivity problems with certain switches
- Fix network configuration incorrectly showing as \"static\" after factory reset
- [Beta] Add support for PD4 protocol endpoint

Known issues:

- NTP configuration is not persistent

## 2.5.0 (2024-04)

- Beta release only
- [Beta] Add support for PD4 protocol endpoint
- Fix issue that causes Ethernet connectivity problems with certain switches

Known issues:

- NTP configuration is not persistent

## 2.4.5 (2024-01)

- Reduce boot time when ethernet is not connected
- Fix bug where altitudes <0.2m can be unstable (bug introduced in 2.4.0)
- Add PD6 BS sentence (Bottom track, ship referenced velocity)
- Add storing gyro calibration automatically when using the API
- Change gyro calibration to be single button for calibrate and store in the GUI
- Change warning messages to include a popup in the GUI
- Improve temperature shutdown warning in GUI
- Fix minor upgrade issue affecting a minority of users

Known issues:

- NTP configuration is not persistent

## 2.4.4 (2023-12)

- Fix bug where altitudes <0.2m can be unstable (bug introduced in 2.4.0)
- Add PD6 BS sentence (Bottom track, ship referenced velocity)
- Add storing gyro calibration automatically when using the API
- Change gyro calibration to be single button for calibrate and store in the GUI
- Change warning messages to include a popup in the GUI
- Improve temperature shutdown warning in GUI
- Fix minor upgrade issue affecting a minority of users

Known issues:

- NTP configuration is not persistent

## 2.4.0 (2023-06)

- Add IMU compensation for fast velocity changes
- Improve accuracy of time of validity for altitudes >10m
- Improve dead reckoning position estimation when exposed to high acceleration
- Improve accuracy of altitude
- Improve accuracy of velocity valid
- Add ability to trigger pings though API
- Add configuration for periodic cycling
- Fix dead reckoning map clears when dead reckoning is reset using the API
- Fix NTP configuration persistent over reboots
- Fix velocities containing NaN or Inf not outputted to API/GUI
- Update serial protocol version to 2.5.0
- Update JSON protocol version to v3.1

Known issues:

- NTP configuration is not persistent

## 2.3.2 (2023-02)

- Beta release only
- Add ability to trigger pings though API
- Add configuration for periodic cycling
- Fix dead reckoning map clears when dead reckoning is reset using the API
- Fix NTP configuration persistent over reboots
- Fix velocities containing NaN or Inf not outputted to API/GUI
- Update serial protocol version to 2.5.0
- Update JSON protocol version to v3.1

Known issues:

- NTP configuration is not persistent

## 2.2.1 (2022-02)

- Add PD6 protocol support
- Add system time configuration
- Update serial protocol to version 2.4.0
- Fix missing line ending in JSON protocol
- Bugfixes

Known issues:

- NTP configuration is not persistent

## 2.1.0 (2021-12)

- Add configuration over serial/TCP
- Add reset of dead reckoning over serial/TCP
- Add additional information in serial protocol (updated to 2.3.0)
- Add covariance to JSON protocol (updated to v3)
- Add timing information (time of validity, time_of_transmission)
- Improve GUI visuals
- Fix mounting rotation offset bug
- Change ethernet auto-negotiation to 10/100

## 2.0.8 (2021-08)

- Bugfixes

## 2.0.2 (2021-06)

- Add thermal shut down
- Improve velocity calculation
- Update serial protocol to version 2.2.0
- Add output of orientation angels
- Add position estimation (dead reckoning) (Beta)

## 1.6.0 (2021-03)

- Improve range

## 1.5.1 (2021-02)

- Improve velocity valid
- Improve noise immunity
- Add tranducer details in serial protocol
- Add vertical speed visualisation
- Add ping rate in GUI
- Improve web gui update rate using websockets

## 1.4.2 (2020-12)

- Fix bug in setting of fallback IP
- Add hardware revision in API

## 1.4.1 (2020-11)

- Fix instability introduced by 1.4.0

## 1.4.0 (2020-11)

- Add factory reset
- Fix TCP stops working after some time

## 1.3.7 (2020-08)

- Add generation of diagnostic report

## 1.3.5 (2020-06)

- Improve reliability of velocity data
- GUI fixes

## 1.3.3 (2020-06)

- Improve power control

## 1.3.2 (2020-04)

- Higher speed supported on longer range
- Improved velocity valid
- Increased ping rate
- Add high temperature warning
- Update serial protocol to version 2.1.0

## 1.3.1 (2020-04)

- Initial public release