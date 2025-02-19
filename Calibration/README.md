# CALIBRATION 
FeatherWeight (FW) Devices: 
MR-devices: Tom and Jerry 
TMS/EEG-devices: Bob and Patrick 

MR Devices are stored near the scanner. Tom is the primary used, Jerry is kept as back-up. 
TMS/EEG-devices are stored in TMS/EEG labs. Bob is primarly used, Patrick is kept as back-up. 

### HOW TO CALIBRATE
#### Step 1: Software setup
1) Download Arduino 
2) ... 
#### Step 2: Adjust gain function for each hand in both modes. 
3) For Game-mode (GM): Put approx. 2625g on the sensor, and monitor the ADC output, then turn (counter-clockwise I think) the gain function screw (on the amplifier for the relevant hand, with the number 205 written on it) to increase the ADC until it reaches plateau, which should be around 950-1022.  
4) For Max-mode (MM): Put approx. 14500 gram on the sensor, and turn the gain screw (has a number like 104 written on it) untill it reaches plateau. 
#### Step 3: Calibration 
5) Slowly add weights, read ADC output after 2 sec (time is important in this protokol) and note down in Excel.  
6) Note, weights should be added to reach as close to 1022 as possible, there should be an ADC measure reaching 1015-1022 for the calibration calculations. 
#### Step 4: Calculating Calibration files 
7) Excel



# HOW TO UPDATE ARDUINO CODE: 
The arduino code file is saved as a .ino file in the FWkode folder (necessary structure, do not change). 
The code can be updated and pushed to the FW box using the Arduino interface (install if not already). 

1) open the .ino file. 
2) Make sure to define the port where FW is connected to the computer, by 1) selecting "Tools" --> Choose "Board" as "Arduino Nano" and then 2) "Tools" --> Choose "Port" as the relevant port. If you are unsure of which port you have connected the device in, go to Windows "Device Manager", find and unfold "Ports" and look for a name similar to "USB Serial Port" or sometimes "USB-SERIAL". 
3) In the left upper corner of the Arduino interface, there is an arrow pointing right. Click to upload the code. 
4) Note the update down into the README.md file, to keep track of changes, why they were made and which FW devices were updated.


### LOG OF UPDATES: 
2022 - November : Changing parameter double alpha = 0.1, from 0.01. The modifies the smoothing of the running average. Changes pushed to Bob, Patrick, Jerry and Tom.  
2022 - August : All FW devices delivered by René Stennow Gotfredsen with the code file taking point in the Applejack file created by Kristoffer Hougaard Madsen. 



