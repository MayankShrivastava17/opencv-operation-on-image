import cv2 as cv
import numpy as np

img1 = cv.imread("dog.jpg")

img = cv.cvtColor(img1, cv.COLOR_BGR2GRAY)

ret, thresh = cv.threshold(img, 120, 255, cv.THRESH_BINARY + cv.THRESH_OTSU)

cv.imshow("Original", img1)
cv.waitKey(0)

cv.imshow("Otsu Threshold", thresh)
cv.waitKey(0)

cv.destroyAllWindows()
