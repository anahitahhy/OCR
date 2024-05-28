import easyocr
import cv2
import matplotlib.pyplot as plt

# Initialize the EasyOCR reader
reader = easyocr.Reader(['en'])

# Read the image
image_path = 'path_to_your_image.jpg'
image = cv2.imread(image_path)

# Perform OCR
result = reader.readtext(image_path)

# Display the results
for (bbox, text, prob) in result:
    print(f"Detected text: {text} (Confidence: {prob})")
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    image = cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), 2)

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.show()