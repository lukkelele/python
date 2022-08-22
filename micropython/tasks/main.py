from machine import Pin, Timer
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

def tick(timer):
    led.toggle()

Timer().init(freq=50, mode=Timer.PERIODIC, callback=Tick)

while True:
    if button.value():
        led.toggle()
        time.sleep(0.50)

