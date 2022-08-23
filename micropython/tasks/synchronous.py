from machine import Pin
import time

led = Pin(15, Pin.OUT)
led1 = Pin(0, Pin.OUT)
led1.toggle()
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

# Synchronous
# Do one thing, wait until done, then move on

toggled = False     # toggle flag
c = 0
while True:
    while button.value():
        # TOGGLE ONCE
        if toggled == False:
            led1.toggle()
        toggled = True
        time.sleep(0.10)
    # REMOVE TOGGLE FLAG
    toggled = False
    if c == 40000:
        # TOGGLE LED AND RESET COUNTER
        led.toggle()
        c = 0
    c += 1




