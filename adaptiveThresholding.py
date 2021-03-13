import cv2 as cv
import numpy as np

img1 = cv.imread('dog.jpg')

img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

thresh1 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 199, 5)
thresh2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 199, 5)

cv.imshow('Original', img)
cv.waitKey(0)

cv.imshow('Adaptive Mean', thresh1)
cv.waitKey(0)

cv.imshow('Adaptive Gaussian', thresh2)
cv.waitKey(0)

cv.destroyAllWindows()
