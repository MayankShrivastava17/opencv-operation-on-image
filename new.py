import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib qt

img = cv.imread("dog.jpg")

half = cv.resize(img, (0,0), fx=0.1, fy=0.1)
bigger = cv.resize(img, (1050, 1610))

stretch_near = cv.resize(img, (780, 540), interpolation = cv.INTER_NEAREST)

titles = ["Original", "Half", "Bigger", "Interpolation Nearest"]
images = [img, half, bigger, stretch_near]
cnt = 4

for i in range(cnt):
    plt.subplot(2, 2, i+1)
    plt.title(titles[i])
    plt.imshow(images[i])

plt.show()
