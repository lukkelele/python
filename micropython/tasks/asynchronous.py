from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)
led1 = Pin(0, Pin.OUT)
led2 = Pin(1, Pin.OUT)
led1.toggle()
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Asynchronous
# Do something, continue, do something else
# Not scheduled
c = 0
while True:
    if button.value():
        led1.toggle()
    if c == 40000:
        led.toggle()
        c = 0
    c += 1
    
    
    
