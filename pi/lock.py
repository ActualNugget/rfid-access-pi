import time
# GPIO initialization
import RPi.GPIO as GPIO


def open(lock_pin, led_pin):
    GPIO.setmode(GPIO.BOARD)
    # GPIO.setwarnings(False)
    GPIO.setup(lock_pin, GPIO.OUT)
    GPIO.output(lock_pin,1)
    GPIO.output(led_pin,1)
    time.sleep(1)
    GPIO.output(lock_pin,0)
    GPIO.output(led_pin,0)

def led(led_pin):
    GPIO.output(led_pin,1)
    time.sleep(1)
    GPIO.output(led_pin,0)