import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def region_growing(img, seed, threshold):
    # Create a binary mask of the image
    mask = np.zeros_like(img)
    # Set the seed point to be 1 in the mask
    mask[seed[0], seed[1]] = 1

    # Define 8-connectivity neighbors
    neighbors = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]

    # Start growing the region
    while True:
        # Copy the current mask to a temporary variable
        temp_mask = np.copy(mask)
        # Loop through the mask and grow the region if a neighboring pixel meets the threshold
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if temp_mask[i, j] == 1:
                    for neighbor in neighbors:
                        ni = i + neighbor[0]
                        nj = j + neighbor[1]
                        # Make sure the neighbor is within the image bounds
                        if 0 <= ni < img.shape[0] and 0 <= nj < img.shape[1]:
                            # Check if the neighbor meets the threshold
                            if abs(img[i, j] - img[ni, nj]) <= threshold and mask[ni, nj] == 0:
                                mask[ni, nj] = 1
        # Check if the mask has changed, if not we have grown the entire region
        if np.array_equal(mask, temp_mask):
            break

    return mask


if __name__ == "__main__":
    # Load the image and convert to grayscale
    img = Image.open("img.png").convert('L')
    img = np.array(img)
    # Set the seed point and threshold
    seed = (150, 150)
    threshold = 10
    # Apply the region growing algorithm
    mask = region_growing(img, seed, threshold)
    # Display the original image and the resulting mask
    fig, axs = plt.subplots(1, 2, figsize=(10, 5))
    axs[0].imshow(img, cmap='gray')
    axs[0].plot(seed[1], seed[0], 'ro')
    axs[0].set_title("Original Image")
    axs[1].imshow(mask, cmap='gray')
    axs[1].set_title("Resulting Mask")
    plt.savefig('result2.png')

    plt.show()
