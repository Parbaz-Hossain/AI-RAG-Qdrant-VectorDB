import io
import pandas as pd
from pypdf import PdfReader
import os


async def load_file(file):
    contents = await file.read()
    filename = file.filename
    file_type = os.path.splitext(filename)[1].lower().lstrip(".")  

    if file_type == "pdf":
        return extract_pdf_text(contents)
    elif file_type in ["xlsx", "xls"]:
        return extract_excel_text(contents)
    elif file_type in ["txt", "csv"]:
        return contents.decode("utf-8")
    else:
        return "Unsupported file format"

def extract_pdf_text(binary_data):
    reader = PdfReader(io.BytesIO(binary_data))
    return "\n".join([page.extract_text() for page in reader.pages if page.extract_text()])

def extract_excel_text(binary_data):
    df = pd.read_excel(io.BytesIO(binary_data))
    return df.to_string(index=False)