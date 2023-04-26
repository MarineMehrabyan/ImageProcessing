import cv2
import numpy as np
import matplotlib.pyplot as plt

'''The purpose of the code is to perform histogram matching, which is a technique for adjusting the pixel values of an image to match the distribution of pixel values in a reference image. Histogram matching can be used for various applications such as improving the contrast and brightness of an image, and color correction in image processing.'''

def histogram_matching(source_img_path, reference_img_path):

    # Read the source and reference images
    source_img = cv2.imread(source_img_path, 0)
    reference_img = cv2.imread(reference_img_path, 0)

    # Calculate the histograms of the source and reference images
    source_hist, _ = np.histogram(source_img.flatten(), 256, [0, 256])
    reference_hist, _ = np.histogram(reference_img.flatten(), 256, [0, 256])

    # Calculate the cumulative distribution functions (CDF) of the histograms
    # The CDF of a histogram is a way of representing the cumulative probability distribution of the pixel intensities in the image.
    
    # first calculate the cumulative sum of the histogram values. For example, the cumulative sum of a histogram at bin i is the sum of all the histogram values from bin 0 to bin i. This gives us a new array that represents the CDF.
    source_cdf = source_hist.cumsum()
    
    # we normalize the CDF values by dividing them by the maximum value of the CDF. This normalization step is done to ensure that the range of the CDF is between 0 and 1, which makes it easier to work with.
    source_cdf_normalized = source_cdf / source_cdf.max()
    
    
    # Repeat these steps for reference image
    reference_cdf = reference_hist.cumsum()
    reference_cdf_normalized = reference_cdf / reference_cdf.max()

    # Calculate the lookup table for mapping pixel values
    # is used to create a lookup table for mapping the pixel values of the source image to the corresponding pixel values in the reference image.
    # provides a sequence of 256 equally spaced values from 0 to 255
    lookup_table = np.interp(source_cdf_normalized, reference_cdf_normalized, range(256))

    # Map the pixel values of the source image using the lookup table
    # The source_img.flatten() function is used to convert the 2D source image to a 1D array, so that each pixel value can be easily mapped using the lookup table. The reshape(source_img.shape) function is then used to convert the 1D array back to a 2D array with the same shape as the original source image. This creates the final matched image. 
    #The range(256) argument specifies the source pixel values that need to be mapped to their matched values in the lookup table, and the lookup_table argument specifies the matched values that need to be returned.
    matched_img = np.interp(source_img.flatten(), range(256), lookup_table).reshape(source_img.shape)

    # Display the original and matched images and their histograms
    fig, axs = plt.subplots(2, 2, figsize=(12, 10))
    axs[0, 0].imshow(source_img, cmap='gray')
    axs[0, 0].set_title('Source Image')
    
    axs[0, 1].imshow(reference_img, cmap='gray')
    axs[0, 1].set_title('Reference Image')
    
    axs[1, 0].imshow(matched_img, cmap='gray')
    axs[1, 0].set_title('Matched Image')
    
    axs[1, 1].plot(source_hist, color='b')
    axs[1, 1].plot(reference_hist, color='g')
    axs[1, 1].set_title('Histogram')
    axs[1, 1].legend(('Source', 'Reference'))
    plt.show()


# Example usage
histogram_matching('source.jpeg', 'reference.jpeg')

