import cv2
import numpy as np

def apply_max_filter(image, kernel_size):
    # Create a kernel of ones with size kernel_size x kernel_size
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    # Apply dilation with the kernel to obtain the maximum value in the neighborhood of each pixel
    max_filtered_image = cv2.dilate(image, kernel, iterations=1)
    return max_filtered_image

def on_trackbar(val):
    # Update the kernel size and apply the max filter
    kernel_size = val * 2 + 1
    filtered_image = apply_max_filter(img, kernel_size)
    # Show the filtered image
    cv2.imshow("Max Filter", filtered_image)

# Load an example image
img = cv2.imread("img5.jpeg")

# Create a window to display the filtered image
cv2.namedWindow("Max Filter")

# Set an initial kernel size of 3x3
kernel_size = 3

# Create a trackbar to adjust the kernel size
cv2.createTrackbar("Kernel Size", "Max Filter", kernel_size//2, 10, on_trackbar)

# Call the on_trackbar function to display the initial filtered image
on_trackbar(kernel_size//2)

# Wait for the user to close the window
cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()

