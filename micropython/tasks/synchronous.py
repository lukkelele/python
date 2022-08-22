from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)
led1 = Pin(0, Pin.OUT)
led1.toggle()
button = Pin(14, Pin.IN, Pin.PULL_DOWN)


#def tick(timer):
#    led.toggle()
#Timer().init(freq=2, mode=Timer.PERIODIC, callback=tick)

toggled = False
c = 0
while True:
    while button.value():
        if toggled == False:
            led1.toggle()
        toggled = True
        time.sleep(0.30)
    toggled = False
    if c == 40000:
        led.toggle()
        c = 0
    c += 1
