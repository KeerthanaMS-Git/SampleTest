import os
import easyocr
from pdf2image import convert_from_path
from PIL import Image
import numpy as np
import cv2

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

def count_words_in_line(line):
    # Split the line into words
    words = line.split()
    return len(words)

def extract_text_from_pdf(pdf_path):
    # Convert PDF to images
    images = convert_from_path(pdf_path)

    # Initialize variable to store extracted text
    extracted_text = ""

    # Process each page image
    for img in images:
        # Convert PIL Image to OpenCV format
        img_np = np.array(img)
        if img_np.ndim != 3:
            continue  # Skip grayscale or empty images
        img_cv = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

        # Perform OCR on image
        text = reader.readtext(img_cv)

        # Extract text from OCR results
        for detection in text:
            extracted_text += detection[1] + '\n'

    return extracted_text

def count_words_in_pdf(pdf_path):
    # Extract text from PDF
    extracted_text = extract_text_from_pdf(pdf_path)

    # Split text into lines
    lines = extracted_text.split('\n')

    # Process each line to count words
    for line in lines:
        word_count = count_words_in_line(line)
        print(f"Words in line: {word_count}, Line content: {line}")


# Path to your PDF file
pdf_path = r'SampleInputs\PDF\Demo - 1-1.pdf'

# Count words in the PDF and print them
count_words_in_pdf(pdf_path)