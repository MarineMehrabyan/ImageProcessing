import cv2
import numpy as np

# Load a BGR image
img_bgr = cv2.imread('image.jpg')
original_img = img_bgr.copy()
# Define percentage increase in red
x_percent = 40  # x% more

# Calculate factor to increase red channel
red_factor = 1 + (x_percent / 100)

# Multiply red channel by factor
# np.clip() function to ensure that the pixel values stay within the range of 0 to 255
# 0 is blue, 1 is greem, 2 is red, 
img_bgr[:,:,2] = np.clip(img_bgr[:,:,2] * red_factor, 0, 255).astype(np.uint8)

# Display modified image
cv2.imshow('Original Image', original_img)
cv2.imshow('Modified Image', img_bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()

