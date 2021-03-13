import cv2 as cv

img = cv.imread("dog.jpg")

cv.imshow("Original Image", img)
cv.waitKey(0)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Image", grey)
cv.waitKey(0)

cv.destroyAllWindows()
