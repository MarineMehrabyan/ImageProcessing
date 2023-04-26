import cv2
import numpy as np
import glob

# This function takes in a folder path and returns a list of all image files in that folder
def get_images(folder_path):
    img_files = []
    for file_type in ('*.jpeg', '*.jpg', '*.png'):
        img_files.extend(glob.glob(folder_path + file_type))
    return img_files

#This function takes in an image, converts it to grayscale, and i 
#It returns the gray image and the initial Canny threshold values.
def process_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    canny_thresh1 = 50
    canny_thresh2 = 100
    return gray, canny_thresh1, canny_thresh2


# This function creates trackbars for adjusting the Canny threshold values and displays the resulting edges.
def display_edges(gray, canny_thresh1, canny_thresh2):
    cv2.namedWindow('Canny Edge Detector', cv2.WINDOW_NORMAL)
    cv2.createTrackbar('Threshold 1', 'Canny Edge Detector', canny_thresh1, 255, lambda x: None)
    cv2.createTrackbar('Threshold 2', 'Canny Edge Detector', canny_thresh2, 255, lambda x: None)
    
    while True:
        # Get the current values of the trackbars
        canny_thresh1 = cv2.getTrackbarPos('Threshold 1', 'Canny Edge Detector')
        canny_thresh2 = cv2.getTrackbarPos('Threshold 2', 'Canny Edge Detector')
        
        # Apply the Canny edge detector with the current threshold values
        edges = cv2.Canny(gray, canny_thresh1, canny_thresh2)
        
        cv2.imshow('Canny Edge Detector', edges)
        key = cv2.waitKey(1) & 0xFF
        # If the 'q' key is pressed, exit the loop
        if key == ord('q'):
            break

    cv2.destroyAllWindows()




folder_path = "images/"
img_files = get_images(folder_path)

for img_file in img_files:
    img = cv2.imread(img_file)
    gray, canny_thresh1, canny_thresh2 = process_image(img)
    display_edges(gray, canny_thresh1, canny_thresh2)




