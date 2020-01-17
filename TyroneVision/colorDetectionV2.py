import cv2
import numpy as np
from PathFinder import getArray
cap = cv2.VideoCapture(1)

lower_green = np.array([45, 35, 50])
upp_green = np.array([85, 255, 255])

while(1):
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, channels = hsv.shape

    mask_g = cv2.inRange(hsv, lower_green, upp_green)


    arr = getArray(mask_g, height-60, width)
    #print(arr)
    if len(arr) > 0:
        for i in range(len(arr)-1):
            cv2.circle(frame, (arr[i]), 2, (180, 105, 255),-1)

    cv2.imshow('frame',frame)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        frame.release()
        cv2.destroyAllWindows()
        break




