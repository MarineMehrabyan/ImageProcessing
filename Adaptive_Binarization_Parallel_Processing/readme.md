_____Adaptive Binarization using Parallel Processing_____

This Python code performs adaptive binarization on multiple images in parallel using the cv2.adaptiveThreshold() function of the OpenCV library. The code uses the concurrent.futures.ProcessPoolExecutor class of the concurrent library for parallel processing.

____Dependencies____
1. OpenCV (cv2)
2. NumPy
3. Math
4. Time
5. OS
6. Multiprocessing (mp)
7. Concurrent.futures
8. Threading
9. Queue
10. Glob

____Usage____
1. Save the code in a Python file with a .py extension
2. Place the images that you want to binarize in the same directory as the Python file
3. Adjust the block_size and constant parameters as needed
4. Run the Python file to binarize all images in parallel

____Functionality____

1. The code first retrieves a list of all the image files in the current directory
2. It then creates a process pool using the ProcessPoolExecutor class with the specified number of processes
3. For each image file, the code loads the input grayscale image, divides it into sections for parallel processing using np.array_split(), and applies adaptive binarization to each section in parallel using executor.map()
4. The thresholded sections are then combined into a single output image using np.concatenate()
5. The original and binarized images are displayed using cv2.imshow() and wait for user input
6. The code loops through all images in the directory and repeats the binarization process for each image.



