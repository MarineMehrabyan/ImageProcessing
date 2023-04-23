_____Barcode and QR code detection and decoding using Python and OpenCV_____

This code is a Python script that detects and decodes barcodes and QR codes in images using the OpenCV library.

___Requirements___
1. Python 3
2. OpenCV library
3. pyzbar library
4. Numpy library


____Usage____
1. Make sure that you have all the required libraries installed.
2. Place the images containing the barcodes and QR codes in the same directory as the Python script.
3. Edit the extensions list to include the file extensions of the images you want to process.
4. Run the Python script.
5. The decoded data for each barcode and QR code will be printed to the console and displayed on the image as text.
6. Press any key to close the image window.


____Code Explanation____

The code consists of the following steps:

1. Import the required libraries.
2. Define the file extensions to be searched for.
3. Loop over each file with the specified extensions.
4. Read the image file.
5. Convert the image to grayscale.
6. Apply a threshold to the image to enhance the contrast between the barcode/QR code and the background.
7. Loop over each detected barcode/QR code in the image.
8. Decode the data from the barcode/QR code.
9. Add a bounding box around the barcode/QR code.
10. Add text to the image showing the decoded data.
11. Display the result image with the detected barcode/QR code and the decoded data.
12. Close all windows.



____Limitations____

1. The code is not able to detect and decode damaged or partially obscured barcodes and QR codes.
2. The code may not work well with images that have low contrast or uneven lighting.





