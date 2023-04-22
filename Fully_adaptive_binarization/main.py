import cv2
import numpy as np
# glob provides functions to search for files and directories whose names match a specified pattern
import glob

# Define a list of kernel sizes to try
kernel_sizes = [(3, 3), (5, 5), (7, 7), (9, 9), (11, 11), (13, 13), (15, 15), (17, 17), (19, 19), (21, 21), (23, 23), (25, 25)]

# Define a list of k values to try
k_values = np.arange(0.05, 0.55, 0.05)


# Get a list of all files with .jpg, .jpeg, or .png extensions in the current directory
file_list = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png")

# Iterate over all files in the list
for filename in file_list:
    # Load image and convert to grayscale
    img = cv2.imread(filename)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #get the best Gaussian blur kernel size for the current image
    # Initialize variables to keep track of the best kernel size and best quality
    best_kernel_size = None
    best_quality = None

    # Iterate over kernel sizes and evaluate the resulting image quality
    for kernel_size in kernel_sizes:
        # Apply Gaussian blur
        blur = cv2.GaussianBlur(gray, kernel_size, 0)

        # Compute a quality metric (e.g. mean squared error, structural similarity index, etc.)
        # Here, we simply use the variance of the image as a quality metric
        quality = np.var(blur)

        # Update the best kernel size and quality if the current one is better
        if best_quality is None or quality > best_quality:
            best_kernel_size = kernel_size
            best_quality = quality

    # Apply the chosen kernel size to the original image
    blur = cv2.GaussianBlur(gray, best_kernel_size, 0)




    # Initialize variables to keep track of the best k value and best quality
    best_k = None
    best_quality = None

    # Iterate over k values and evaluate the resulting image quality
    for k in k_values:
        R = np.max(blur) - np.min(blur)
        threshold = np.mean(blur) * (1 + k * ((R / 256) - 1))
        th = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)[1]

        # Compute a quality metric 
        # we simply use the variance of the binary image as a quality metric
        quality = np.var(th)

        # Update the best k value and quality if the current one is better
        if best_quality is None or quality > best_quality:
            best_k = k
            best_quality = quality

    # Apply the chosen k value to the original image
    R = np.max(blur) - np.min(blur)
    threshold = np.mean(blur) * (1 + best_k * ((R / 128) - 1))
    th = cv2.threshold(blur, threshold, 255, cv2.THRESH_BINARY)[1]

    print(f"Optimized k value for {filename}: {best_k}")
    
    # Show the binary image
    cv2.imshow('Original Image', img)
    cv2.imshow('Binary Image', th)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    

