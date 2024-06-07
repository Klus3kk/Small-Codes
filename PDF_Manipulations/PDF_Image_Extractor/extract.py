from PyPDF2 import PdfReader
import os

def extract_images(pdf_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    
    for pdf_file in pdf_files:
        pdf_path = os.path.join(pdf_folder, pdf_file)
        reader = PdfReader(pdf_path)
        
        for page_num, page in enumerate(reader.pages):
            count = 0
            for image_file_object in page.images:
                with open(os.path.join(output_folder, f"{pdf_file}_page{page_num+1}_image{count}.jpg"), "wb") as fp:
                    fp.write(image_file_object.data)
                count += 1

if __name__ == "__main__":
    pdf_folder = 'PDF'
    output_folder = 'Extracted'
    
    extract_images(pdf_folder, output_folder)
