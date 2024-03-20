# This code is to extract the text from image files. 
# Open Source Computer Vision used for reading image files. 
# Pytesseract - for Optical Character recognition.

import cv2
import os
import numpy as np
import pytesseract
from pytesseract import Output
import string

input_folder = r'SampleInputs\Multicolumn'
output_folder = r'OutputFiles\MulticolumnExtraction'
os.makedirs(output_folder, exist_ok=True)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'

def convert_NoiseRemovedImg_To_Text(image_Path):
    img = cv2.imread(image_Path)

    noise_Removed_img = cv2.medianBlur(img, 5)

    # Use Tesseract to do OCR on the grayscale image
    text = pytesseract.image_to_string(noise_Removed_img)

    # Print the extracted text
    print("Extracted Text:")
    print(text)

    # Save the processed image to the output folder
    output_image_path = os.path.join(output_folder, os.path.basename(image_Path))
    cv2.imwrite(output_image_path, noise_Removed_img)

    print(f"Processed image saved at: {output_image_path}")
    output_file_path = os.path.splitext(output_image_path)[0] + '.txt'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Text saved to: {output_file_path}")

def process_images_in_folder(folder_path):
    image_files = [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

    for image_file in image_files:
        image_path = os.path.join(folder_path, image_file)
        convert_NoiseRemovedImg_To_Text(image_path)

# Calling the function to process each image in the folder.
process_images_in_folder(r'SampleInputs\PDF')



