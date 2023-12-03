import cv2
import pytesseract

# Load the image
image = cv2.imread('IELTS-template.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply adaptive thresholding to handle varying lighting conditions
thresholded = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Use morphological operations to clean up the image
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
cleaned_image = cv2.morphologyEx(thresholded, cv2.MORPH_CLOSE, kernel)

# Find contours in the cleaned image
contours, _ = cv2.findContours(cleaned_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Iterate through contours and filter based on area
min_area = 100
filtered_contours = [contour for contour in contours if cv2.contourArea(contour) > min_area]
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\Kiran Tungal\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Draw bounding boxes around the filtered contours
for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

# Use Tesseract OCR to extract text from the regions
for contour in filtered_contours:
    x, y, w, h = cv2.boundingRect(contour)
    text_roi = cleaned_image[y:y + h, x:x + w]
    text = pytesseract.image_to_string(text_roi, config='--psm 6')
    print("Detected Text:", text)

# Display the result
cv2.imshow('Result', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
