# How to implement external GPS compass data in the UGPS
In very dynamic conditions with rapid changes in angles, the IMU will drift too much to provide sufficient heading accuracy. In this case it is recommended to implement an external compass to provide updated heading information.

## Which compass to use
If the UGPS is permanently installed on a boat, the simple solution is to use the boats compass, if it provides the possibility to output NMEA data. Otherwise it is possible to use any portable compass that provide NMEA0185 or NMEA2000 information.

## External compass on the UGPS:
To use an external compass with the UGPS it has to be integrated in the software on your computer. As for now there are no direct hardware connection available.
The needed firmware can be installed by following this procedure:

!!! Note
This is valid only for compasses that provides NMEA0183

- Go to: https://github.com/waterlinked/ugps-nmea-go under “Readme” and “Installation” and “Download the application”, choose v.1.8.0 
- Download the .zip-file.
- In windows: run the file. Follow the instructions you get. (It is advisable to create a folder on your computer specifically for this configuration)
- In linux, in the directory you saved the file in: use chmod +x <filename> (It is advisable to create a folder on your computer specifically for this configuration)
- Go back to the “ugps-nmea-go” repository and download the file: “config-example.yml”, save it in the same folder as the application and rename it to config.yml.
- Open the file and make sure you have the correct com or tty-port on “device” and the correct position sentence. If you are uncertain, check the gps manual. The baudrate is usually 9600. If you still are uncertain of the baudrate, open the device with a serial program like putty or minicom and connect to the compass. Try different baudrates and see which one that gives you sensible data. -Save the changes you made to the config.yml file.
- Connect the UGPS topside to your computer and turn it on.
- Run the application from a terminal.
To do this, navigate to the correct folder with “cd <folder>/<your-nmea-folder>” (in your terminal) and run the application with ./nmea_ugps_linux_amd64 or ./nmea_ugps_windows_amd64.exe
- In the UGPS GUI, go to Configuration -> Topside setup and choose “external” compass.

!!! Note
The UGPS do still need GPS lock to synchronize time with the locator, but as long as the UGPS has access to a GPS signal (is outside) you do not have to worry about it. 

##If you have an NMEA2000 GPS compass
In this case you will need an NMEA0183 to NMEA2000 converter.
Below are link's to converters that can be used for the purpose:

https://www.mrad.co.za/wp-content/uploads/2019/09/ngw-1-user-manual.pdf

https://actisense.com/products/nmea-2000-gateway-ngw-1/



