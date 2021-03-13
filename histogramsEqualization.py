import cv2 as cv
import numpy as np

img = cv.imread("dog.jpg", 0)
cv.imshow("Original Image", img)
cv.waitKey(0)

equ = cv.equalizeHist(img)

res = np.hstack((img, equ))
cv.imshow(res)
cv.waitKey(0)

cv.destoryAllWindows()
