from adafruit_hid.keycode import Keycode

MEDIA = 1
KEY = 2
LAYER = 3
NONE = 3

EMPTY_ROW = {
    0: (NONE, 0, "None"),
    1: (NONE, 0, "None"),
    2: (NONE, 0, "None"),
    3: (NONE, 0, "None"),
    4: (NONE, 0, "None"),
    5: (NONE, 0, "None"),
    6: (NONE, 0, "None"),
    7: (NONE, 0, "None"),
    8: (NONE, 0, "None"),
    9: (NONE, 0, "None"),
}

# format is [layer_number][row]{[(type, code, name)]}
keymap = [
    # layer 0
    {
        0: {
            9: (KEY, Keycode.Q, "Q"),
            8: (KEY, Keycode.W, "W"),
            7: (KEY, Keycode.E, "E"),
            6: (KEY, Keycode.R, "R"),
            5: (KEY, Keycode.T, "T"),
            4: (KEY, Keycode.Y, "Y"),
            3: (KEY, Keycode.U, "U"),
            2: (KEY, Keycode.I, "I"),
            1: (KEY, Keycode.O, "O"),
            0: (KEY, Keycode.P, "P"),
        },
        1: {
            9: (KEY, Keycode.A, "A"),
            8: (KEY, Keycode.S, "S"),
            7: (KEY, Keycode.D, "D"),
            6: (KEY, Keycode.F, "F"),
            5: (KEY, Keycode.G, "G"),
            4: (KEY, Keycode.H, "H"),
            3: (KEY, Keycode.J, "J"),
            2: (KEY, Keycode.K, "K"),
            1: (KEY, Keycode.L, "L"),
            0: (KEY, Keycode.ENTER, "Enter"),
        },
        2: {
            9: (KEY, Keycode.Z, "Z"),
            8: (KEY, Keycode.X, "X"),
            7: (KEY, Keycode.C, "C"),
            6: (KEY, Keycode.V, "V"),
            5: (KEY, Keycode.B, "B"),
            4: (KEY, Keycode.N, "N"),
            3: (KEY, Keycode.M, "M"),
            2: (KEY, Keycode.PERIOD, "."),
            1: (KEY, Keycode.UP_ARROW, "Up Arrow"),
            0: (KEY, Keycode.RIGHT_SHIFT, "Shift"),
        },
        3: {
            9: (KEY, Keycode.LEFT_CONTROL, "Ctrl"),
            8: (KEY, Keycode.LEFT_ALT, "Alt"),
            7: (KEY, Keycode.COMMAND, "Cmd"),
            6: (LAYER, 1, "Layer 1"),
            5: (KEY, Keycode.SPACEBAR, "Space"),
            4: (NONE, 0, "None"),
            3: (LAYER, 2, "Layer 2"),
            2: (KEY, Keycode.LEFT_ARROW, "Left Arrow"),
            1: (KEY, Keycode.DOWN_ARROW, "Down Arrow"),
            0: (KEY, Keycode.RIGHT_ARROW, "Right Arrow"),
        },
    },
    # layer 1
    {
        0: {
            9: (KEY, Keycode.F1, "F1"),
            8: (KEY, Keycode.F2, "F2"),
            7: (KEY, Keycode.F3, "F3"),
            6: (KEY, Keycode.F4, "F4"),
            5: (KEY, Keycode.F5, "F5"),
            4: (KEY, Keycode.F6, "F6"),
            3: (KEY, Keycode.F7, "F7"),
            2: (KEY, Keycode.F8, "F8"),
            1: (KEY, Keycode.F9, "F9"),
            0: (KEY, Keycode.F10, "F10"),
        },
        1: {
            9: (KEY, Keycode.ESCAPE, "Esc"),
            8: (KEY, Keycode.TAB, "Tab"),
            7: (NONE, 0, "None"),
            6: (NONE, 0, "None"),
            5: (NONE, 0, "None"),
            4: (NONE, 0, "None"),
            3: (KEY, Keycode.F11, "F11"),
            2: (KEY, Keycode.F12, "F12"),
            1: (KEY, Keycode.DELETE, "Delete"),
            0: (KEY, Keycode.BACKSPACE, "Backspace"),
        },
        2: {
            9: (KEY, Keycode.LEFT_SHIFT, "Shift"),
            8: (NONE, 0, "None"),
            7: (NONE, 0, "None"),
            6: (NONE, 0, "None"),
            5: (NONE, 0, "None"),
            4: (NONE, 0, "None"),
            3: (NONE, 0, "None"),
            2: (NONE, 0, "None"),
            1: (KEY, Keycode.UP_ARROW, "Up Arrow"),
            0: (KEY, Keycode.RIGHT_SHIFT, "Shift"),
        },
        3: {
            9: (KEY, Keycode.LEFT_CONTROL, "Ctrl"),
            8: (KEY, Keycode.LEFT_ALT, "Alt"),
            7: (KEY, Keycode.COMMAND, "Cmd"),
            6: (LAYER, 1, "Layer 1"),
            5: (KEY, Keycode.SPACEBAR, "Space"),
            4: (NONE, 0, "None"),
            3: (LAYER, 2, "Layer 2"),
            2: (KEY, Keycode.LEFT_ARROW, "Left Arrow"),
            1: (KEY, Keycode.DOWN_ARROW, "Down Arrow"),
            0: (KEY, Keycode.RIGHT_ARROW, "Right Arrow"),
        }
    },
    # layer 2
    {
        0: {
            9: (KEY, Keycode.ONE, "1"),
            8: (KEY, Keycode.TWO, "2"),
            7: (KEY, Keycode.THREE, "3"),
            6: (KEY, Keycode.FOUR, "4"),
            5: (KEY, Keycode.FIVE, "5"),
            4: (KEY, Keycode.SIX, "6"),
            3: (KEY, Keycode.SEVEN, "7"),
            2: (KEY, Keycode.EIGHT, "8"),
            1: (KEY, Keycode.NINE, "9"),
            0: (KEY, Keycode.ZERO, "0"),
        },
        1: {
            9: (KEY, Keycode.GRAVE_ACCENT, "`"),
            8: (NONE, 0, "None"),
            7: (NONE, 0, "None"),
            6: (NONE, 0, "None"),
            5: (NONE, 0, "None"),
            4: (NONE, 0, "None"),
            3: (KEY, Keycode.MINUS, "-"),
            2: (KEY, Keycode.EQUALS, "="),
            1: (KEY, Keycode.LEFT_BRACKET, "["),
            0: (KEY, Keycode.RIGHT_BRACKET, "]"),
        },
        2: {
            9: (KEY, Keycode.LEFT_SHIFT, "Shift"),
            8: (NONE, 0, "None"),
            7: (NONE, 0, "None"),
            6: (NONE, 0, "None"),
            5: (NONE, 0, "None"),
            4: (NONE, 0, "None"),
            3: (KEY, Keycode.SEMICOLON, ";"),
            2: (KEY, Keycode.QUOTE, "'"),
            1: (KEY, Keycode.BACKSLASH, "\\"),
            0: (KEY, Keycode.RIGHT_SHIFT, "Shift"),
        },
        3: {
            9: (KEY, Keycode.LEFT_CONTROL, "Ctrl"),
            8: (KEY, Keycode.LEFT_ALT, "Alt"),
            7: (KEY, Keycode.COMMAND, "Cmd"),
            6: (LAYER, 1, "Layer 1"),
            5: (KEY, Keycode.SPACEBAR, "Space"),
            4: (NONE, 0, "None"),
            3: (LAYER, 2, "Layer 2"),
            2: (KEY, Keycode.COMMA, ","),
            1: (KEY, Keycode.PERIOD, "."),
            0: (KEY, Keycode.FORWARD_SLASH, "/"),
        }
    },
]
