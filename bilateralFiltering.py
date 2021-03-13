# This is used to remove to noise from image
import cv2 as cv

img = cv.imread("dog.jpg")

bilateral = cv.bilateralFilter(img, 15, 75, 75)

cv.imshow("Bilateral Filter", bilateral)
cv.waitKey(0)
