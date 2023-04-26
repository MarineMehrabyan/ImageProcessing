import cv2
import numpy as np

def apply_gaussian_blur(image, ksize, sigma):
    """
    Applies a Gaussian blur to an image with the specified kernel size and sigma value.
    """
    # Ensure that the kernel size is odd
    if ksize % 2 == 0:
        ksize += 1
    # Apply the Gaussian blur
    blurred_image = cv2.GaussianBlur(image, (ksize, ksize), sigma)

    return blurred_image


def on_trackbar(val):
    """
    Callback function for the trackbar that updates the displayed image as the trackbar is adjusted.
    """
    # Get the current values of the trackbars
    '''kernel size determines the size of the blur, while sigma determines the amount of blur.'''
    
    ksize = cv2.getTrackbarPos('Kernel Size', 'Gaussian Blur')
    sigma = cv2.getTrackbarPos('Sigma', 'Gaussian Blur')

    # Apply the Gaussian blur with the current parameters
    blurred_image = apply_gaussian_blur(img, ksize, sigma)

    # Display the blurred image
    cv2.imshow('Gaussian Blur', blurred_image)


# Load the image
img = cv2.imread('img3.jpeg')

# Create a window to display the image and the trackbars
cv2.namedWindow('Gaussian Blur')

# Create trackbars to adjust the kernel size and sigma value
cv2.createTrackbar('Kernel Size', 'Gaussian Blur', 1, 31, on_trackbar)
cv2.createTrackbar('Sigma', 'Gaussian Blur', 1, 10, on_trackbar)

# Apply the initial blur with the default parameters
blurred_image = apply_gaussian_blur(img, 1, 1)

# Display the blurred image
cv2.imshow('Gaussian Blur', blurred_image)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()

