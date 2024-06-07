import PyPDF2
import os

def extract_text(pdf_folder, output_folder, output_filename):
    output_path = os.path.join(output_folder, output_filename)
    
    with open(output_path, 'w', encoding='utf-8') as output_file:
        pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
        
        for pdf_file in pdf_files:
            pdf_path = os.path.join(pdf_folder, pdf_file)
            reader = PyPDF2.PdfReader(pdf_path)

            for page_num in range(len(reader.pages)):
                page = reader.pages[page_num]
                text = page.extract_text()
                if text:
                    output_file.write(text)
                    output_file.write("\n\n")




if __name__ == "__main__":
    pdf_folder = 'PDF'
    output_folder = 'Extracted'
    output_filename = input("Name for the extracted text from PDF: ") + ".txt"
    
    extract_text(pdf_folder, output_folder, output_filename)