import cv2
import pytesseract
from pytesseract import Output
import os

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'  # Adjust this path accordingly

def extract_multicolumn_data(image_path, output_folder):
    # Read the image using OpenCV
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to create a binary image
    _, binary_img = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)

    # Use Tesseract to get the bounding boxes and text data
    custom_config = r'--oem 3 --psm 6'  # PSM 6 assumes a sparse text with uniform vertical alignment
    result = pytesseract.image_to_data(binary_img, output_type=Output.DICT, config=custom_config)

    # Extract text and coordinates
    extracted_data = []
    for i in range(len(result['text'])):
        text = result['text'][i].strip()
        x, y, w, h = result['left'][i], result['top'][i], result['width'][i], result['height'][i]

        # Filter out empty strings and consider only non-empty text regions
        if text and w > 10 and h > 10:
            extracted_data.append((text, (x, y, w, h)))

    # Save the processed image to the output folder
    output_image_path = os.path.join(output_folder, os.path.basename(image_path))
    cv2.imwrite(output_image_path, binary_img)

    print(f"Processed image saved at: {output_image_path}")

    # Save text to a text file in the output folder
    output_text_path = os.path.join(output_folder, os.path.splitext(os.path.basename(image_path))[0] + '_output_text.txt')
    with open(output_text_path, 'w', encoding='utf-8') as file:
        for text, coordinates in extracted_data:
            file.write(f"Original Text: {text}, Coordinates: {coordinates}\n")

    print(f"Text saved to: {output_text_path}")

def process_images_in_folder(input_folder, output_folder):
    os.makedirs(output_folder, exist_ok=True)

    image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in image_files:
        image_path = os.path.join(input_folder, image_file)
        extract_multicolumn_data(image_path, output_folder)

# Replace 'Data' with the path to your input folder
input_folder = r'SampleInputs\Multicolumn'
output_folder = r'OutputFiles\MulticolumnExtraction'
process_images_in_folder(input_folder, output_folder)
