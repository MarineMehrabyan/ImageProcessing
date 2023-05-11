import cv2
import numpy as np
'''The images are rotated using the self-defined code for rotation
instead of the OpenCV inbuilt function. When an image is rotated
by 45 degrees for 8 times, it does not produce the same result as
when it is rotated by 90 degrees for 4 times. This is because,
when an image is rotated 45 degrees, during the rotation more 
pixels values for the new position of the pixels are to be calculated.
And calculating these new pixel positions and their intensities uses 
interpolation which is an approximation method. So when an image is 
rotated by 90 degrees there is a smoother transition since fewer no 
of approximations are to be made for the new pixel positions and 
their intensities.
A clear example is shown below'''

img = cv2.imread('8.jpg')
(h,w) = img.shape[:2] # height and width of the image
center = (w/2, h/2)   # the center point of the image
angle45 = 45		  # rotation angle
angle90 = 90          # rotation angle
scale = 1.0			  # the scale factor to 1.0 (no scaling)

# Computes the affine transformation matrix
# M, M2 for rotating the image by 45 and by 90 degrees
M = cv2.getRotationMatrix2D(center, angle45, scale)
M2 = cv2.getRotationMatrix2D(center, angle90, scale)


# The absolute cosine and sine values of the first
# row of each transformation matrix
abs_cos = abs(M[0,0])
abs_sin = abs(M[0,1])

abs_cos = abs(M2[0,0]) 
abs_sin = abs(M2[0,1])


# the width and height of the rotated images
bound_w = int(h * abs_sin + w * abs_cos)
bound_h = int(h * abs_cos + w * abs_sin)

# The translation part of the transformation matrix
# is then updated to ensure that the rotated image
# is centered in the output image. This is done by
# adding the difference between the width and height
# of the bounding rectangle and the original image
# to the corresponding elements of the translation
# vector in the transformation matrix.
M[0, 2] += bound_w/2 - center[0]
M[1, 2] += bound_h/2 - center[1]

M2[0, 2] += bound_w/2 - center[0]
M2[1, 2] += bound_h/2 - center[1]

# function is used to rotate the image by the desired angle
# The function takes the input image, the transformation matrix,
# and the dimensions of the output image as input arguments.
# The resulting rotated image is then used as the input for
# additional rotations in a loop.
rotated45 = cv2.warpAffine(img, M, (bound_w,bound_h))

# The first loop rotates the image by 45 degrees a total of 7 times,
# and the second loop rotates the image by 90 degrees a total of 3 times.
for i in range(7):
	rotated45 = cv2.warpAffine(rotated45, M, (bound_w,bound_h))

rotated90 = cv2.warpAffine(img, M2, (bound_w,bound_h))

for i in range(3):
	rotated90 = cv2.warpAffine(rotated90, M2, (bound_w,bound_h))

cv2.imshow('Rotated by 45 8 times', rotated45)
cv2.imshow('Rotated by 90 4 times', rotated90)
cv2.imwrite('rotated45.jpg',rotated45)
cv2.imwrite('rotated90.jpg',rotated90)
cv2.waitKey(0)
cv2.destroyAllWindows()