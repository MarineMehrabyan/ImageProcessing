import cv2
import glob
import numpy as np

# Get a list of all files with .jpg, .jpeg, or .png extensions in the current directory
file_list = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png")

# Iterate over all files in the list
for filename in file_list:
    # Load the image
    image = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

    # Define the kernel size of the Mean Filter, which must be an odd number to ensure that the kernel has a well-defined center.
    kernel_size = 5
    #generate the kernel for the Mean Filter using a numpy array of ones with the same dimensions as the kernel size. We divide this kernel by the sum of all its elements to ensure that the output is properly normalized
    kernel = np.ones((kernel_size, kernel_size), dtype=np.float32) / (kernel_size**2)

    #  Apply the Mean Filter to the input image using convolution with cv2.filter2D. We pass -1 as the second argument to the function to indicate that we want the output image to have the same depth as the input image.
    mean_filtered = cv2.filter2D(image, -1, kernel)

    # horizontally concatenate the original and filtered images using cv2.hconcat and store the resulting image in comparison
    comparison = cv2.hconcat([image, mean_filtered])

    # Display the comparison image and wait for a key press
    cv2.imshow('Original vs Mean Filtered', comparison)
    cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()

