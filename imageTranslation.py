# Shifting of image to one location to another is also know as Translation
import cv2 as cv
import numpy as np

img = cv.imread("dog.jpg")

height, width = img.shape[:2]

qHeight, qWidth = height/4, width/4

t = np.float32([[1, 0, qWidth], [0, 1, qHeight]])

imgTranslation = cv.warpAffine(img, t, (width, height))

cv.imshow("Original Image", img)
cv.imshow("Translation", imgTranslation)
cv.waitKey(0)

cv.destroyAllWindows()
