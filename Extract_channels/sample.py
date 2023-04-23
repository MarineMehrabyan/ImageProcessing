import cv2

# Load the image
try:
    img = cv2.imread('image.jpg')
    if img is None:
        raise ValueError("Image file not found or cannot be loaded.")
except Exception as e:
    print("Error:", str(e))
    exit()

# Split the image into its color channels
try:
    b,g,r = cv2.split(img)
except ValueError as e:
    print("Error:", str(e))
    exit()

# Display each channel
cv2.imshow('Blue Channel', b)
cv2.imshow('Green Channel', g)
cv2.imshow('Red Channel', r)
cv2.waitKey(0)
cv2.destroyAllWindows()

