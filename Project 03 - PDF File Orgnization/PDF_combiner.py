import os
from PyPDF2 import PdfReader, PdfWriter


current_working_folder = os.path.dirname(os.path.abspath(__file__))

# Specify the folder containing PDF files and the output file path
pdf_folder=os.path.join(current_working_folder, "PDF to Combine")
pdf_combined_file=os.path.join(current_working_folder, "PDF Combined.pdf")


def merge_pdfs(folder_path, output_path):
    # Create a PdfWriter object
    pdf_writer = PdfWriter()

    # Iterate through all the files in the folder
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            # Open each PDF file in read-binary mode
            with open(file_path, 'rb') as file:
                # Create a PdfReader object
                pdf_reader = PdfReader(file)
                # Add each page to the writer object
                for page in pdf_reader.pages:
                    pdf_writer.add_page(page)

    # Write out the merged PDF to a new file
    with open(output_path, 'wb') as output_file:
        pdf_writer.write(output_file)

    print(f'Merged PDF saved as {output_path}')


merge_pdfs(pdf_folder, pdf_combined_file)

print("Python code Run by Jiatao Lu.")