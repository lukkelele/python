from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)
led1 = Pin(0, Pin.OUT)
led1.toggle()
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Asynchronous
# Do something, continue, do something else

c = 0   # tick counter
while True:
    if button.value():
        # LED WILL BLINK IF BUTTON HELD
        led1.toggle()
    if c == 40000:
        # TOGGLE LED AND RESET COUNTER
        led.toggle()
        c = 0
    c += 1
    






