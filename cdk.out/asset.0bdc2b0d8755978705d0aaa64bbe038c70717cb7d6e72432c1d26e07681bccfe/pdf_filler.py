

# lambda_src/pdf_data_generator/pdf_filler.py
import io
from PyPDF2 import PdfReader, PdfWriter

def fill_pdf(template_path: str, field_data: dict) -> bytes:
    """
    Fills form fields in the given PDF template and returns the result as a byte stream.
    """
    with open(template_path, "rb") as f:
        reader = PdfReader(f)
        writer = PdfWriter()

        # Only first page might have form fields, or multiple pages do. 
        # We'll iterate all pages to ensure we fill any that have fields:
        for page_idx in range(len(reader.pages)):
            page = reader.pages[page_idx]
            writer.add_page(page)

        # Update form fields
        writer.update_page_form_field_values(writer.pages, field_data)

        # Write to in-memory buffer
        buffer = io.BytesIO()
        writer.write(buffer)
        buffer.seek(0)

        return buffer.read()
