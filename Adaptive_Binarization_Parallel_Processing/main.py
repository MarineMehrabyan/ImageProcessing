import cv2
import numpy as np
import math
import time
import os
import multiprocessing as mp
import concurrent.futures # Concurrent library for parallel processing
import threading # Threading library for concurrent execution
import queue # Queue library for multi-threading support
import glob # Glob library for file search and pattern matching


# The function applies adaptive binarization to the input image and returns the binarized output image.
def adaptive_binarization(img, block_size, constant):
    """
    Applies adaptive binarization to an input grayscale image.

    Parameters:
    img (numpy.ndarray): The input grayscale image.
    block_size (int): The size of the adaptive thresholding window.
    constant (int): A constant subtracted from the mean or weighted mean.

    Returns:
    numpy.ndarray: The binarized output image.
    """
    
    #gets the height and width of the input image and creates a numpy array of zeros with the same height and width. This numpy array will store the binarized output image
    img_height, img_width = img.shape[:2]
    thresholded = np.zeros((img_height, img_width), np.uint8)

    #divides the input image into blocks of size block_size x block_size. For each block, the function calculates an adaptive threshold using the cv2.adaptiveThreshold() function and applies it to the block. The resulting binarized block is then stored in the thresholded numpy array.
    for i in range(0, img_height, block_size):
        for j in range(0, img_width, block_size):
            block = img[i:i + block_size, j:j + block_size]
            # Calculate the adaptive threshold for this block
            threshold = cv2.adaptiveThreshold(block, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, block_size, constant)
            thresholded[i:i + block_size, j:j + block_size] = threshold
    
    return thresholded # the binarized output image

if __name__ == '__main__':
    # Get a list of image files in the current directory
    file_list = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png")
    # defines the block size and constant that will be used for adaptive thresholding, as well as the number of parallel processes to use.
    block_size = 51
    constant = 10
    num_processes = 4

    # Create a process pool with the specified number of processes
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        #divides the image into sections for parallel processing using np.array_split(). It then applies adaptive binarization to each image section in parallel using executor.map(), and combines the thresholded sections into a single output image using np.concatenate()
        for filename in file_list:
            # Load the input grayscale image
            img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
            # Show the original image

            # Divide the image into sections for parallel processing
            img_sections = np.array_split(img, num_processes)
            # Apply adaptive binarization to each image section in parallel
            thresholded_sections = list(executor.map(adaptive_binarization, img_sections, [block_size]*num_processes, [constant]*num_processes))
            # Combine the thresholded sections into a single output image
            thresholded = np.concatenate(thresholded_sections)
            # Show the binarized image
            cv2.imshow('Original Image', img)
            cv2.imshow('Binarized Image', thresholded)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

