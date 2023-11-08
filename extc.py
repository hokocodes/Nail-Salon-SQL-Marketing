import fitz  # PyMuPDF

def extract_text_coordinates(pdf_path):
    doc = fitz.open(pdf_path)

    for page_num in range(doc.page_count):
        page = doc[page_num]
        blocks = page.get_text("blocks")

        for b in blocks:
            block_rect = fitz.Rect(b[:4])
            block_text = b[4]

            print(f"Page {page_num + 1}, Block: {block_text}, Coordinates: {block_rect}")

    doc.close()

# Example usage
pdf_path = r"C:\Users\MSI\Desktop\TINA OFFICE\QUOTE PROPOSALS\NAIL SALONS\2023\OCTOBER\AKYISH Japanese Retreat & Spa BOP QUOTE.pdf"
extract_text_coordinates(pdf_path)