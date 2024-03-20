from PIL import Image
import pytesseract
import os
from PyPDF2 import PdfReader  # Import the required module

# Set the path to the Tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'  # Adjust this path accordingly
output_folder = r'OutputFiles\ImageWithTextExtraction'

# Ensure the output folder exists
os.makedirs(output_folder, exist_ok=True)

def extract_text_from_file(file_path):
    # Check the file extension and process accordingly
    _, file_extension = os.path.splitext(file_path.lower())

    if file_extension == '.pdf':
        text = extract_text_from_pdf(file_path)
    elif file_extension in ['.png', '.tiff', '.tif', '.jpg', '.jpeg']:
        text = extract_text_from_image(file_path)
    else:
        print(f"Unsupported file format: {file_extension}")
        return ""

    return text

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()

    except ImportError:
        print("PyPDF2 library is not installed. Please install it using 'pip install PyPDF2'.")

    return text

def extract_text_from_image(image_path):
    # Open the image using Pillow
    img = Image.open(image_path)

    # Use Tesseract to extract text
    text = pytesseract.image_to_string(img)
    print("Extracted Text:")
    print(text)

    output_image_path = os.path.join(output_folder, os.path.basename(image_path))
    output_file_path = os.path.splitext(output_image_path)[0] + '.txt'
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(text)

    print(f"Text saved to: {output_file_path}")

    return text

def process_single_file(file_path):
    if os.path.isfile(file_path):
        extract_text_from_file(file_path)
    else:
        print(f"File not found: {file_path}")

# Calling the function to process a specific file.
process_single_file(r'SampleInputs\ImageWithText\high_quality_image.jpg')  # Adjust the file path accordingly
