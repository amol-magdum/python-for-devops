from PyPDF2 import PdfReader, PdfWriter

# Reading a PDF file
def read_pdf(file_path):
    reader = PdfReader(file_path)
    for page in reader.pages:
        print(page.extract_text())
    
# Writing to a new PDF file
def write_pdf(input_file, output_file, page_numbers):
    reader = PdfReader(input_file)
    writer = PdfWriter()

    for page_num in page_numbers:
        writer.add_page(reader.pages[page_num])

    with open(output_file, "wb") as output_pdf:
        writer.write(output_pdf)

if __name__ == "__main__":
    input_pdf = "example1.pdf"
    output_pdf = "output.pdf"

    # Read the content of the PDF
    print("Reading PDF content:")
    read_pdf(input_pdf)

    # Write specific pages to a new PDF
    print(f"\nWriting selected pages to {output_pdf}")
    write_pdf(input_pdf, output_pdf, [0, 1])  # Example: Copying the first two pages
