import cv2
import numpy as np
import matplotlib.pyplot as plt


def plot_histogram(image, ax, title):
    # Plots the histogram of an image.
    ax.hist(image.flatten(), 256, [0, 256])
    ax.set_title(title)

'''
    The modified code performs adaptive histogram equalization using OpenCV's createCLAHE method. The clip_limit parameter controls the amount of contrast enhancement, while the grid_size parameter determines the size of the subregions used for local histogram equalization. The resulting equalized_image is the output of the adaptive histogram equalization process.
'''
def adaptive_equalize_hist(image, clip_limit=2.0, grid_size=(8,8)):
    
    # creates an object for Contrast Limited Adaptive Histogram Equalization (CLAHE) with the specified clipLimit and tileGridSize parameters.
    # clipLimit specifies the maximum amount of contrast enhancement applied to each pixel, which can prevent over-enhancement in regions with high contrast.
    # tileGridSize specifies the size of the subregions used for local histogram equalization. The image is divided into a grid of subregions with tileGridSize rows and columns, and histogram equalization is performed independently on each subregion.
    clahe = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=grid_size)
    
    
    #applies the CLAHE transformation to the input image image, returning the resulting equalized image.
    equalized_image = clahe.apply(image)
    return equalized_image

def plot_images(original, equalized):
    # Displays the original and equalized images side by side, along with their respective histograms.
    
    fig, axes = plt.subplots(2, 2, figsize=(10, 7))
    axes[0, 0].imshow(original, cmap='gray')
    axes[0, 0].set_title('Original Image')
    plot_histogram(original, axes[1, 0], 'Histogram of Original Image')
    axes[0, 1].imshow(equalized, cmap='gray')
    axes[0, 1].set_title('Equalized Image')
    plot_histogram(equalized, axes[1, 1], 'Histogram of Equalized Image')
    plt.show()

if __name__ == '__main__':
    image = cv2.imread('image.jpeg', cv2.IMREAD_GRAYSCALE)
    equalized_image = adaptive_equalize_hist(image)
    plot_images(image, equalized_image)

