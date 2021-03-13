# This is used for object subtraction, security enhancement, pedestrian tracking
import cv2 as cv
import numpy as np 

cap = cv.VideoCapture(0)
fbgb = cv.createBackgroundSubtractorMOG2()

while 1:
    ret, frame = cap.read()
    fgmask = fbgb.apply(frame)
    cv.imshow('fgmask', fgmask)
    # cv.waitKey(0)
    cv.imshow('frame', frame)
    # cv.waitKey(0)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
