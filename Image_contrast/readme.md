_____Code the Contrast (-100 to +100)_____

Program that adjusts the contrast of an image by a specified amount within the range of -100 to +100.



This Python code uses the OpenCV library to adjust the contrast of an image. It defines two functions __adjust_contrast__ and __on_trackbar__. The first function, __adjust_contrast__, takes an image and a contrast value as input, and returns the adjusted image. The contrast value is specified within the range of -100 to +100, with 0 being no adjustment, -100 being maximum decrease in contrast, and +100 being maximum increase in contrast.

The second function, __on_trackbar__, is a callback function for the trackbar. It receives a value from the trackbar, which is used to adjust the contrast of the image. It calls the __adjust_contrast__ function with the original image and the contrast value, and displays the adjusted image.

The code reads an image named "cat.jpg" using the __cv2.imread()__ function and displays it using __the cv2.imshow()__ function. It also creates a trackbar named "Contrast" with a range of 0 to 200 and initial value of 100, using the __cv2.createTrackbar()__ function. When the trackbar value is changed, the __on_trackbar__ function is called and the image is adjusted accordingly.



____Requirements_____

This code requires the OpenCV library to be installed. You can install it using pip: __pip install opencv-python__

____Usage____

1. Place an image in the same directory as the code file, and specify the image name in the cv2.imread() function.
2. Run the code using the command python filename.py.
3. Adjust the contrast of the image using the trackbar.


Note: Press any key to close the image window.
