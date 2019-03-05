import cv2
import config
import face
import picam
import emailer
import time
import datetime
import os
import shutil
import glob
import subprocess

# Initialize camera and box.
camera = config.get_camera()

while True:
	# Getting image
	image = camera.read()
	gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	cv2.equalizeHist(gray_image,gray_image)

	gray_image = cv2.resize(gray_image,(160,120))
	# Time calculation
	#t = cv2.getTickCount()

	# Human face detection
	result = face.detect_single(gray_image,config.HAAR_FACES)

	if result is None:
		pass
	else:
	#	print 'Human Face found'
		x, y, w, h = result
		cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)
		cv2.imwrite(config.DEBUG_IMAGE, image)
		emailer.sendMail(["xyz@gmail.com"],
        	"Message from Your Scarecrow",
        	"There is someone in the garden",
        	["capture.jpg"])
	

	#t = cv2.getTickCount() - t
	#print "time taken for detection = %gms" % (t/(cv2.getTickFrequency()*1000.))
	
