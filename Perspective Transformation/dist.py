import numpy as np
import cv2 
from matplotlib import pyplot as plt 
'''
This code performs perspective correction on an input image.
e purpose of perspective correction is to remove any 
distortions that may have occurred due to the camera's 
angle or position when the image was taken.
'''
  
# read the image 
img = cv2.imread('chDistorted.jpeg') 

# convert image to gray scale image 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# detect corners with the goodFeaturesToTrack function.
'''It takes the following arguments:
gray: the grayscale image to detect corners in.
maxCorners: the maximum number of corners to be detected. 
            If there are more corners than this, 
            only the strongest ones are returned.
qualityLevel: the minimum quality level below which corners
               are rejected. This is a value between 0 and 1.
               Higher values produce more accurate and 
               fewer corners.
minDistance: the minimum distance between detected corners. 
             If the distance between two corners is less than
            this value, one of them is rejected.
In the code you provided, gray is the grayscale version of the 
input image img, maxCorners is set to 27, qualityLevel is set 
to 0.01, and minDistance is set to 10. 
Generally, a higher qualityLevel produces fewer but more 
accurate corners, while a smaller minDistance results in more
corners being detected.

After cv2.goodFeaturesToTrack() returns the detected corners,
np.int0() is used to convert the floating-point coordinates 
of the corners to integers. This is necessary because the 
cv2.circle() function used later requires integer coordinates.
'''

corners = cv2.goodFeaturesToTrack(gray, 27, 0.01, 10)
corners = np.int0(corners) 
  
# we iterate through each corner,  
# making a circle at each point that we think is a corner. 
for i in corners: 
    x, y = i.ravel() 
    cv2.circle(img, (x, y), 3, 255, -1)

(h,w) = img.shape[:2]

#  defining two sets of points,
''' "pts1" is a set of four points that define the corners of 
a rectangle in the original image. "pts2" is a set of four 
points that correspond to the same corners in the corrected 
image. The values for "pts2" have been manually selected based
on the original image and the desired corrected output.'''
pts1=np.float32([[0,0],[0,h],[w,0],[w,h]])
pts2=np.float32([(7.17803, 6.05628),(67.6975,198.332),(209.54, 50.1851),(231.604, 226.7)])

# the transformation matrix
m = cv2.getPerspectiveTransform(pts2,pts1)
# The transformation matrix "m" is then applied to the
# original image using the "warpPerspective" function,
# resulting in the perspective-corrected image
img = cv2.warpPerspective(img,m,(w,h))

cv2.imshow('Perspective', img)
plt.imshow(img)
cv2.waitKey()
cv2.destroyAllWindows()

