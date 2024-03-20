import time
import easyocr
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
import numpy as np

# Set the path to the Tesseract executable (adjust this path accordingly)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'

def extract_text_from_image(image_path):
    # Use EasyOCR for text extraction
    reader = easyocr.Reader(['en'])
    result_easyocr = reader.readtext(image_path)
    text_easyocr = ' '.join([entry[1] for entry in result_easyocr])

    # Use Tesseract for text extraction
    text_tesseract = pytesseract.image_to_string(Image.open(image_path))

    return text_easyocr, text_tesseract

def extract_text_from_pdf(pdf_path):
    # Convert PDF pages to images
    images = convert_from_path(pdf_path, 500)  # Adjust the DPI (dots per inch) if needed
    text_easyocr = ""
    text_tesseract = ""

    # Use EasyOCR and Tesseract for each image
    for img in images:
        # Convert PIL image to numpy array
        img_np = np.array(img)

        # Use EasyOCR for text extraction
        reader = easyocr.Reader(['en'])
        result_easyocr = reader.readtext(img_np)
        text_easyocr += ' '.join([entry[1] for entry in result_easyocr])

        # Use Tesseract for text extraction
        text_tesseract += pytesseract.image_to_string(img)

    return text_easyocr, text_tesseract

def write_text_to_file(text, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

def measure_execution_time(func, *args):
    start_time = time.time()
    result = func(*args)
    end_time = time.time()
    execution_time = end_time - start_time
    return result, execution_time

def extract_text_from_file(file_path):
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        return extract_text_from_image(file_path)
    elif file_path.lower().endswith('.pdf'):
        return extract_text_from_pdf(file_path)
    else:
        print("Unsupported file format.")
        return "", ""

# Example usage:
file_path = r'SampleInputs\PDF\Demo - 1-1.pdf'  # Change this to your file path
output_file_path_easyocr = r'OutputFiles\EasyOCROutput\output_easyocr.txt'  # Specify the output file path for EasyOCR
output_file_path_tesseract = r'OutputFiles\EasyOCROutput\output_tesseract.txt'  # Specify the output file path for Tesseract

# Extract text from the file using EasyOCR and Tesseract
extracted_text, execution_time = measure_execution_time(extract_text_from_file, file_path)
print(f"Extraction time: {execution_time:.4f} seconds")

# Write the extracted text to files
write_text_to_file(extracted_text[0], output_file_path_easyocr)  # EasyOCR text
write_text_to_file(extracted_text[1], output_file_path_tesseract)  # Tesseract text

# Compare the extracted text
print("Comparison:")
print("EasyOCR:")
print(extracted_text[0])
print("Tesseract:")
print(extracted_text[1])
