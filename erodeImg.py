import cv2 as cv
import numpy as np

img = cv.imread("dog.jpg")

window_name = 'Image'

kernal = np.ones((5, 5), np.uint8)

image = cv.erode(img, kernal)#, cv.BORDER_REFLECT)

cv.imshow(window_name, image)
cv.waitKey(0)
