from bs4 import BeautifulSoup


def html_to_txt(html_file, txt_file):
    # Читаем HTML файл
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    # Парсим HTML с помощью BeautifulSoup
    soup = BeautifulSoup(html_content, 'lxml')

    # Извлекаем текст
    text = soup.get_text(separator='\n', strip=True)

    # Записываем текст в TXT файл
    with open(txt_file, 'w', encoding='utf-8') as output:
        output.write(text)


# Пример использования
html_to_txt('input.html', 'output.txt')