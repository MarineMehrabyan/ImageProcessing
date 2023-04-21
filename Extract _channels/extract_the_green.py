# want to extract the green color information from this image to 
# create a mask that highlights the vegetation in the forest. 
# To do this, you can use the green channel of the image, 
# which represents the intensity of the green color in the image.
# the resulting green areas image highlights the vegetation in the forest
import cv2
import numpy as np

# Load the image
img = cv2.imread('forest.jpeg')

# Split the image into its color channels
b,g,r = cv2.split(img)

# Normalize the green channel to a 0-255 range
# to make it more visually appealing or suitable for further processing 
# to make sure that the green intensity values are consistent across the entire image.
g_norm = cv2.normalize(g, None, 0, 255, cv2.NORM_MINMAX)

# Threshold the green channel to create a binary mask
# that highlights the green areas in the image.
_, mask = cv2.threshold(g_norm, 100, 255, cv2.THRESH_BINARY)

# Apply the mask to the original image
'''we apply a bitwise AND operation between the original image img and the binary mask mask to create a new image that shows only the green areas in the original image.

The bitwise AND operation between two arrays compares each corresponding pixel in both arrays, and outputs a new array with values set to 1 only where both input arrays have a value of 1.'''
masked_img = cv2.bitwise_and(img, img, mask=mask)

# Display the results
cv2.imshow('Original Image', img)
cv2.imshow('Green Channel', g_norm)
cv2.imshow('Green Mask', mask)
cv2.imshow('Green Areas', masked_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

