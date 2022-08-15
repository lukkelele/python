from machine import Pin
import time


while True:
    p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
    p0.on()                 # set pin to "on" (high) level
    time.sleep(1)
    p0.off()                # set pin to "off" (low) level


