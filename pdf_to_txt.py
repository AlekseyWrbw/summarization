import pdfplumber

def pdf_to_txt(pdf_file, txt_file):
    with pdfplumber.open(pdf_file) as pdf:
        with open(txt_file, 'w', encoding='utf-8') as output:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    output.write(text)
                    output.write("\n")  # Добавляем новую строку между страницами

# Пример использования
pdf_to_txt('input.pdf', 'output.txt')