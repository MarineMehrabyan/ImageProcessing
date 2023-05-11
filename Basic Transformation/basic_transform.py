import cv2 
import numpy as np 
#  basic transformation
image = cv2.imread('calvinHobbes.jpeg') 

# applies a translation transformation on the image
# The translation transformation moves the image to
# a new position based on a specified number of
# pixels in the x and y direction
# n this case, the image is moved by a quarter of its
# height and width in the positive x and y direction.
height, width = image.shape[:2] 
quarter_height, quarter_width = height/4, width/4
T = np.float32([[1, 0, quarter_width], [0, 1, quarter_height]]) 
img_translation = cv2.warpAffine(image, T, (width, height)) 

cv2.imshow("Originalimage", image) 
cv2.imshow('Translation', img_translation)
cv2.imwrite('Translation.jpg', img_translation) 
cv2.waitKey()
cv2.destroyAllWindows()
