from PIL import Image
import pytesseract
import cv2

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Read the image
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Perform OCR
text = pytesseract.image_to_string(gray)

print(f"Detected text: {text}")