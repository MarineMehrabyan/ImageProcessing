import cv2
import numpy as np

def apply_sharpen_filter(image, kernel_size, strength):
    blurred_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    sharp_image = cv2.addWeighted(image, 1 + strength, blurred_image, -strength, 0)
    return sharp_image

def on_trackbar(val):
    global img
    sharp_image = apply_sharpen_filter(img, 5, val/100)
    cv2.imshow("Sharpen Filter", sharp_image)

img = cv2.imread("img6.jpeg")

cv2.namedWindow("Sharpen Filter")

cv2.createTrackbar("Strength", "Sharpen Filter", 0, 200, on_trackbar)

cv2.imshow("Sharpen Filter", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

