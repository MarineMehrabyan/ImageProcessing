import cv2
import numpy as np

def apply_median_filter(image, ksize):
    filtered_image = cv2.medianBlur(image, ksize)
    return filtered_image

def on_trackbar(val):
    global img
    ksize = val*2+1
    filtered_image = apply_median_filter(img, ksize)
    cv2.imshow("Median Filter", filtered_image)

img = cv2.imread('img1.jpeg', cv2.IMREAD_GRAYSCALE)
cv2.namedWindow("Median Filter")

cv2.createTrackbar("Kernel Size", "Median Filter", 1, 10, on_trackbar)

cv2.imshow("Median Filter", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

