import os
import PyPDF2

current_working_folder = os.path.dirname(os.path.abspath(__file__))

# Specify the folder containing PDF files and the output file path
pdf_input=os.path.join(current_working_folder, "PDF_Input.pdf")
pdf_output=os.path.join(current_working_folder, "PDF_Reversed_Page_Order.pdf")
# print(pdf_input)


def reverse_pdf(input_pdf_path, output_pdf_path):
    # Open the input PDF file
    with open(input_pdf_path, 'rb') as input_file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(input_file)
        
        # Get the total number of pages
        num_pages = len(pdf_reader.pages)
        
        # Create a PDF writer object
        pdf_writer = PyPDF2.PdfWriter()
        
        # Reverse the pages and add them to the writer
        for page_num in range(num_pages - 1, -1, -1):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)
        
        # Write the reversed pages to the output PDF file
        with open(output_pdf_path, 'wb') as output_file:
            pdf_writer.write(output_file)


reverse_pdf(pdf_input, pdf_output)

print("Python code Run by Jiatao Lu.")