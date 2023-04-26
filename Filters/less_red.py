import cv2
import numpy as np

# Load image
img = cv2.imread('image.jpg')

# Define reduction/increase factor for red channel
x = 30  # x% less red
red_factor = 1 - x/100

# Reduce red channel values by x% to make image x% less red
less_red_img = img.copy()


# To access the red channel of a BGR image, you can use the NumPy array indexing notation with the [:,:,2] syntax. Here, the : indicates that we want to select all rows and columns in the image, while the 2 indicates that we want to select the third channel, which corresponds to the Red channel.
less_red_img[:,:,2] = less_red_img[:,:,2] * red_factor
less_red_img = np.clip(less_red_img, 0, 255).astype(np.uint8)

# Display original, less red, and more red images
cv2.imshow('Original Image', img)
cv2.imshow(f'{x}% Less Red', less_red_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

