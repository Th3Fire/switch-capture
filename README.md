# switch-capture
Press switch for control Raspberry pi capture photo

## Device
* USB Web Cam 
* Raspberry Pi
* ET-TEST 10P/INP

## Install package
```bash
sudo apt-get install python-opencv
```

## Prepair before run program
1.Connect jumper wire look at table

| GPIO raspberry pi (pin)| ET-TEST 10P/INP (pin) |
|:----------------------:|:---------------------:|
|           16           |           1           |
|           2 (5V)       |           10 (5V)     |
|           6 (GND)      |           9 (GND)    |


![GPIO](GPIO.png?raw=true "GPIO")

credit image http://grimbodroid.blogspot.com/2012/08/following-directions-on-these-pages-1.html

2.Connect USB Web Cam to Raspberry Pi

## Run
Please ensure your web cam must not run on another service.
```bash
sudo python SW_capture.py 
```

```Note``` press switch for capture photo.

