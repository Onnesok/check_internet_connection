# check_internet_connection using raspberry pi 4

[![License Badge](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
![Compatibility](https://img.shields.io/badge/python-3-brightgreen.svg)
![Modified](https://img.shields.io/badge/Coverage-working-orange)

## Details

This script will check if we get a response from google or not and from that we can determine if our internet connection is available or not. By checking our connection we can use it with other scripts and logics to do some interesting things.


For example in this script if we are not connected to internet then we will turn on a led; else we won't. If we lose connection even once we'll light up led even after restoring connection. By this way we can determine if our internet was ever lost while this script was running.


## clone repo

```bash
git clone https://github.com/Onnesok/check_internet_connection
```

## Instruction
First check if ```python-rpi.gpio```  is installed or not. so, for that open your terminal and write:
```bash
pip install RPi.GPIO
```
Now connect led positive part to raspberry pi ```GPIO pin 18``` and ```negative to ground.``` you're done....
After that you're good to run the script.
To run it open your terminal and write.

```bash
cd check_internet_connection
sudo python3 internet_connection_checker.py
```
<img src="https://github.com/Onnesok/check_internet_connection/blob/main/raspberry/raspberry_pi_gpio.png" alt="Avatar" clas="center" width="600" height="300" />



