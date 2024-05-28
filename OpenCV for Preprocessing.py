import cv2
import pytesseract

# Read the image
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply thresholding
_, binary_image = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

# Perform OCR
text = pytesseract.image_to_string(binary_image)

print(f"Detected text: {text}")