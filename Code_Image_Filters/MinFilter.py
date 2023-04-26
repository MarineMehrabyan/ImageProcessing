import cv2
import numpy as np

def apply_min_filter(image, ksize):
    kernel = np.ones((ksize, ksize), np.uint8)
    filtered_image = cv2.erode(image, kernel, iterations=1)
    return filtered_image

def on_trackbar(val):
    ksize = cv2.getTrackbarPos("Kernel Size", "Minimum Filter")
    filtered_image = apply_min_filter(img, ksize)
    cv2.imshow("Minimum Filter", filtered_image)

img = cv2.imread("img4.jpeg")

cv2.namedWindow("Minimum Filter")
cv2.createTrackbar("Kernel Size", "Minimum Filter", 1, 30, on_trackbar)
cv2.imshow("Minimum Filter", img)

cv2.waitKey(0)
cv2.destroyAllWindows()

