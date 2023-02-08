# https://www.deviceplus.com/raspberry-pi/integrate-rfid-module-raspberry-pi/
# https://pimylifeup.com/raspberry-pi-rfid-rc522/
# https://www.circuitbasics.com/what-is-an-rfid-reader-writer/

# Scans the RFID and returns the UID of the RFID

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def scan():
    id, text = reader.read()
    print(id)
    print(text)
    GPIO.cleanup()
    return id
