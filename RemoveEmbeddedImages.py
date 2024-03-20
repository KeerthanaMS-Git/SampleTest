import cv2
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\TesseractOCR\tesseract.exe'  # Adjust this path accordingly
def remove_embedded_images(image_path):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Use an edge detection method (such as Canny) to identify edges
    edges = cv2.Canny(gray, 50, 150)

    # Use dilation and erosion to close gaps in contours
    dilated = cv2.dilate(edges, None, iterations=2)
    eroded = cv2.erode(dilated, None, iterations=2)

    # Find contours in the eroded image
    contours, _ = cv2.findContours(eroded, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Create a mask to remove detected contours
    mask = img.copy()
    cv2.drawContours(mask, contours, -1, (255, 255, 255), thickness=cv2.FILLED)

    # Replace the detected contours with white color
    result = cv2.bitwise_and(img, mask)

    # Convert the result to PIL Image
    result_pil = Image.fromarray(cv2.cvtColor(result, cv2.COLOR_BGR2RGB))

    return result_pil

def extract_text_from_image(image_path):
    # Remove embedded images
    processed_image = remove_embedded_images(image_path)

    # Use Tesseract to extract text from the processed image
    text = pytesseract.image_to_string(processed_image)

    return text

# Example usage
input_image_path = r'SampleInputs\ImageWithText\high_quality_image.jpg'
extracted_text = extract_text_from_image(input_image_path)

print("Extracted Text:")
print(extracted_text)
