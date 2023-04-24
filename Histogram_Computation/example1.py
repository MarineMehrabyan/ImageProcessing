import cv2
import matplotlib.pyplot as plt

image = cv2.imread('img.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Compute the histogram
histogram = cv2.calcHist([gray_image], [0], None, [256], [0, 256])

# Plot the histogram
# It shows the distribution of pixel intensities in the grayscale version of the image. The x-axis of the histogram represents the intensity levels, and the y-axis represents the number of pixels that have that intensity level.
plt.plot(histogram, color='gray')
plt.xlabel('Intensity level')
plt.ylabel('Number of pixels')
plt.title('Histogram of Grayscale Image')

# Display the plot
plt.show()

