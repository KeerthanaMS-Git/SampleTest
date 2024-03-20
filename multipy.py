import fitz  # PyMuPDF
import pytesseract
from PIL import Image
import io

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'

def is_scanned_image(pdf_path):
    doc = fitz.open(pdf_path)
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        image_list = page.get_images(full=True)
        
        if image_list:
            return True  # If there are images, consider it as a scanned image
        
        text = page.get_text()
        if text.strip():  # If there is non-empty text, it's not just a scanned image
            return False
    
    return True  # If no text and no images, assume it's a scanned image

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()
    
    return text

def extract_text_from_scanned_pdf(pdf_path):
    images_text = ""
    doc = fitz.open(pdf_path)
    
    for page_num in range(doc.page_count):
        page = doc[page_num]
        images = page.get_images(full=True)
        
        for img_index, img in enumerate(images):
            xref = img[0]
            base_image = doc.extract_image(xref)
            image_bytes = base_image["image"]

            # Convert the image to PIL format and use Tesseract for OCR
            image = Image.open(io.BytesIO(image_bytes))
            text = pytesseract.image_to_string(image)
            images_text += text

    return images_text

# Example usage:
pdf_path = r'SampleInputs\PDF\samplePDF.pdf'

if is_scanned_image(pdf_path):
    scraped_data = extract_text_from_scanned_pdf(pdf_path)
    print("Scanned Image PDF - Extracted Text:")
    print(scraped_data)
else:
    scraped_data = extract_text_from_pdf(pdf_path)
    print("Normal PDF - Extracted Text:")
    print(scraped_data)
