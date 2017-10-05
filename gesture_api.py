import pyautogui as gui
import os
import time
import datetime
import cv2
import thread

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
GEST_SHOW_PIC1 = ("W", "S", "E", "S", "W")
GEST_SHOW_PIC2 = ("E", "S", "W", "E", "N")
GEST_SCREENSHOT = (("W", "S", "E"), ("E", "S", "W"))
GEST_CAMERA = (("SW", "SE"), ("SE", "SW"))
GEST_TEXT_EDITOR = (("N", "E", "S", "W"), ("S",))

GESTURES_ONE_HAND = {GEST_CUT: ('ctrlleft', 'x'),
GEST_CLOSE: ('altleft', 'f4'),
GEST_ALT_SHIFT_TAB: ('altleft', 'shiftleft', 'tab'),
GEST_PASTE: ('ctrlleft', 'v'),
GEST_ALT_TAB: ('altleft', 'tab'),
GEST_COPY: ('ctrlleft', 'c'),
GEST_NEW_FILE: ('ctrlleft', 'n'),
GEST_SELECT_ALL: ('ctrlleft', 'a')}


def screenshot():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d %H_%M_%S')
    gui.screenshot("screenshot/" + st + ".png")

def text_editor():
    print("text_editor")
    if os.name == 'nt':
        os.system("notepad.exe")
    else:
        os.system("gedit")

GESTURES_TWO_HAND = {GEST_SCREENSHOT: screenshot,
GEST_TEXT_EDITOR: text_editor}

if os.name == 'nt':
    GESTURES_ONE_HAND[GEST_START] = ('winleft',)
    GESTURES_ONE_HAND[GEST_LOCK] = ('winleft', 'l')
    GESTURES_ONE_HAND[GEST_TASK_MANAGER] = ('ctrlleft', 'shiftleft', 'esc')
else:
    GESTURES_ONE_HAND[GEST_START] = ('altleft', 'f1')
    GESTURES_ONE_HAND[GEST_LOCK] = ('ctrlleft', 'altleft', 'l')
    GESTURES_ONE_HAND[GEST_TASK_MANAGER] = ('ctrlleft', 'esc')

def do_gesture_action(gesture1, gesture2 = None):
    print(gesture1)
    print(gesture2)
    if gesture2 == None:
        if gesture1 in GESTURES_ONE_HAND.keys():
            keys = list(GESTURES_ONE_HAND[gesture1])
            last_key = keys.pop()
            if len(keys) >= 1:
                for key in keys:
                    gui.keyDown(key)
            gui.press(last_key)
            if len(keys) >= 1:
                keys.reverse()
                for key in keys:
                    gui.keyUp(key)
    else:
        if (gesture1, gesture2) in GESTURES_TWO_HAND.keys():
            thread.start_new_thread(GESTURES_TWO_HAND[(gesture1, gesture2)], ())
