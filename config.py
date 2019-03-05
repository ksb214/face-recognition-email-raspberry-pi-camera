# Face detection cascade classifier configuration.
# You don't need to modify this unless you know what you're doing.
# See: http://docs.opencv.org/modules/objdetect/doc/cascade_classification.html

HAAR_FACES         = 'haarcascade_frontalface_default.xml'
#HAAR_OBJ1	   = 'cascade2.xml'
HAAR_SCALE_FACTOR  = 1.2
HAAR_MIN_NEIGHBORS = 4
HAAR_MIN_SIZE      = (20, 20)


# Filename to use when saving the most recently captured image for debugging.
DEBUG_IMAGE = 'capture.jpg'

def get_camera():
        # Camera to use for capturing images.
        # Use this code for capturing from the Pi camera:
        import picam
        return picam.OpenCVCapture()
        # Use this code for capturing from a webcam:
        # import webcam
        # return webcam.OpenCVCapture(device_id=0)
