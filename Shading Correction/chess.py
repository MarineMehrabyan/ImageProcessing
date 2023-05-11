import cv2
'''
The main purpose of this code is to apply image processing 
techniques to an input image of a chessboard and generate 
a new image with an enhanced contrast

These codes perform the following operations:

1. Reads an image named 'ChessBoardGrad.png' using the cv2.imread() method.
2. Converts the color image into a grayscale image using the cv2.cvtColor() method.
3. Displays the grayscale image using the cv2.imshow() method.
4. Waits for the user to press any key to proceed to the next step using the cv2.waitKey() method.
5. Applies a Gaussian filter to the grayscale image using the cv2.GaussianBlur() method with a kernel size of (filtersize, filtersize) and a standard deviation of 128.
6. Displays the filtered image using the cv2.imshow() method.
7. Waits for the user to press any key to proceed to the next step using the cv2.waitKey() method.
8. Subtracts the filtered image from the grayscale image to get a new image.
9. Displays the new image using the cv2.imshow() method.
10. Writes the new image to a file named 'Converted.png' using the cv2.imwrite() method.
11. Waits for the user to press any key to close all the windows using the cv2.waitKey() method.
12. Closes all the windows using the cv2.destroyAllWindows() method.

This code is used to subtract the Gaussian filtered image 
from the grayscale image to get a new image. 
This technique is used to enhance edges and features in an 
image. The larger the kernel size of the Gaussian filter,
the more the blur applied to the image. 
By subtracting the blurred image from the original image,
we can get a sharper version of the original image.
'''

img = cv2.imread('ChessBoardGrad.png')

grayImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', grayImg)
cv2.waitKey(0)

filtersize = 513
gaussianImg = cv2.GaussianBlur(grayImg, (filtersize, filtersize), 128)

cv2.imshow('Converted Image', gaussianImg)
cv2.waitKey(0)

newImg = (grayImg-gaussianImg)
cv2.imshow('New Image', newImg)
cv2.imwrite('Converted.png', newImg)
cv2.waitKey(0)
cv2.destroyAllWindows()