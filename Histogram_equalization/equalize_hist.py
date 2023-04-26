import cv2
import numpy as np
import matplotlib.pyplot as plt


def histogram(image, bins=256):
    """
    Calculates the histogram of an image by counting the number of pixels with each intensity value.
    """
    histogram = np.zeros(bins)
    for pixel in image.flatten():
        histogram[pixel] += 1
    return histogram


def normalize(entries):
    """
    Normalizes an array to the range [0, 255].
    """
    numerator = (entries - np.min(entries)) * 255
    denominator = np.max(entries) - np.min(entries)
    result = numerator / denominator
    return result.astype('uint8')


def equalize_hist(image):
    """
    Performs histogram equalization on an input image.
    """
    hist = histogram(image)
    cdf = hist.cumsum()
    cdf_normalized = normalize(cdf)
    equalized_image = cdf_normalized[image]
    return equalized_image, cdf_normalized


def plot_histogram(image, ax, title):
    """
    Plots the histogram of an image.
    """
    ax.hist(image.flatten(), 256, [0, 256])
    ax.set_title(title)


def plot_images(original, equalized):
    """
    Displays the original and equalized images side by side, along with their respective histograms.
    """
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
    equalized_image, normalized_cdf = equalize_hist(image)
    plot_images(image, equalized_image)

