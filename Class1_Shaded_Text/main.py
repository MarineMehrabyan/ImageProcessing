import skimage.filters as filters
import cv2
import numpy as np
import glob

file_list = glob.glob("*.jpg") + glob.glob("*.jpeg") + glob.glob("*.png")

for filename in file_list:
    img = cv2.imread(filename)

    #This is necessary because the unsharp masking technique requires a single-channel (i.e., grayscale) input image.
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #The blur is applied to reduce noise and unwanted details in the image, which can interfere with the unsharp masking process.
    smooth = cv2.GaussianBlur(gray, (33,33), 0)
    
    #This divides the grayscale image by the blurred image. This creates an "edge image" that highlights the edges and features in the original image. The division is scaled by 255 to normalize the values between 0 and 1.
    division = cv2.divide(gray, smooth, scale=255)
    
    
    #Unsharp masking is a process that enhances edges and fine details in an image by subtracting a blurred version of the image from the original. In this step, a sharpened version of the image is obtained by subtracting the blurred division image from the division image.
    sharp = filters.unsharp_mask(division, radius=1.5, amount=2.5, preserve_range=False)

    # it converts the image data into a valid image format that can be displayed using OpenCV's "imshow" function.
    #The "unsharp_mask" function from the skimage library returns an image in a floating-point format, which means the pixel values can be outside the range of [0, 255] and cannot be directly displayed as an image
    finished = (255*sharp).clip(0,255).astype(np.uint8)

    # show results
    cv2.imshow('original', img)
    cv2.imshow('finished', finished) 
    cv2.waitKey(0)
cv2.destroyAllWindows()

