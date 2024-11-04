from bs4 import BeautifulSoup

def fb2_to_txt(fb2_file, txt_file):
    # Чтение FB2 файла
    with open(fb2_file, 'r', encoding='utf-8') as file:
        fb2_content = file.read()

    # Парсинг FB2 с помощью BeautifulSoup
    soup = BeautifulSoup(fb2_content, 'lxml')

    # Извлечение текста
    texts = soup.find_all('p')  # Находим все параграфы
    full_text = '\n'.join([text.get_text() for text in texts])

    # Запись текста в TXT файл
    with open(txt_file, 'w', encoding='utf-8') as file:
        file.write(full_text)

# Пример использования
fb2_file = r'C:\Users\user\Downloads\slavoj_zhizhek-sobitie_filosofskoe_puteshes-620777488d118.fb\Zhizhek_Sobytie-Filosofskoe-puteshestvie-po-konceptu.pEAlvg.610317.fb2'  # Укажите путь к вашему FB2 файлу
txt_file = r'C:\Users\user\Downloads\output.txt'      # Укажите имя выходного TXT файла
fb2_to_txt(fb2_file, txt_file)

print(f"Конвертация завершена! Текст сохранен в {txt_file}.")