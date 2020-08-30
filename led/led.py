import RPi.GPIO as GPIO
import time

myLED = 17

GPIO.setmode(GPIO.BCM)
GPIO.setup(myLED, GPIO.OUT)
while False:
    GPIO.output(myLED, True)
    time.sleep(1)
    GPIO.output(myLED, False)
    time.sleep(0.5)
    
GPIO.output(myLED, False)