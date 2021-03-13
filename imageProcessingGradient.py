# Gradient morphological operation on input frame

import cv2 as cv
import numpy as np

scr = cv.VideoCapture(0)

while 1:
    _, image = scr.read()
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    blue1 = np.array([110, 50, 50])
    blue2 = np.array([130, 255, 255])
    mask = cv.inRange(hsv, blue1, blue2)
    res = cv.bitwise_and(image, image, mask = mask)
    kernel = np.ones((5, 5), np.uint8)
    gradient = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernel)
    cv.imshow('Gradient', gradient)
    cv.imshow('Original', image)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

cv.destroyAllWindows()
scr.release()
