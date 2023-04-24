import cv2
import matplotlib.pyplot as plt
import numpy as np



#This can give you insights into the color distribution in the image and can be useful for tasks such as color-based image segmentation or color correction.
image = cv2.imread('image.jpg')

# Split the image into its three color channels
b, g, r = cv2.split(image)

# Set the histogram parameters
hist_size = 256
hist_range = (0, 256)

# Compute the histograms for each color channel
# # The first argument is the input array (in this case, the b, g, and r arrays), the second argument specifies which channel to compute the histogram for (0 for grayscale images or single-channel images), the third argument is a mask (which we don't use here), the fourth argument is the number of bins (which we set to hist_size), and the fifth argument is the range of values to consider (which we set to hist_range).
b_hist = cv2.calcHist([b], [0], None, [hist_size], hist_range)
g_hist = cv2.calcHist([g], [0], None, [hist_size], hist_range)
r_hist = cv2.calcHist([r], [0], None, [hist_size], hist_range)

# These lines normalize the histograms so that the area under the curve =1.
cv2.normalize(b_hist, b_hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
cv2.normalize(g_hist, g_hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)
cv2.normalize(r_hist, r_hist, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX)


# Create a plot with three subplots, one for each color channel
fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))

# Plot the histograms for each color channel
ax1.plot(b_hist, color='blue')
ax1.set_title('Blue Channel')
ax2.plot(g_hist, color='green')
ax2.set_title('Green Channel')
ax3.plot(r_hist, color='red')
ax3.set_title('Red Channel')

# Add labels to the x and y axes
for ax in (ax1, ax2, ax3):
    ax.set_xlabel('Intensity level')
    ax.set_ylabel('Normalized Frequency')

# Add a title to the plot
plt.suptitle('Histograms of RGB Channels')

# Display the plot
plt.show()
