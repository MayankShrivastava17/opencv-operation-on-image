# Foreground extraction from the background using "Grabcut Algorithm"

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("dog.jpg")

mask = np.zeros(img.shape[:2], np.uint8)

bgModel = np.zeros((1, 65), np.float64)
fgModel = np.zeros((1, 65), np.float64)

rectangle = (20, 100, 150, 150)

cv.grabCut(img, mask, rectangle, bgModel, fgModel, 3, cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')

img = img * mask2[:, :, np.newaxis]

plt.imshow(img)
plt.colorbar()
plt.show()
