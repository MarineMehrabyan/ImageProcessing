____Fully adaptive image binarization____

This Python script applies image thresholding to a set of input images using adaptive thresholding. It uses OpenCV and NumPy libraries for image processing.

____Requirements____

Python 3.x
OpenCV
NumPy

____Installation____

You can install OpenCV and NumPy using pip:
_pip install opencv-python_
_pip install numpy_


____Usage____

1. Place your input images (in .jpg, .jpeg, or .png format) in the same directory as the script.
2. Modify the kernel_sizes and k_values variables to adjust the range of values to try.
3. Run the script using the command _python3 main.py_
4. The script will iterate over all images in the directory, apply adaptive thresholding, and display the original and thresholded images.

____Explanation____

The script performs the following steps for each input image:

1. Load the image and convert it to grayscale.
2. Determine the best Gaussian blur kernel size for the image by iterating over a range of kernel sizes and evaluating the resulting image quality. The quality metric used in this script is the variance of the blurred image.
3. Apply the chosen kernel size to the original image to produce a blurred image.
4. Determine the best value of k for the adaptive thresholding by iterating over a range of k values and evaluating the resulting image quality. The quality metric used in this script is the variance of the binary image produced by the thresholding operation.
5. Apply the chosen k value to the blurred image using adaptive thresholding to produce a binary image.
6. Display the original and binary images.
