import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while (True):
    ret, frame = cap.read()
    cv2.line(img=frame, pt1=(10, 10), pt2=(100, 10), color=(255, 255, 255), thickness=5)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS)


    cv2.imshow('frame', gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()