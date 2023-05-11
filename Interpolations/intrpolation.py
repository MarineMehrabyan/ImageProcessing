import cv2
import numpy as np
'''Interpolation is used in tasks such as zooming, shrinking, rotating, 
and geometrically correcting digital images. It is the process of using 
known data to estimate values at unknown locations. So for giving the 
chance to estimate values, we will do some transformation, here it is a 
rotation by 45 degrees. The 3 interpolations we see here are:
1. Nearest Neighbour	
2. Bilinear	
3. Bicubic	
Here you can see a slight variation between the 3 images. 
The smoothness gets better from left to right.  Since Bicubic interpolation 
uses a higher-order equation it can capture features in-depth.
This code performs a rotation and scaling operation on an image
These operations can be used for various applications, such as image
 registration, image alignment, and image analysis. '''
img = cv2.imread('panda.jpg', 0)
(h,w) = img.shape[:2]   # the center point of the image
center = (w/2, h/2)
angle45 = 45
scale = 1.0

M = cv2.getRotationMatrix2D(center, angle45, scale)

abs_cos = abs(M[0,0]) 
abs_sin = abs(M[0,1])


bound_w = int(h * abs_sin + w * abs_cos)
bound_h = int(h * abs_cos + w * abs_sin)

#  affine transformation matrix
M[0, 2] += bound_w/2 - center[0]
M[1, 2] += bound_h/2 - center[1]

# The matrix M is used to rotate the image by 30 degrees
rotated30 = cv2.warpAffine(img, M, (bound_w,bound_h))

# cv2.imshow('Original Image', img)
# cv2.imshow('Rotated by 30', rotated30)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# it is then scaled to 110% of its original size using cv2.resize()
# function with three different interpolation methods:
scale_percent = 110
width = int(rotated30.shape[1] * scale_percent / 100)
height = int(rotated30.shape[0] * scale_percent / 100)
dim = (width, height)

# These methods are used to perform different types of interpolation
# to obtain the new pixel values after scaling the image.
scaled = cv2.resize(rotated30, dim, interpolation=cv2.INTER_NEAREST)
scaled1 = cv2.resize(rotated30, dim, interpolation=cv2.INTER_LINEAR)
scaled2 = cv2.resize(rotated30, dim, interpolation=cv2.INTER_CUBIC)

cv2.imshow("Nearest Neighbour", scaled)
cv2.imshow("Bilinear", scaled1)
cv2.imshow("Bicubic", scaled2)

cv2.imwrite("Nearest Neighbour.jpg", scaled)
cv2.imwrite("Bilinear.jpg", scaled1)
cv2.imwrite("Bicubic.jpg", scaled2)
cv2.waitKey(0)
cv2.destroyAllWindows() 