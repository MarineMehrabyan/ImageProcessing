import cv2
import numpy as np

# Load the image
img = cv2.imread('image.jpg')

# Define the percentage of color reduction or increase
x = 60

# Copy the original image
img_less_color = img.copy()
img_more_color = img.copy()

# Reduce color by x%
img_less_color = np.clip((1 - x/100) * img_less_color, 0, 255).astype(np.uint8)

# Increase color by x%
img_more_color = np.clip((1 + x/100) * img_more_color, 0, 255).astype(np.uint8)

# Display the images
cv2.imshow('Original Image', img)
cv2.imshow(str(x)+'% Less Color', img_less_color)
cv2.imshow(str(x)+'% More Color', img_more_color)

cv2.waitKey(0)
cv2.destroyAllWindows()

