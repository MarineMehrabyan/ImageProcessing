import cv2
import glob

# define the image file extensions
extensions = ['*.jpeg', '*.jpg', '*.png']

# loop through each image
for ext in extensions:
    for file in glob.glob(ext):
        # read the image and convert to grayscale
        img = cv2.imread(file, cv2.IMREAD_GRAYSCALE)

        # perform Gaussian smoothing to reduce noise
        blur = cv2.GaussianBlur(img, (5,5), 0)

        # perform binary thresholding
        ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

        # perform morphological opening to remove small noise and fill small gaps
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
        opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel)

        # perform morphological closing to remove small spots
        closing_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2,2))
        closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, closing_kernel)


        # display the original and modified images side-by-side
        cv2.imshow("Original Image", img)
        cv2.imshow("Noise-Reduced Image", closing)
        cv2.waitKey(0)



cv2.destroyAllWindows()

