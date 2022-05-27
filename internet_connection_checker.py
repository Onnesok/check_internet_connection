import urllib.request
import RPi.GPIO as GPIO
import time
from datetime import datetime

timeout = 5
now = datetime.now()

current_time = now.strftime("%H:%M:%S")

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    def connect(host='https://google.com'):
        try:
            urllib.request.urlopen(host, timeout = timeout)  # getting a ping response
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

print("Inturrupt time = ", current_time)



    
