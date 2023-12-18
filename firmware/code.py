import time
from digitalio import DigitalInOut, Direction, Pull
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.consumer_control import ConsumerControl

from keymaps import keymap, KEY, MEDIA, LAYER
from pins import row_pins, col_pins

kbd = Keyboard(usb_hid.devices)
cc = ConsumerControl(usb_hid.devices)

input_rows = []
for i in range(len(row_pins)):
    row = DigitalInOut(row_pins[i])
    row.direction = Direction.INPUT
    row.pull = Pull.DOWN
    input_rows.append(row)

output_cols = []
for i in range(len(col_pins)):
    col = DigitalInOut(col_pins[i])
    col.direction = Direction.OUTPUT
    output_cols.append(col)

switch_state = {
    0: [0, 0, 0, 0],
    1: [0, 0, 0, 0],
    2: [0, 0, 0, 0],
    3: [0, 0, 0, 0],
    4: [0, 0, 0, 0],
    5: [0, 0, 0, 0],
    6: [0, 0, 0, 0],
    7: [0, 0, 0, 0],
    8: [0, 0, 0, 0],
    9: [0, 0, 0, 0],
    10: [0, 0, 0, 0],
    11: [0, 0, 0, 0],
}

active_layer = 0

def press_key(col, button):
    print(f"Pressed col {col} and row {button} - {keymap[active_layer][button][col][2]}")
    try:
        if keymap[active_layer][button][col][0] == KEY:
            kbd.press(keymap[active_layer][button][col][1])
        elif keymap[active_layer][button][col][0] == MEDIA:
            cc.send(keymap[active_layer][button][col][1])
        elif keymap[active_layer][button][col][0] == LAYER:
            active_layer = keymap[active_layer][button][col][1]
            print(f"Switching to layer {active_layer}")
    except ValueError:  # deals w six key limit
        pass
    switch_state[col][button] = 1


def release_key(col, button):
    print(f"Released col {col} and row {button} - {keymap[active_layer][button][col][2]}")
    try:
        if keymap[active_layer][button][col][0] == KEY:
            kbd.release(keymap[active_layer][button][col][1])
            pass
        if keymap[active_layer][button][col][0] == LAYER:
            active_layer = 0
            print(f"Switching to layer {active_layer}")

    except ValueError:
        pass
    switch_state[col][button] = 0


while True:
    # activate 1 column at a time
    for col in range(len(col_pins)):
        output_cols[col].value = True
        # wait for output to settle
        time.sleep(0.005)

        # read buttons in column
        for button in range(len(row_pins)):
            if switch_state[col][button] == 0:
                if input_rows[button].value:
                    press_key(col, button)

            if switch_state[col][button] == 1:
                if not input_rows[button].value:
                    release_key(col, button)

        # deactivate column
        output_cols[col].value = False
