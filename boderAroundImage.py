import cv2 as cv

img = cv.imread("dog.jpg")

cv.imshow("Original Image", img)
cv.waitKey(0)

border = cv.copyMakeBorder(img, 10, 10, 10, 10, cv.BORDER_CONSTANT)
cv.imshow("Bordered Image", border)
cv.waitKey(0)

cv.destoryAllWindows()
