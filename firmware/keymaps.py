from adafruit_hid.keycode import Keycode

MEDIA = 1
KEY = 2
INTERNAL = 3

# format is (type, code, name)
keymap_base_layer = {
    0: {
        0: (KEY, Keycode.ESCAPE, "Esc"),
        1: (KEY, Keycode.Q, "Q"),
        2: (KEY, Keycode.W, "W"),
        3: (KEY, Keycode.E, "E"),
        4: (KEY, Keycode.R, "R"),
        5: (KEY, Keycode.T, "T"),
        6: (KEY, Keycode.Y, "Y"),
        7: (KEY, Keycode.U, "U"),
        8: (KEY, Keycode.I, "I"),
        9: (KEY, Keycode.O, "O"),
        10: (KEY, Keycode.P, "P"),
        11: (KEY, Keycode.BACKSPACE, "Backspace"),
    },
    1: {
        0: (KEY, Keycode.TAB, "Tab"),
        1: (KEY, Keycode.A, "A"),
        2: (KEY, Keycode.S, "S"),
        3: (KEY, Keycode.D, "D"),
        4: (KEY, Keycode.F  , "F"),
        5: (KEY, Keycode.G, "G"),
        6: (KEY, Keycode.H, "H"),
        7: (KEY, Keycode.J, "J"),
        8: (KEY, Keycode.K, "K"),
        9: (KEY, Keycode.L, "L"),
        10: (KEY, Keycode.SEMICOLON, "Semicolon"),
        11: (KEY, Keycode.QUOTE, "Quote"),
    },
    2: {
        0: (KEY, Keycode.LEFT_SHIFT, "Shift"),
        1: (KEY, Keycode.Z, "Z"),
        2: (KEY, Keycode.X, "X"),
        3: (KEY, Keycode.C, "C"),
        4: (KEY, Keycode.V, "V"),
        5: (KEY, Keycode.B, "B"),
        6: (KEY, Keycode.N, "N"),
        7: (KEY, Keycode.M, "M"),
        8: (KEY, Keycode.COMMA, "Comma"),
        9: (KEY, Keycode.PERIOD, "Period"),
        10: (KEY, Keycode.FORWARD_SLASH, "Forward Slash"),
        11: (KEY, Keycode.ENTER, "Enter"),
    },
    3: {
        0: (INTERNAL, "Fn", "Fn"),
        1: (KEY, Keycode.LEFT_CONTROL, "Ctrl"),
        2: (KEY, Keycode.LEFT_ALT, "Alt"),
        3: (KEY, Keycode.COMMAND, "Cmd"),
        4: (INTERNAL, "LAYER_DOWN", "Layer Down"),
        5: (KEY, Keycode.SPACEBAR, "Space"),
        6: (INTERNAL, "LAYER_UP", "Layer Up"),
        7: (KEY, Keycode.LEFT_ARROW, "Left Arrow"),
        8: (KEY, Keycode.DOWN_ARROW, "Down Arrow"),
        9: (KEY, Keycode.UP_ARROW, "Up Arrow"),
        10: (KEY, Keycode.RIGHT_ARROW, "Right Arrow"),
    },
}
