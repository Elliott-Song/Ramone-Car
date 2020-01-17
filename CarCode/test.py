# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)

# allow the camera to warmup
time.sleep(0.1)

# grab an image from the camera
camera.capture(rawCapture, format="rgb")
image = rawCapture.array



height, width, channels = image.shape
print "STUFF: ", height, width, channels


print('This pixel: ' + image[height/2,width/2,0])

cv2.imwrite('/home/pi/ThunderHurricanes/testImage.jpg', image)

# display the image on screen and wait for a keypress
# cv2.imshow("Image", image)


cv2.waitKey(0)