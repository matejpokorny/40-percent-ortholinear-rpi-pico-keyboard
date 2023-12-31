# 3D printed 40 percent ortholinear raspberry pi pico based mechanical keyboard

This is a 3D printed 40 percent ortholinear mechanical keyboard powered by Raspberry pi pico. The repository contains
the firmware and tutorial on how to build the keyboard.

If you want to read more about the build, you can find the articles on my blog:

- [Building a custom mechanical keyboard](https://blog.matejpokorny.cz/page/2023-12-20_building-a-custom-mechanical-keyboard/)
- [Another custom mechanical keyboard](https://blog.matejpokorny.cz/page/2023-12-31_another-custom-mechanical-keyboard/)

![keyboard](./images/keyboard.jpg)

*\* When the heat inserted threaded inserts arrive, the zip ties will be replaced with screws.*

## The keymaps

The firmware currently contains 3 layers - the default layer, a control layer
and a symbol layer.

### Default layer

![default layer](./images/40-keys-base-layer.png)

### Control layer

![control layer](./images/40-keys-control-layer.png)

### Symbol layer

![symbol layer](./images/40-keys-symbol-layer.png)

## You will need

- 3D printer
- Raspberry Pi Pico
- 40 Cherry MX compatible switches
- 40 keycaps (can be also printed if you want to)
- 40 1N4148 diodes
- some wire
- soldering iron
- a lot of patience

*Tip: if you are cheap like me, you can harvest most of the parts from a cheap second hand mechanical keyboard*

## Build

1. Print the case from  `https://www.printables.com/model/345568-fortyorty`

*The printed parts in the photos are the unfinished prototype later replaced with the model mentioned above.*

![base_plate](./images/base_plate.jpg)

2. Assemble all the switches and stabilizer to the base plate

![switches](./images/switches.jpg)

*I did not use the stabilizers in the end, as the 2U spacebar works just fine without them.*

3. Solder diodes to the switches and connect them in a row as shown in picture below.

- You can also use another wire to connect the diodes in a row instead of connecting them directly.

![diodes](./images/diodes.jpg)

4. Solder wires to the rows of diodes and route them to one place

![wires](./images/wires.jpg)

5. Solder wires to the switches in columns as shown in picture below

![wires](./images/wires2.jpg)

6. Choose your GPIO pins on the pico based on your firmware in `pins.py` and solder the wires to the pico

![pico](./images/pico.jpg)

7. Carefully put the pico inside the keyboard.

- I wrapped the pico in electrical tape to prevent short circuits inside the keyboard.

*Currently in its second generation, the case still does not fit correctly, I modified the second prototype with
side cutters and the case works with zip ties. If I get around to another model and print, I will update this repo.*

## Flashing the firmware

1. Install circutpython on your pico
2. Copy the `adafruit_hid` folder to the `lib` folder on pico.
3. Modify your keymaps in `keymaps.py`
4. Copy the `keymaps.py`, `pins.py` and `code.py` files to the pico.
5. When you are done testing your firmware, you can copy the file called `boot.py` to your pico to prevent it appearing
   as a usb drive on your pc.

## Sources

- Firmware is based on this tutorial: https://learn.adafruit.com/diy-pico-mechanical-keyboard-with-fritzing-circuitpython/code-the-pico-keyboard
- I ended up using this model for the keyboard body instead creating my own: https://www.printables.com/model/345568-fortyorty
