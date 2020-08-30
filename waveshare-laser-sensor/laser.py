import RPi.GPIO as GPIO
import time

myLASER=21
GPIO.setmode(GPIO.BCM)
GPIO.setup(myLASER, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
	input_state = GPIO.input(myLASER)
	print(input_state)
	time.sleep(0.2)

