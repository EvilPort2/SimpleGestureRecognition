import pyautogui as gui
import os
import time
import datetime
import cv2
import thread
from threading import Thread

class TakePhoto(Thread):
	def __init__(self, cam):
		Thread.__init__(self)
		self.cam = cam
		self.start()

	def run(self):
		cam = self.cam
		time.sleep(5)
		img1 = cam.read()[1]
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d %H_%M_%S')
		cv2.imwrite("photos/"+st + ".png", img1)
		

def screenshot(x):
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d %H_%M_%S')
	gui.screenshot("screenshot/" + st + ".png")

def text_editor(x = None):
	thread.start_new_thread(os.system, ("notepad", ))

def start_menu(x = None):
	gui.press('winleft')

def new_file(x = None):
	gui.hotkey('ctrlleft', 'n')

def select_all(x = None):
	gui.hotkey('ctrlleft', 'a')

def close(x = None):
	gui.hotkey('altleft', 'f4')

def copy(x = None):
	gui.hotkey('ctrlleft', 'c')
	
def paste(x = None):
	gui.hotkey('ctrlleft', 'v')

def cut(x = None):
	gui.hotkey('ctrlleft', 'x')

def next_window(x = None):
	gui.hotkey('altleft', 'tab')

def prev_window(x = None):
	gui.hotkey('altleft', 'shiftleft', 'tab')

def maximize(x = None):
	gui.hotkey('winleft', 'up')

def minimize(x = None):
	gui.hotkey('winleft', 'down')

def lockscreen(x = None):
	gui.hotkey('winleft', 'l')

def task_manager(x = None):
	gui.hotkey('ctrlleft', 'shiftleft', 'esc')

GEST_START = ("N", "E", "S", "W")
GEST_CLOSE = ("SE", "N", "SW")
GEST_COPY = ("W", "S", "E")
GEST_PASTE = ("SE", "NE")
GEST_CUT = ("SW", "N", "SE")
GEST_ALT_TAB = ("SE", "SW")
GEST_ALT_SHIFT_TAB = ("SW", "SE")
GEST_MAXIMIZE = ("N",)
GEST_MINIMIZE = ("S",)
GEST_LOCK = ("S", "E")
GEST_TASK_MANAGER = ("E", "W", "S")
GEST_NEW_FILE = ("N", "SE", "N")
GEST_SELECT_ALL = ("NE", "SE", "NW", "W")

GESTURES_ONE_HAND = \
{GEST_START: start_menu, 
GEST_CLOSE: close,
GEST_COPY: copy,
GEST_PASTE: paste,
GEST_CUT: cut,
GEST_ALT_TAB: next_window,
GEST_ALT_SHIFT_TAB: prev_window,
GEST_MAXIMIZE: maximize,
GEST_MINIMIZE: minimize,
GEST_LOCK: lockscreen,
GEST_TASK_MANAGER: task_manager,
GEST_NEW_FILE: new_file,
GEST_SELECT_ALL: select_all}


GEST_SCREENSHOT = (("W", "S", "E"), ("E", "S", "W"))
GEST_CAMERA = (("SW", "SE"), ("SE", "SW"))
GEST_TEXT_EDITOR = (("N", "E", "S", "W"), ("S",))

GESTURES_TWO_HAND = \
{GEST_SCREENSHOT: screenshot,
GEST_CAMERA: TakePhoto,
GEST_TEXT_EDITOR: text_editor}

def do_gesture_action(cam, gesture1, gesture2 = None):
	ret = None
	if gesture2 == None:
		if gesture1 in GESTURES_ONE_HAND.keys():
			ret = GESTURES_ONE_HAND[gesture1](cam)
	else:
		if (gesture1, gesture2) in GESTURES_TWO_HAND.keys():
			ret = GESTURES_TWO_HAND[(gesture1, gesture2)](cam)

	if ret != None:
		cam = ret

	return cam