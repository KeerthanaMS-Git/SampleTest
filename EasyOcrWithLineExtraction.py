import easyocr
from PIL import Image

# Load the image
image = Image.open(r'Data\download.jpg')

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Perform OCR on the image
result = reader.readtext(image)

# Print only the detected text
for detection in result:
    print(detection[0])
