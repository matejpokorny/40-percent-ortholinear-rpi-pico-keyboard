from machine import Pin
from time import sleep

push_button = Pin(15, Pin.IN) # pin 20 on pico, GPIO 15

while True:
    logic_level = push_button.value()
    if logic_level == True:
        print("Button pressed")
    else:
        pass
    sleep(0.1)