import cv2, pickle, time, os
import numpy as np
from webcam_video_stream import WebcamVideoStream
from action import do_action
from collections import deque
from keras.models import load_model
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

model = load_model('cnn_model_keras21.h5')
image_x, image_y = 28, 28

def contour_area_sort(contours, area_threshold):
	contours.sort(key = cv2.contourArea, reverse = True)
	cnts = [c for c in contours if cv2.contourArea(c) > area_threshold]
	return cnts

def process_letter(letter):
	letter = cv2.copyMakeBorder(letter, 2, 2, 2, 2, cv2.BORDER_CONSTANT, (0, 0, 0))
	h, w = letter.shape 
	if w > h:
		letter = cv2.copyMakeBorder(letter, int((w-h)/2) , int((w-h)/2) , 0, 0, cv2.BORDER_CONSTANT, (0, 0, 0))
	elif h > w:
		letter = cv2.copyMakeBorder(letter, 0, 0, int((h-w)/2) , int((h-w)/2) , cv2.BORDER_CONSTANT, (0, 0, 0))
	letter = cv2.resize(letter, (28, 28))
	letter = np.array(letter, dtype=np.float32)
	letter = np.reshape(letter, (1, image_x, image_y, 1))
	return letter

def predict_letter(letter):
	pred_probab = model.predict(letter)[0]
	pred_class = list(pred_probab).index(max(pred_probab))
	return max(pred_probab), pred_class

def get_letter_from_class(pred_class):
	return chr(64+int(pred_class))

def gesture_action():
	predict_letter(process_letter(np.zeros((200, 200), np.uint8)))
	with open("range.pickle", "rb") as f:
		t = pickle.load(f)
	yellow_lower = np.array([t[0], t[1], t[2]])						  # HSV yellow lower
	yellow_upper = np.array([t[3], t[4], t[5]])					  # HSV yellow upper
	buff = 500
	line_pts = deque(maxlen = buff)
	blackboard = np.zeros((480, 640, 3), dtype=np.uint8)
	letter = np.zeros((200, 200, 3), dtype=np.uint8)
	pred_letter = ''
	mode = 'None'
	frames = 0

	vs = WebcamVideoStream(1).start()
        
	while True:
		img = vs.read()
		img = cv2.flip(img, 1)
		imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(imgHSV, yellow_lower, yellow_upper)
		blur = cv2.medianBlur(mask, 15)
		blur = cv2.GaussianBlur(blur , (5,5), 0)
		thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
		img_cnts = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]
		
		if len(img_cnts) >= 1:
			cnt = max(img_cnts, key=cv2.contourArea)
			if cv2.contourArea(cnt) > 250:
				x, y, w, h = cv2.boundingRect(cnt)
				cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
				M = cv2.moments(cnt)
				center = (int(M['m10']/M['m00']), int(M['m01']/M['m00']))
				line_pts.appendleft(center)
				for i in range(1, len(line_pts)):
					if line_pts[i-1] is None or line_pts[i] is None:
						continue
					cv2.line(blackboard, line_pts[i-1], line_pts[i], (255, 255, 255), 7)
					cv2.line(img, line_pts[i-1], line_pts[i], (0, 0, 255), 2)
		elif len(img_cnts) == 0:
			if len(line_pts) != []:
				blackboard_gray = cv2.cvtColor(blackboard, cv2.COLOR_BGR2GRAY)
				blur1 = cv2.medianBlur(blackboard_gray, 15)
				blur1 = cv2.GaussianBlur(blur1, (5,5), 0)
				thresh1 = cv2.threshold(blur1, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
				blackboard_cnts = cv2.findContours(thresh1.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)[1]
				if len(blackboard_cnts) >= 1:
					cnt = max(blackboard_cnts, key=cv2.contourArea)
					#print(cv2.contourArea(cnt))
					if mode != 'None' and cv2.contourArea(cnt) > 1000:
						x, y, w, h = cv2.boundingRect(cnt)
						letter = blackboard_gray[y:y+h, x:x+w]
						processed_letter = process_letter(letter)
						pred_probab, pred_class = predict_letter(processed_letter)
						if pred_probab*100 > 50:
							pred_letter = get_letter_from_class(pred_class)
						else:
							pred_letter = ''
						do_action(pred_letter, mode, vs)
			line_pts = deque(maxlen=500)
			blackboard = np.zeros((480, 640, 3), dtype=np.uint8)

		cv2.putText(blackboard, "Predicted letter - " + pred_letter, (25, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.5, (255, 255, 0))
		cv2.putText(blackboard, "Mode - " + mode, (25, 100), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 255, 0))
		result = np.hstack((img, blackboard))
		cv2.imshow('img', result)
		keypress = cv2.waitKey(1)
		if keypress == ord('q'):
			break
		elif keypress == ord('s'):
			mode = 'keyboard_shortcut'
		elif keypress == ord('t'):
			mode = 'typing'

	cv2.destroyAllWindows()
	vs.stop()

gesture_action()