import fitz  # PyMuPDF
import pandas as pd

def add_text_to_pdf(pdf_path, text_data):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    # Iterate through pages and add text
    page = pdf_document[0]

        # Extract text data from the dictionary
    name = str(text_data.get('Name', ''))
    top = str(text_data.get('Top', ''))  # Default value 100 if 'Top' is not provided
    bottom = str(text_data.get('Bottom', ''))
    num = str(text_data.get('Number', ''))
    font_name = 'helv'  # Replace with your desired font
    font_size = 12  # Replace with your desired font size
    color = (1, 0, 0)  # RGB color, default is red

        # Add text line to the page
    p1 = fitz.Point(36, 277)
    p2 = fitz.Point(36, 295)
    p3 = fitz.Point(36, 320)
    p4 = fitz.Point(460, 331)
    page.insert_text(p1, name, fontname=font_name, fontsize=font_size, color=color)
    page.insert_text(p2, top, fontname=font_name, fontsize=font_size, color=color)
    page.insert_text(p3, bottom, fontname=font_name, fontsize=font_size, color=color)
    page.insert_text(p4, num, fontname=font_name, fontsize=font_size, color=color)

    # Save the modified PDF
    output_path_page = name + ' BOP QUOTE.pdf'
    pdf_document.save(output_path_page)
    print(f"Text added to {pdf_path} and saved to {output_path_page}")
    pdf_document.close()

def process_pdfs(csv_path, pdf_path):
    # Read CSV file
    csv_data = pd.read_csv(csv_path)

    # Open the PDF file
    pdf_document = fitz.open(pdf_path)

    for index, row in csv_data.iterrows():
        # Extract text data from the CSV row
        text_data = {
            'Name': row['Name'].strip(),
            'Top': row['Top'],
            'Bottom': row['Bottom'],
            'Number': row['Number']
        }

        # Add text to PDF
        add_text_to_pdf(pdf_path, text_data)

if __name__ == "__main__":
    csv_path = r'C:\Users\MSI\Documents\GitHub\Nail-Salon-SQL-Marketing\final2.csv'  # Provide your CSV file path
    pdf_path = r'C:\Users\MSI\Documents\GitHub\Nail-Salon-SQL-Marketing\BOPQUOTE.pdf'  # Provide your PDF file path

    process_pdfs(csv_path, pdf_path)
