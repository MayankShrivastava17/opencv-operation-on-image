import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)

while 1:
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_blue = np.array([60, 35, 140])
    upper_blue = np.array([180, 255, 255])
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    result = cv.bitwise_and(frame, frame, mask = mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('result', result)

    cv.waitKey(0)

cv.destroyAllWindows()
cap.release()
