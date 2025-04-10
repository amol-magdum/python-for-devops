from PyPDF2 import PdfReader

# Path to the encrypted PDF file
encrypted_pdf_path = "encrypted_file.pdf"

# Password for the encrypted PDF
password = "your_password"

# Open and decrypt the PDF
reader = PdfReader(encrypted_pdf_path)
if reader.is_encrypted:
    success = reader.decrypt(password)
    if success:
        print("PDF decrypted successfully!")
        # Access the content of the PDF
        for page in reader.pages:
            print(page.extract_text())
    else:
        print("Failed to decrypt the PDF. Check the password.")
else:
    print("The PDF is not encrypted.")