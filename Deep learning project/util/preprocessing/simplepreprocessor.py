# import the necessary packages
import cv2

class SimplePreprocessor:
	def __init__(self, width, height, inter=cv2.INTER_AREA):
		self.width = width
		self.height = height
		self.inter = inter

	def preprocess(self, image):
		# ย่อรูปไม่สนใจสัดส่วน
		return cv2.resize(image, (self.width, self.height),
			interpolation=self.inter)