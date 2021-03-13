# We are going to increase and decrease the resolution of image
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("dog.jpg")
layer = img.copy()

# We are going to create different size of image
for i in range(4):
    plt.subplot(2, 2, i+1)
    layer = cv.pyrDown(layer)
    plt.imshow(layer)
    cv.imshow("str(i)", layer)
    cv.waitKey(0)
    
for i in range(4):
    plt.subplot(2, 2, i+1)
    layer = cv.pyrUp(layer)
    plt.imshow(layer)
    cv.imshow("str(i)", layer)
    cv.waitKey(0)

cv.destroyAllWindows()
