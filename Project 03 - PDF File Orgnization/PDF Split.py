import os
#import PyPDF2
from PyPDF2 import PdfReader, PdfWriter


current_working_folder = os.path.dirname(os.path.abspath(__file__))

# Specify the folder containing PDF files and the output file path
pdf_input_folder=os.path.join(current_working_folder, "Input")
pdf_output_folder=os.path.join(current_working_folder, "Output")


for filename in os.listdir(pdf_input_folder):
    # print(filename)
    file_base_name, file_extension_name=os.path.splitext(filename)
    # print(file_base_name)
    # print(file_extension_name)
    input_file_name=os.path.join(current_working_folder, "Input", filename)

    with open(input_file_name, 'rb') as file:
        # Create a PdfReader object
        pdf_reader = PdfReader(file)
        number_of_page=len(pdf_reader.pages)
        # Add each page to the writer object
        for page_number in range(0,number_of_page,2):
            pdf_writer = PdfWriter()
            pdf_writer.add_page(pdf_reader.pages[page_number])
            pdf_writer.add_page(pdf_reader.pages[page_number+1])
            # Write out the merged PDF to a new file
            # with open(output_path, 'wb') as output_file:
            output_file_name=os.path.join(current_working_folder, "Output", file_base_name+" - " + f"{(page_number//2+1):03}"+file_extension_name)
            pdf_writer.write(output_file_name)


print("PDF split is done. Run by Jiatao Lu.")