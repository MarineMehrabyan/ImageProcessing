import copy
import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

''' 
    The code implements contrast stretching, which is a technique used to enhance the contrast of an image by increasing the dynamic range of pixel intensities. The algorithm works by mapping the original pixel intensities to a new range of values, which typically spans the entire intensity range. This can help to reveal more detail in dark or bright areas of an image that might otherwise be difficult to see. The implementation in this code appears to use a histogram-based approach to determine the appropriate mapping of pixel intensities.
'''
class contrastStretch:
    def __init__(self):
        self.img = ""
        self.original_image = ""
        self.last_list = []
        self.rem = 0
        self.L = 256
        self.sk = 0
        self.k = 0
        self.number_of_rows = 0
        self.number_of_cols = 0

    def stretch(self, input_image):
        self.img = cv2.imread(input_image, 0)
        self.original_image = copy.deepcopy(self.img)
        
       
        x, _, _ = plt.hist(self.img.ravel(), 256, [0, 256], label="x")
        self.k = np.sum(x)
        
        '''the cumulative distribution function (CDF) is calculated using the formula last = (self.L - 1) * self.sk. self.L is set to 256, which is the maximum value of a pixel in an 8-bit grayscale image. self.sk is the sum of the probabilities of each pixel value in the image.'''
        for i in range(len(x)):
            prk = x[i] / self.k
            self.sk += prk
            last = (self.L - 1) * self.sk
            if self.rem != 0:
                self.rem = int(last % last)
            last = int(last + 1 if self.rem >= 0.5 else last)
            self.last_list.append(last)
            self.number_of_rows = int(np.ma.count(self.img) / self.img[1].size)
            self.number_of_cols = self.img[1].size
            
            
            
        for i in range(self.number_of_cols):
            for j in range(self.number_of_rows):
                num = self.img[j][i]
                if num != self.last_list[num]:
                    self.img[j][i] = self.last_list[num]


    def plotHistogram(self):
        plt.hist(self.img.ravel(), 256, [0, 256])

    def showImage(self):
        cv2.imshow("Output-Image", self.img)
        cv2.imshow("Input-Image", self.original_image)
        cv2.waitKey()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    stretcher = contrastStretch()
    stretcher.stretch("image.jpeg")
    stretcher.plotHistogram()
    stretcher.showImage()
    plt.show()
