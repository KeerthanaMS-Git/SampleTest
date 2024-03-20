from docx import Document

def justify_paragraph(paragraph):
    for run in paragraph.runs:
        run.text = run.text.strip()  # Remove leading and trailing spaces
    paragraph.alignment = 3  # 3 for justify alignment

def justify_docx(file_path):
    # Load the document
    doc = Document(file_path)

    # Iterate through paragraphs and justify each one
    for paragraph in doc.paragraphs:
        justify_paragraph(paragraph)

    # Save the modified document
    output_path = r'OutputFiles\EasyOCROutput\Corrected_extracted_text.doc'
    doc.save(output_path)

    print(f"Text justified and saved to '{output_path}'")

# Example usage:
input_file_path = r'OutputFiles\EasyOCROutput\extracted_text.doc'
justify_docx(input_file_path)
