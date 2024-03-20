import os
import cv2
import pytesseract

# Set the path to the Tesseract executable (modify as needed)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'
output_folder = r'OutputFiles\HandwrittenExtraction'
os.makedirs(output_folder, exist_ok=True)

def extract_handwritten_text(image_path):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    noise_Removed_img = cv2.medianBlur(img, 5)

    # Use Tesseract to do OCR on the grayscale image
    text = pytesseract.image_to_string(noise_Removed_img)

    # Print the extracted text
    print(f"Extracted Handwritten Text from {image_path}:")
    print(text)
    output_image_path = os.path.join(output_folder, os.path.basename(image_path))
    output_file_path = os.path.splitext(output_image_path)[0] + '.txt'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Text saved to: {output_file_path}")
# Replace 'folder_path' with the actual path to your folder containing handwritten images
folder_path = r'SampleInputs\HandWritten'

# List all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        # Build the full path to the image file
        image_path = os.path.join(folder_path, filename)

        # Process each image in the folder
        extract_handwritten_text(image_path)
