from transformers import pipeline


# Создание pipeline для суммаризации

summarizer = pipeline("summarization", model="IlyaGusev/ru_bert_summ")


# Русскоязычный текст для суммаризации

file = open(r'C:\Users\user\Desktop\github\summarization\chunk_1.txt', encoding='utf-8')

text = file.read() # текст в файле изначально считывается как строка (может быть есть другой способ?)

# Суммаризация текста

summary = summarizer(text, max_length=100, clean_up_tokenization_spaces=True)


print(summary)