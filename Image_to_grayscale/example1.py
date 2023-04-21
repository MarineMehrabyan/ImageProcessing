import cv2

# Load the image
img = cv2.imread("Image1.jpg")

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Display the original and grayscale images side-by-side
cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

