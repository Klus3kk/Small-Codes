import PyPDF2
import os

def merge_pdfs(pdf_folder, output_folder, output_filename):
    pdf_merger = PyPDF2.PdfWriter()
    
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        pdf_merger.append(pdf_path)
        
    output_path = os.path.join(output_folder, output_filename)
    
    with open(output_path, 'wb') as output_file:
        pdf_merger.write(output_file)    

    pdf_merger.close()



if __name__ == "__main__":
    pdf_folder = 'PDF'
    output_folder = 'Merged'
    output_filename = input("Name for the merged PDF: ") + ".pdf"
    
    merge_pdfs(pdf_folder, output_folder, output_filename)