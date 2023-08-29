import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
img = cv.imread('/Users/mac/Documents/GitHub/data-science/lecture/고잉1.png', cv.IMREAD_COLOR)
cv.imshow("frame",img)
cv.waitKey(0)

assert img is not None, "file could not be read, check with os.path.exists()"
edges = cv.Canny(img,50,150)
cv.imshow("edges", edges)
cv.waitKey(0)
print(img.shape)
cv.imwrite("edges.jpg", edges)

# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
# plt.show()