from threading import Thread
import cv2

class WebcamVideoStream:
	def __init__(self, src=1):
		self.cam = cv2.VideoCapture(src)
		if self.cam.read()[0] == False:
			self.cam = cv2.VideoCapture(0)
		self.img = self.cam.read()[1]
		self.stopped = False

	def start(self):
		Thread(target=self.update, args=()).start()
		return self

	def update(self):
		while not self.stopped:
			self.img = self.cam.read()[1]

	def read(self):
		return self.img

	def save(self, location):
		cv2.imwrite(location, self.read())

	def stop(self):
		self.cam.release()
		self.stopped = True

