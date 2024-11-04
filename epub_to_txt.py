import os
from ebooklib import epub
from bs4 import BeautifulSoup

def epub_to_txt(epub_file, txt_file):
    # Загружаем EPUB файл
    book = epub.read_epub(epub_file)

    # Открываем текстовый файл для записи
    with open(txt_file, 'w', encoding='utf-8') as output_file:
        # Проходим по всем элементам книги
        for item in book.get_items():
            # Проверяем, является ли элемент HTML
            if item.get_type() == epub.EpubHtml:
                # Извлекаем текст из HTML
                soup = BeautifulSoup(item.get_body_content_str(), 'html.parser')
                text = soup.get_text()
                output_file.write(text + '\n')

    print(f"Файл '{epub_file}' успешно преобразован в '{txt_file}'.")

if __name__ == "__main__":
    # Укажите путь к вашему EPUB файлу
    epub_file_path = "example.epub"  # Замените на ваш EPUB файл
    txt_file_path = "output.txt"      # Имя выходного текстового файла

    epub_to_txt(epub_file_path, txt_file_path)