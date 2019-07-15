from gpiozero import LED
import time
from time import sleep

def firstLed():
    led = LED(18)

    led.on()
    time.sleep(10)
    led.off()

def secondLed():
    led = LED(18)

    while True:
        led.on()
        sleep(1)
        led.off()
        sleep(1)
secondLed()