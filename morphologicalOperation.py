# Python program to illustrate
# Opening morphological Operation
# on a image
import cv2 as cv
import numpy as np

src = cv.VideoCapture(0)

while 1:
    _, image = src.read()
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    blue1 = np.array([110, 50, 50])
    blue2 = np.array([130, 255, 255])
    mask = cv.inRange(hsv, blue1, blue2)
    res = cv.bitwise_and(image, image, mask = mask)
    kernel = np.ones((5, 5), np.uint8)
    closing = cv.morphologyEx(mask, cv.MORPH_OPEN, kernel)
    cv.imshow('Mask', mask)
    cv.imshow('Closing', closing)
    if cv.waitKey(1) & 0xFF == ord('a'):
        break


cv.destroyAllWindows()
src.release()
