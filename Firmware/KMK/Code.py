import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())

# ===== MATRIX PINS (MATCH YOUR SCHEMATIC) =====
keyboard.row_pins = (
    board.GP26,
    board.GP27,
    board.GP28,
    board.GP29,
    board.GP6,
)

keyboard.col_pins = (
    board.GP0,
    board.GP1,
    board.GP2,
    board.GP3,
    board.GP4,
    board.GP5,
    board.GP7,
    board.GP8,
    board.GP9,
    board.GP10,
    board.GP11,
    board.GP12,
    board.GP13,
    board.GP14,
)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

# ===== KEYMAP =====
keyboard.keymap = [
    [
        KC.ESC, KC.N1, KC.N2, KC.N3, KC.N4, KC.N5, KC.N6, KC.N7, KC.N8, KC.N9, KC.N0, KC.MINS, KC.EQL, KC.BSPC,
        KC.TAB, KC.Q,  KC.W,  KC.E,  KC.R,  KC.T,  KC.Y,  KC.U,  KC.I,  KC.O,  KC.P,  KC.LBRC, KC.RBRC, KC.BSLS,
        KC.CAPS,KC.A,  KC.S,  KC.D,  KC.F,  KC.G,  KC.H,  KC.J,  KC.K,  KC.L,  KC.SCLN, KC.QUOT, KC.ENT,
        KC.LSFT,KC.Z,  KC.X,  KC.C,  KC.V,  KC.B,  KC.N,  KC.M,  KC.COMM,KC.DOT, KC.SLSH, KC.RSFT,
        KC.LCTL,KC.LGUI,KC.LALT,KC.SPC,KC.RALT,KC.RGUI,KC.MO(1),KC.RCTL
    ],
    [
        KC.GRV, KC.F1, KC.F2, KC.F3, KC.F4, KC.F5, KC.F6, KC.F7, KC.F8, KC.F9, KC.F10, KC.F11, KC.F12, KC.DEL,
        KC.NO,  KC.NO, KC.UP, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.LEFT,KC.DOWN,KC.RIGHT,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO,
        KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO, KC.NO
    ]
]

if __name__ == '__main__':
    keyboard.go()
