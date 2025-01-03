from pdf2docx import Converter
import PyPDF2 as pdf

def convert_pdf_to_docx(uploaded_file):
    # Save the uploaded PDF file
    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Convert PDF to DOCX
    docx_path = "converted.docx"
    cv = Converter("uploaded.pdf")
    cv.convert(docx_path, start=0, end=None)
    cv.close()

    return docx_path

def extract_text_from_pdf(uploaded_file):
    reader = pdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += str(page.extract_text())
    return text