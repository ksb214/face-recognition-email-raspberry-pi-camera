import io
import time
import cv2
import numpy as np
import picamera
import config


class OpenCVCapture(object):
	def read(self):
		data = io.BytesIO()
		
		#to speed things up, lower the resolution of the camera
		CAMERA_WIDTH = 320
		CAMERA_HEIGHT = 240
		
		with picamera.PiCamera() as camera:
			camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)	
			camera.rotation = (90)
			camera.capture(data, format='jpeg')
		data = np.fromstring(data.getvalue(), dtype=np.uint8)
		# Decode the image data and return an OpenCV image.
		image = cv2.imdecode(data, 1)
		# Save captured image for debugging.
		#cv2.imwrite(config.DEBUG_IMAGE, image)
		# Return the captured image data.
		return image
