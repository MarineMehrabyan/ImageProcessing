import cv2
import numpy as np
from pyzbar.pyzbar import decode 
import glob

extensions = ['*.jpeg', '*.jpg', '*.png']

# loop over all the images in the current directory with extensions as mentioned in extensions list
for ext in extensions:
    for file in glob.glob(ext):
        img = cv2.imread(file)
        
        # To improve the bounding box of the detected barcode/QR code in the image, we apply some preprocessing techniques like thresholding or edge detection to enhance the barcode/QR code's contrast and edges.
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 120, 255, cv2.THRESH_BINARY)[1]
        
        # decode all the barcodes and QR codes in the current image
        decoded_objs = decode(thresh)

        # iterate over each decoded object
        for obj in decoded_objs:
            # extract the decoded data from the object and convert it into a string
            myData = obj.data.decode("utf-8")
            print(myData)
            
            # extract the polygon (boundary) of the detected barcode/QR code and draw a bounding box around it
            pts = np.array([obj.polygon], np.int32)
            pts = pts.reshape((-1,1,2))
            cv2.polylines(img, [pts], True, (255,0.255), 5)
            
            # extract the position and size of the bounding box and display the decoded data at the top-left corner of the box
            pts2 = obj.rect
            cv2.putText(img, myData, (pts2[0],pts2[1]), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255,0,255), 2)
        
        # display the image with detected barcodes and QR codes
        cv2.imshow("Result", img)
        cv2.waitKey(0)

# close all windows
cv2.destroyAllWindows()

