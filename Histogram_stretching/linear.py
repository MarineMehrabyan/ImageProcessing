'''the given code implements the linear histogram stretching technique. The stretching is performed by modifying the intensity values of pixels in the input image, based on the histogram of the input image. Specifically, the technique tries to spread the pixel values uniformly across the entire range of intensities in the image (typically 0 to 255), by mapping the original pixel intensities to new values using a linear function. The resulting image will have an increased contrast, making it easier to visualize details in the image.'''


import copy
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt #is a library for creating visualizations.


class LinearStretch:

    def __init__(self):
        self.img = ""
        self.original_image = ""
        self.last_list = []
        self.rem = 0
        self.sk = 0
        self.k = 0
        self.number_of_rows = 0
        self.number_of_cols = 0
    
    #The method performs a linear histogram stretch on the image.
    def stretch(self, input_image):
        self.img = cv2.imread(input_image, 0)
        self.original_image = copy.deepcopy(self.img)

        # Original image histogram
        plt.subplot(2, 2, 1)
        plt.hist(self.img.ravel(), 256, [0, 256])
        plt.title('Original Image Histogram')
        plt.xlim([0, 256])
        plt.ylim([0, 5000])
        # returns a tuple of values (x, bins, and patches)
        x, _, _ = plt.hist(self.img.ravel(), 256, [0, 256], label="x")
        # each element x[i] contains the number of pixels that have intensity value equal to i
        self.k = np.sum(x) # the total number of pixels

        for i in range(len(x)):
            prk = x[i] / self.k # the probability of each intensity level 
            
            self.sk += prk # the cumulative probability up to the current bin 
            
            last = (256 - 1) * self.sk #the intensity value that the current bin should be stretched to
            
            
            #if there is any remainder from the previous bin's intensity value. If so, it is added to the current bin's intensity value.
            if self.rem != 0:
                self.rem = int(last % last)
            
            # rounds the intensity value to the nearest integer.
            last = int(last + 1 if self.rem >= 0.5 else last)
            
            #appends the rounded intensity value to a list
            self.last_list.append(last)
            
            #These two lines calculate the number of rows and columns in the image. 
            self.number_of_rows = int(np.ma.count(self.img) / self.img[1].size)
            self.number_of_cols = self.img[1].size
            
            
            
        # For each pixel, the intensity value is replaced with its stretched value from self.last_list
         
        for i in range(self.number_of_cols):
            for j in range(self.number_of_rows):
                num = self.img[j][i]
                if num != self.last_list[num]:
                    self.img[j][i] = self.last_list[num]
       
        
        # Stretched image histogram
        plt.subplot(2, 2, 2)
        plt.hist(self.img.ravel(), 256, [0, 256])
        plt.title('Stretched Image Histogram')
        plt.xlim([0, 256])
        plt.ylim([0, 5000])

#        cv2.imwrite("output_data/output.jpg", self.img)

    def show_image(self):
        cv2.imshow("Output-Image", self.img)
        cv2.imshow("Input-Image", self.original_image)
        cv2.waitKey(5000)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    stretcher = LinearStretch()
    stretcher.stretch("img.jpg")
    stretcher.show_image()
    plt.show()

