# TextObjectFace-Recognization-using-OpenCV

This Python program utilizes the OpenCV and pytesseract libraries to perform Optical Character Recognition (OCR) on an image. The image is loaded, converted to grayscale, and adaptive thresholding is applied to handle varying lighting conditions. Morphological operations are then employed to clean up the image. Contours are detected in the cleaned image, and filtering based on contour area is applied to retain only significant regions. Bounding boxes are drawn around these filtered contours, highlighting the regions of interest. Tesseract OCR is used to extract text from each of these regions, and the detected text is printed to the console. Finally, the original image with bounding boxes is displayed. This program is designed for text extraction from images, particularly useful in scenarios like document analysis or text recognition in images

1. pip install opencv-python
2. pip install pytesseract
3. Download and install Tesseract OCR from the official website: Tesseract OCR. Make sure to add the Tesseract installation directory to your system's PATH environment variable. After installing the required libraries and Tesseract OCR, you can execute the provided program.
