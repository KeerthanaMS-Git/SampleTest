import fitz  # PyMuPDF
import tabula
import pandas as pd
import os

output_folder = 'OutputFiles'

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text("text")
    doc.close()
    return text

def extract_tables_from_pdf(pdf_path):
    # Read the PDF file and extract tables
    tables = tabula.read_pdf(pdf_path, pages='all', multiple_tables=True)
    return tables

def is_table(text):
    # Check if the text contains typical tabular patterns
    return any(char.isdigit() for char in text) and any('\n' in line for line in text.split('\n'))

def separate_paragraphs_and_tables(pdf_text):
    # Split the text into paragraphs and tables based on empty lines
    content_blocks = [block.strip() for block in pdf_text.split('\n\n')]

    # Separate paragraphs and tables
    paragraphs = [block for block in content_blocks if not is_table(block)]
    tables = [block for block in content_blocks if is_table(block)]

    return paragraphs, tables

def write_to_text_file(content, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def combine_text_files(files, output_combined_path):
    with open(output_combined_path, 'w', encoding='utf-8') as combined_file:
        for file_path in files:
            with open(file_path, 'r', encoding='utf-8') as current_file:
                combined_file.write(current_file.read() + '\n\n')

def main():
    # Specify the path to your PDF file
    pdf_path = r'SampleInputs\TabularData\TableData_withPara.pdf'

    # Extract paragraphs and tables
    pdf_text = extract_text_from_pdf(pdf_path)
    paragraphs, tables = separate_paragraphs_and_tables(pdf_text)

    # Write paragraphs to a text file
    paragraphs_output_path = os.path.join(output_folder, 'extracted_paragraphs.txt')
    write_to_text_file('\n\n'.join(paragraphs), paragraphs_output_path)
    print(f"Extracted Paragraphs written to: {paragraphs_output_path}")

    # Extract tables
    pdf_tables = extract_tables_from_pdf(pdf_path)

    # Iterate through the extracted tables
    for i, table in enumerate(pdf_tables):
        # Replace NaN with an empty string in each DataFrame
        df_cleaned = table.fillna('')
        
        # Write each table to a text file
        table_output_path = os.path.join(output_folder, f'extracted_table_{i}.txt')
        df_cleaned.to_csv(table_output_path, sep='\t', index=False)
        print(f"Table {i} written to: {table_output_path}")

    # Combine all text files into a single file
    all_files = [paragraphs_output_path] + [os.path.join(output_folder, f'extracted_table_{i}.txt') for i in range(len(pdf_tables))]
    combined_output_path = os.path.join(output_folder, 'combined_output.txt')
    combine_text_files(all_files, combined_output_path)
    print(f"All text files combined into: {combined_output_path}")

if __name__ == "__main__":
    main()
