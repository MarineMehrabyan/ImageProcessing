import cv2

# Load the grayscale image
img = cv2.imread('image3.jpg', 0)

# Apply Gaussian blur to reduce noise
img = cv2.GaussianBlur(img, (5, 5), 0)

# Apply adaptive thresholding
th = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

# Show original and thresholded images
cv2.imshow('Original Image', img)
cv2.imshow('Adaptive Thresholded Image', th)

cv2.waitKey(0)
cv2.destroyAllWindows()
