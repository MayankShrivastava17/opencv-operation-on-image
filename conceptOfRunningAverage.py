# This technique is used for detecting dynamically moving objects from static camera

import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

_, img = cap.read()

averageValue1 = np.float32(img)

while 1:
    _, img = cap.read()
    cv.accumulateWeighted(img, averageValue1, 0.02)
    resultingFrame1 = cv.convertScaleAbs((averageValue1))
    cv.imshow('InputWindow', img)
    cv.imshow('AverageValue1', resultingFrame1)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()
