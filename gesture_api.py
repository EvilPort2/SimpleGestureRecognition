import pyautogui as gui
import os

GEST_START = ("N", "E", "S", "W")
GEST_CLOSE = ("SE", "N", "SW")
GEST_COPY = ("W", "S", "E")
GEST_PASTE = ("SE", "NE")
GEST_CUT = ("SW", "N", "SE")
GEST_ALT_TAB = ("SE", "SW")
GEST_ALT_SHIFT_TAB = ("SW", "SE")
GEST_MAXIMISE = ("N",)
GEST_MINIMISE = ("S",)
GEST_LOCK = ("S", "E")
GEST_TASK_MANAGER = ("E", "W", "S")
GEST_NEW_FILE = ("N", "SE", "N")
GEST_SELECT_ALL = ("NE", "SE", "NW", "W")

GESTURES = {GEST_CUT: ('ctrlleft', 'x'),
GEST_CLOSE: ('altleft', 'f4'),
GEST_ALT_SHIFT_TAB: ('altleft', 'shiftleft', 'tab'),
GEST_PASTE: ('ctrlleft', 'v'),
GEST_ALT_TAB: ('altleft', 'tab'),
GEST_COPY: ('ctrlleft', 'c'),
GEST_NEW_FILE: ('ctrlleft', 'n'),
GEST_SELECT_ALL: ('ctrlleft', 'a')}

if os.name == 'nt':
    GESTURES[GEST_START] = ('winleft',)
    GESTURES[GEST_LOCK] = ('winleft', 'l')
    GESTURES[GEST_TASK_MANAGER] = ('ctrlleft', 'shiftleft', 'esc')
else:
    GESTURES[GEST_START] = ('altleft', 'f1')
    GESTURES[GEST_LOCK] = ('ctrlleft', 'altleft', 'l')
    GESTURES[GEST_TASK_MANAGER] = ('ctrlleft', 'esc')

def do_gesture_action(gesture):
    if gesture in GESTURES.keys():
        keys = list(GESTURES[gesture])
        last_key = keys.pop()
        if len(keys) >= 1:
            for key in keys:
                gui.keyDown(key)
        gui.press(last_key)
        if len(keys) >= 1:
            keys.reverse()
            for key in keys:
                gui.keyUp(key)
