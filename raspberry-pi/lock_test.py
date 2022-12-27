import time
# GPIO initialization
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED config
lock_pin = 21
GPIO.setup(lock_pin, GPIO.OUT)

GPIO.output(lock_pin,1)
time.sleep(1)
GPIO.output(lock_pin,0)