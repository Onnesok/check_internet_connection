import urllib.request
import RPi.GPIO as GPIO
import time
import timee


GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    def connect(host='http://google.com'):
        try:
            urllib.request.urlopen(host)  # getting a ping response
            return True
        except:
            return False

    if connect() == True:
        GPIO.output(18, GPIO.LOW)
        print("Everything is ok 😘")
        time.sleep(5)
    elif connect() == False:
        print("Connection broke unga bunga 🐒🐵")
        break

GPIO.output(18, GPIO.HIGH)
print("connection was lost")

print("Inturrupt time = ", timee)


    
