import pyautogui as gui
import datetime, time, os
from threading import Thread

class TakePhoto:
	def __init__(self, video_stream):
		self.vs = video_stream
		Thread(target=self.start, args=()).start()
		
	def start(self):
		time.sleep(5)
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d %H_%M_%S')
		self.vs.save("photos/"+st + ".png")

def gesture_action_a(*args):
	gui.hotkey('ctrl', 'a')

def gesture_action_b(*args):
	pass

def gesture_action_c(*args):
	gui.hotkey('ctrl', 'c')

def gesture_action_d(*args):
	pass

def gesture_action_e(*args):
	os.system("explorer")

def gesture_action_f(*args):
	gui.hotkey('winleft', 'r')
	gui.typewrite("http://facebook.com")
	gui.press('enter')

def gesture_action_g(*args):
	pass

def gesture_action_h(*args):
	pass

def gesture_action_i(*args):
	pass

def gesture_action_j(*args):
	pass

def gesture_action_k(*args):
	pass

def gesture_action_l(*args):
	gui.hotkey('winleft', 'l')

def gesture_action_m(*args):
	gui.press('winleft')

def gesture_action_n(*args):
	gui.hotkey('ctrl', 'n')

def gesture_action_o(*args):
	ts = time.time()
	st = datetime.datetime.fromtimestamp(ts).strftime('%Y_%m_%d %H_%M_%S')
	gui.screenshot("screenshot/" + st + ".png")

def gesture_action_p(*args):
	video_stream = args[0]
	TakePhoto(video_stream)

def gesture_action_q(*args):
	pass

def gesture_action_r(*args):
	gui.hotkey('winleft', 'r')

def gesture_action_s(*args):
	gui.hotkey('ctrl', 's')

def gesture_action_t(*args):
	gui.hotkey('ctrl', 'shift', 'esc')

def gesture_action_u(*args):
	pass

def gesture_action_v(*args):
	gui.hotkey('ctrl', 'v')

def gesture_action_w(*args):
	pass

def gesture_action_x(*args):
	gui.hotkey('ctrl', 'x')

def gesture_action_y(*args):
	pass

def gesture_action_z(*args):
	gui.hotkey('ctrl', 'z')


def do_action(character, mode, *args):
	gesture_action_set = {
	'A': gesture_action_a,
	'B': gesture_action_b,
	'C': gesture_action_c,
	'D': gesture_action_d,
	'E': gesture_action_e,
	'F': gesture_action_f,
	'G': gesture_action_g,
	'H': gesture_action_h,
	'I': gesture_action_i,
	'J': gesture_action_j,
	'K': gesture_action_k,
	'L': gesture_action_l,
	'M': gesture_action_m,
	'N': gesture_action_n,
	'O': gesture_action_o,
	'P': gesture_action_p,
	'Q': gesture_action_q,
	'R': gesture_action_r,
	'S': gesture_action_s,
	'T': gesture_action_t,
	'U': gesture_action_u,
	'V': gesture_action_v,
	'W': gesture_action_w,
	'X': gesture_action_x,
	'Y': gesture_action_y,
	'Z': gesture_action_z,
	}
	if character != '':
		if mode == 'typing':
			gui.press(character)
		else:
			if len(args) >= 1:
				video_stream = args[0]
				gesture_action_set[character](video_stream)
			else:
				gesture_action_set[character]()