import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read grayscale image
img = cv2.imread('image2.jpg', 0)

# Compute histogram of pixel intensities
hist, bins = np.histogram(img.ravel(), 256, [0,256])

# Plot histogram
plt.hist(img.ravel(), 256, [0,256])
#plt.show()

# Determine threshold value using Otsu's method
ret, threshold = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
print("Threshold value:", ret)

# Apply global thresholding
threshold_value = ret
max_value = 255
img_binary = cv2.threshold(img, threshold_value, max_value, cv2.THRESH_BINARY)[1]

# Show the results
cv2.imshow('Grayscale Image', img)
cv2.imshow('Binary Image', img_binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

