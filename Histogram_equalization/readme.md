__________Histogram Equalization__________

Histogram equalization is a technique used in image processing to enhance the contrast of an image. The main idea is to stretch the intensity values of an image so that the full range of intensity values is utilized. This is done by mapping the original intensity values to new values such that the cumulative distribution function (CDF) of the image is approximately uniform.

The process involves calculating the histogram of an image, which is a frequency distribution of the intensity values in the image. The histogram shows how many pixels have each intensity value. Then, the cumulative distribution function (CDF) of the histogram is calculated. This function gives the cumulative sum of the frequency of pixels up to a particular intensity value.

Next, the CDF is normalized to map the values to the range [0, 1]. The normalized CDF is then used to transform the intensity values of the image to new values, such that the resulting histogram is approximately uniform. This is done by finding the closest intensity value in the normalized CDF for each pixel in the image and assigning the corresponding new value.

The result is an image with improved contrast, where the darker and lighter areas of the image are better differentiated, and details in the mid-range of intensity values are enhanced. Histogram equalization is a simple and effective method for enhancing the visual appearance of an image, but it may also introduce artifacts such as noise amplification and loss of detail in some cases.
____Usage____
To use the code, simply run the __equalize_hist.py__ file, which will read in an image and perform histogram equalization on it. The equalized image and its histogram will be displayed side by side using matplotlib.

The input image should be in JPEG format and should be placed in the same directory as the __equalize_hist.py__ file. The name of the image file should be specified in the __cv2.imread__ function call in the main block of the code.

____Code Structure____
The code is organized into several functions that perform the different steps of the histogram equalization process. The main function, __equalize_hist__, takes an input image and returns the equalized image and the normalized cumulative distribution function (CDF) of the image.

The histogram function calculates the histogram of an image by counting the number of pixels with each intensity value. The normalize function normalizes an array to the range [0, 255] using the minimum and maximum values of the array.

The plot_histogram function plots the histogram of an image, while the plot_images function displays the original and equalized images side by side, along with their respective histograms.


