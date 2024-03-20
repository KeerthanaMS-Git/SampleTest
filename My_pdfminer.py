from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO

class PdfConverter:

    def __init__(self, file_path):
        self.file_path = file_path

    def convert_pdf_to_txt(self):
        print("The function is entered.")
        rsrcmgr = PDFResourceManager()
        retstr = StringIO()
        codec = 'utf-8'  # 'utf16','utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
        with open(self.file_path, 'rb') as fp:
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            print("The function is in part 2 entered.")
            password = ""
            maxpages = 0
            caching = True
            pagenos = set()
            print("The function is in part 3 entered.")
            for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password, caching=caching, check_extractable=True):
                print("The function is in part 4 entered.")
                interpreter.process_page(page)
                print("The function is in part 5 entered.")
        device.close()
        text = retstr.getvalue()
        retstr.close()
        return text

    def save_convert_pdf_to_txt(self):
        content = self.convert_pdf_to_txt()
        print(content)
        with open(r'EasyOCR\text_pdf.txt', 'w', encoding='utf-8') as txt_pdf:
            txt_pdf.write(content)

if __name__ == '__main__':
    pdfConverter = PdfConverter(file_path=r'SampleInputs\PDF\Demo - 1-1.pdf')
    print(pdfConverter.convert_pdf_to_txt())
    print("The function is in part 6 entered.")