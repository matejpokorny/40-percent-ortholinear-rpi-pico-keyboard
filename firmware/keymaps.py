from adafruit_hid.keycode import Keycode

MEDIA = 1
KEY = 2
INTERNAL = 3

# format is (type, code, name)
keymap_base_layer = {
    0: {
        0: (KEY, Keycode.ESCAPE),
        1: (KEY, Keycode.Q),
        2: (KEY, Keycode.W),
        3: (KEY, Keycode.E),
        4: (KEY, Keycode.R),
        5: (KEY, Keycode.T),
        6: (KEY, Keycode.Y),
        7: (KEY, Keycode.U),
        8: (KEY, Keycode.I),
        9: (KEY, Keycode.O),
        10: (KEY, Keycode.P),
        11: (KEY, Keycode.BACKSPACE)
    },
    1: {
        0: (KEY, Keycode.TAB),
        1: (KEY, Keycode.A),
        2: (KEY, Keycode.S),
        3: (KEY, Keycode.D),
        4: (KEY, Keycode.F),
        5: (KEY, Keycode.G),
        6: (KEY, Keycode.H),
        7: (KEY, Keycode.J),
        8: (KEY, Keycode.K),
        9: (KEY, Keycode.L),
        10: (KEY, Keycode.SEMICOLON),
        11: (KEY, Keycode.QUOTE),
    },
    2: {
        0: (KEY, Keycode.LEFT_SHIFT),
        1: (KEY, Keycode.Z),
        2: (KEY, Keycode.X),
        3: (KEY, Keycode.C),
        4: (KEY, Keycode.V),
        5: (KEY, Keycode.B),
        6: (KEY, Keycode.N),
        7: (KEY, Keycode.M),
        8: (KEY, Keycode.COMMA),
        9: (KEY, Keycode.PERIOD),
        10: (KEY, Keycode.FORWARD_SLASH),
        11: (KEY, Keycode.ENTER),
    },
    3: {
        0: (INTERNAL, "Fn"),
        1: (KEY, Keycode.LEFT_CONTROL),
        2: (KEY, Keycode.LEFT_ALT),
        3: (KEY, Keycode.COMMAND),
        4: (INTERNAL, "LAYER_DOWN"),
        5: (KEY, Keycode.SPACEBAR),
        6: (INTERNAL, "LAYER_UP"),
        7: (KEY, Keycode.LEFT_ARROW),
        8: (KEY, Keycode.DOWN_ARROW),
        9: (KEY, Keycode.UP_ARROW),
        10: (KEY, Keycode.RIGHT_ARROW),
    },
}
