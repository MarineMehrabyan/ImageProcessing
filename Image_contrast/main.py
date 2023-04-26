import cv2

def adjust_contrast(img, contrast):
        #function takes an image and a contrast value as input, and returns the adjusted image. The contrast value is specified within the range of -100 to +100, with 0 being no adjustment, -100 being maximum decrease in contrast, and +100 being maximum increase in contrast.
        
    # The contrast adjustment formula
    # factor value is used to adjust the pixel values of the image to achieve the desired contrast level
    factor = (259 * (contrast + 255)) / (255 * (259 - contrast))
    img = cv2.addWeighted(img, factor, img, 0, 0)
    return img

# Callback function for the trackbar.
def on_trackbar(val):
    contrast = val - 100
    img_contrast = adjust_contrast(img_original, contrast)
    cv2.imshow("Image", img_contrast)


img_original = cv2.imread("cat.jpg")
cv2.namedWindow("Image")

# Create a trackbar to adjust the contrast
cv2.createTrackbar("Contrast", "Image", 100, 200, on_trackbar)

# Show the original image
cv2.imshow("Image", img_original)
cv2.waitKey(0)
cv2.destroyAllWindows()

