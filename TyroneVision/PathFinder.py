import cv2
import numpy as np
Exit_fail = -100000


def getDistFromEdge(y, x, width, image):
    #print("Image size: ", image.shape[0])
    #print("Example pixel: ", image[200, 200])
    #cv2.rectangle(image, (0, 0), (60, 60), (255), -1)
    cv2.imshow('mask_g', image)
    i = 0;
    #print("x is ", x, " width is ", width)
    while ((x - i > 1) and (i + x< width-1)):
        #print("Current Pixel: ", image[y, x + i])
        if (image[y, x + i] != image[y, x + i + 1]):
            #print("i: ", i)
            return i
        elif (image[y, x - i] != image[y, x - i - 1]):
            #print("i: ", i)
            return -i
        i += 1
    #print("returning EXIT FAIL")
    return Exit_fail


def getArray(image, height, width):

    x = int(width/2)
    reduced = cv2.reduce(image, 0, cv2.REDUCE_AVG, dtype=cv2.CV_32S)
    for i in range(reduced.shape[1]):
        thisPixel = reduced[0, i]
        if thisPixel > 190:
            x = i;
            print(i)
            break

    ychange = 10
    y = height - 1
    arr = []
    while (y>0):
        i = getDistFromEdge(y, x, width, image)
        if i != Exit_fail:
            #print(arr)
            #return arr
            x += i
            #print("would add: ", x, " ", y)
            arr.append((x, y))
        y -= ychange
    return arr
