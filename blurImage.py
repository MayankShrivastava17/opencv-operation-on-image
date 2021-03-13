import cv2 as cv
import numpy as np

img = cv.imread("dog.jpg")

cv.imshow('Original Image', img)
cv.waitKey(0)

# Gaussian Blur
Gaussian = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussina Blur', Gaussian)
cv.waitKey(0)

# Median Blur
median = cv.medianBlur(img, 5)
cv.imshow('Median Blur', median)
cv.waitKey(0)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 9, 75, 75)
cv.imshow('Bilateral Blur', bilateral)
cv.waitKey(0)

cv.destroyAllWindows()
