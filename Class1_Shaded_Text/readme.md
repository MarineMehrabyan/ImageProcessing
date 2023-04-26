_____Better processing of the shaded text image for Class 1_____

This code performs image enhancement using the unsharp masking technique. It imports necessary libraries such as skimage, OpenCV, numpy, and glob. It reads in all images with the extensions .jpg, .jpeg, and .png present in the same directory as the script using the glob module.

__For each image in the file list, it applies the following steps:__

Converts the image to grayscale using OpenCV's "cvtColor" function. This is necessary because the unsharp masking technique requires a single-channel (i.e., grayscale) input image.

Applies Gaussian blur to the grayscale image using OpenCV's "GaussianBlur" function. The blur is applied to reduce noise and unwanted details in the image, which can interfere with the unsharp masking process.

Divides the grayscale image by the blurred image. This creates an "edge image" that highlights the edges and features in the original image. The division is scaled by 255 to normalize the values between 0 and 1.

Performs unsharp masking on the edge image using the "unsharp_mask" function from the skimage library. Unsharp masking is a process that enhances edges and fine details in an image by subtracting a blurred version of the image from the original.

Converts the resulting sharpened image data into a valid image format that can be displayed using OpenCV's "imshow" function. The "unsharp_mask" function from the skimage library returns an image in a floating-point format, which means the pixel values can be outside the range of [0, 255] and cannot be directly displayed as an image.

Displays the original and sharpened image side by side using OpenCV's "imshow" function.

Waits for a key press before moving on to the next image.





After processing all images, the code closes all open windows using OpenCV's "destroyAllWindows" function.

Note: The parameters for GaussianBlur, unsharp_mask, and the size of the kernel in division can be adjusted to achieve different levels of image enhancement.










