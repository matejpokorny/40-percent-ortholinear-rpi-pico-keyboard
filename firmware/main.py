from machine import Pin
from time import sleep

led = Pin(14, Pin.OUT)
push_button = Pin(13, Pin.IN)

while True:
    logic_level = push_button.value()
    if logic_level == True:
        led.value(1)
    else:
        led.value(0)
    sleep(0.1)