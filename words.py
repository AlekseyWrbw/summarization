import re
file = open(r'C:\Users\user\Desktop\github\summarization\chunk_1.txt', encoding='utf-8')

text = file.read() # текст в файле изначально считывается как строка (может быть есть другой способ?)

# меняем переносы строк на пробелы
text = re.sub('\n', ' ', text)
text = re.sub(r"(\<(/?[^>]+)>)", '', text)
splitted_text = text.split(sep=' ')
words_list = re.findall(r'(?u)\w{4,}', text)
words_dict = {}

for i in words_list:
    if i in words_dict:
        words_dict[i] +=1
    else: words_dict[i] = 1

for key, value in dict(words_dict).items():
    if value < 2:
        del words_dict[key]

# print(words_dict)
# print(f"type(dict(words_dict).items(){type(dict(words_dict).items())}")

x = lambda x: x[1]
print(x)
sorted1 = sorted(words_dict.items(), key=x)
print(sorted1)
stripped_text = text.strip(' ')
file.close()

###### words frequency
import re
from collections import Counter

# Список предлогов и местоимений (можно расширить по необходимости)
prepositions_and_pronouns = set([
    'я', 'ты', 'он', 'она', 'оно', 'мы', 'вы', 'они', 'этот', 'та', 'то',
    'в', 'на', 'с', 'к', 'по', 'из', 'от', 'для', 'о', 'об', 'за', 'при',
    'как', 'что', 'кто', 'где', 'когда', 'чей', 'который', 'такой', 'так',
    'ли', 'или', 'да', 'нет', 'все', 'всё', 'вся', 'каждый', 'некоторые'
])

def count_words(text):
    # Приводим текст к нижнему регистру и удаляем знаки препинания
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)

    # Фильтруем слова, исключая предлоги и местоимения
    filtered_words = [word for word in words if word not in prepositions_and_pronouns]

    # Подсчитываем количество употреблений каждого слова
    word_count = Counter(filtered_words)

    return word_count

# Пример текста
text = """
Я люблю программировать на Python. Программирование — это здорово! 
Мы можем создать много интересных проектов. Например, игры, веб-приложения и т.д.
"""

# Получаем статистику
word_statistics = count_words(text)

# Выводим результаты
for word, count in word_statistics.items():
    print(f"{word}: {count}")


