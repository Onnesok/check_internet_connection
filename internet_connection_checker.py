import urllib.request
import RPi.GPIO as GPIO
import time

flag = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host)  # getting a ping response
            return True
        except:
            flag+= 1
            return False

    if connect() == True and flag == 0:
        GPIO.output(18, GPIO.LOW)
        print("Everything is ok 😘")
    elif connect() == False or flag != 0:
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1)
        GPIO.output(18, GPIO.HIGH)
        print("Connection broke unga bunga 🐒🐵")
    
    GPIO.cleanup()  # clean up or resets ports what I've used
