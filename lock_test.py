import time
# GPIO initialization
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED config
lock_pin = 21
GPIO.setup(lock_pin, GPIO.OUT)

while True:
    GPIO.output(lock_pin,1)
    sleep(3)
    GPIO.output(lock_pin,0)
    sleep(5)