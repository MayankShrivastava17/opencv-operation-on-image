import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("dog.jpg")
cv.imshow("Original Image", img)
cv.waitKey(0)

hist = cv.calcHist([img], [0], None, [256], [0, 256])

plt.plot(hist)
plt.show()
cv.destoryAllWindows()
