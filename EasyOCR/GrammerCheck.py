from docx import Document
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT

def correct_alignment(docx_file, output_file):
    document = Document(docx_file)
    alignment_to_correct = WD_PARAGRAPH_ALIGNMENT.LEFT  # Specify the alignment you want to correct

    # Iterate through paragraphs and runs
    for paragraph in document.paragraphs:
        # Correct alignment of paragraphs
        if paragraph.alignment != alignment_to_correct:
            paragraph.alignment = alignment_to_correct

        for run in paragraph.runs:
            # Check if the run has alignment property
            if hasattr(run, 'alignment'):
                # Correct alignment of runs (if applicable)
                if run.alignment != alignment_to_correct:
                    run.alignment = alignment_to_correct

    # Save the modified document
    document.save(output_file)
    print(f"Alignment corrected and saved to {output_file}")

# Example usage
input_docx_file = r'OutputFiles\EasyOCROutput\extracted_text.doc'
output_docx_file = r'OutputFiles\EasyOCROutput\corrected_document.docx'

correct_alignment(input_docx_file, output_docx_file)
