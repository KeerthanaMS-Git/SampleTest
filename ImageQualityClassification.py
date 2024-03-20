import cv2
import numpy as np
import pytesseract
import easyocr

# Set Tesseract OCR executable path
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'

def preprocess_image(image_path, sharpness, brightness, contrast, sharpness_threshold, brightness_threshold, contrast_threshold):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return None

    # Convert image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply preprocessing techniques based on image qualities
    if sharpness < sharpness_threshold:
        # Apply sharpening
        sharpening_kernel = np.array([[-1, -1, -1],
                                      [-1, 9, -1],
                                      [-1, -1, -1]])
        image = cv2.filter2D(image, -1, sharpening_kernel)
    
    if contrast < contrast_threshold:
        # Apply contrast enhancement
        clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
        image = clahe.apply(gray)

    if brightness < brightness_threshold:
        # Apply brightness adjustment
        alpha = 1.5  # adjust this value based on your requirement
        beta = 50  # adjust this value based on your requirement
        image = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

    return image

def assess_image_quality(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if the image is loaded successfully
    if image is None:
        print("Error: Unable to load image.")
        return

    # Calculate image properties
    height, width, channels = image.shape
    size = image.size
    dtype = image.dtype

    # Calculate image sharpness (variance of Laplacian)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sharpness = cv2.Laplacian(gray, cv2.CV_64F).var()

    # Assess brightness and contrast
    brightness = gray.mean()
    contrast = gray.std()

    # Print image properties
    print("Image Properties:")
    print("- Dimensions: {}x{} pixels".format(width, height))
    print("- Channels:", channels)
    print("- Size:", size)
    print("- Data type:", dtype)
    print("- Sharpness:", sharpness)
    print("- Brightness:", brightness)
    print("- Contrast:", contrast)

    # Set threshold values for preprocessing
    sharpness_threshold = 70  # Adjust threshold value based on your requirement
    contrast_threshold = 50    # Adjust threshold value based on your requirement
    brightness_threshold = 125 # Adjust threshold value based on your requirement

    # Preprocess image based on quality metrics
    preprocessed_image = preprocess_image(image_path, sharpness, brightness, contrast, sharpness_threshold, brightness_threshold, contrast_threshold)

    # Save original and preprocessed images
    cv2.imwrite("original_image.jpg", image)
    cv2.imwrite("preprocessed_image.jpg", preprocessed_image)

    # Extract text from the preprocessed image using pytesseract
    extracted_text_tesseract = extract_text_with_tesseract(preprocessed_image)
    print("Extracted Text with pytesseract:")
    print(extracted_text_tesseract)

    # Extract text from the preprocessed image using EasyOCR
    extracted_text_easyocr = extract_text_with_easyocr(preprocessed_image)
    print("Extracted Text with EasyOCR:")
    print(extracted_text_easyocr)

def extract_text_with_tesseract(image):
    # Use pytesseract to extract text from the image
    extracted_text = pytesseract.image_to_string(image)
    return extracted_text

def extract_text_with_easyocr(image):
    # Initialize EasyOCR reader
    reader = easyocr.Reader(['en'])

    # Use EasyOCR to extract text from the image
    result = reader.readtext(image)

    # Extract and concatenate text from the result
    extracted_text = ' '.join([text[1] for text in result])

    return extracted_text

# Path to your image
image_path = r'outputscreenshots\download.jpg'

# Assess image quality and preprocess
assess_image_quality(image_path)
