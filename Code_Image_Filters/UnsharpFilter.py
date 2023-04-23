import cv2
import numpy as np

def apply_unsharp_filter(image, ksize, sigma, alpha):
    # apply Gaussian blur
    if ksize % 2 == 0:
        ksize += 1
    blurred_image = cv2.GaussianBlur(image, (ksize, ksize), sigma)
    
    # calculate the difference between the original and blurred images
    diff = cv2.subtract(image, blurred_image)
    
    # apply unsharp filter
    sharpened_image = cv2.addWeighted(image, 1 + alpha, diff, -alpha, 0)
    
    return sharpened_image
    
    
def on_trackbar(val):
    global ksize, sigma, alpha, img
    
    ksize = cv2.getTrackbarPos('Kernel Size', 'Unsharp Filter')
    sigma = cv2.getTrackbarPos('Sigma', 'Unsharp Filter')
    alpha = cv2.getTrackbarPos('Alpha', 'Unsharp Filter') / 10
    
    sharpened_image = apply_unsharp_filter(img, ksize, sigma, alpha)
    cv2.imshow('Unsharp Filter', sharpened_image)

# Load the image
img = cv2.imread('img6.jpeg')

# Create a window and trackbars to adjust parameters
cv2.namedWindow('Unsharp Filter')
cv2.createTrackbar('Kernel Size', 'Unsharp Filter', 3, 15, on_trackbar)
cv2.createTrackbar('Sigma', 'Unsharp Filter', 1, 10, on_trackbar)
cv2.createTrackbar('Alpha', 'Unsharp Filter', 1, 30, on_trackbar)

# Initialize parameters
ksize = 3
sigma = 1
alpha = 0.1

# Apply the unsharp filter with the initial parameters
sharpened_image = apply_unsharp_filter(img, ksize, sigma, alpha)
cv2.imshow('Unsharp Filter', sharpened_image)

# Wait for a key press and then close the window
cv2.waitKey(0)
cv2.destroyAllWindows()

