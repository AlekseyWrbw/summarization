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
# print(sorted1)
stripped_text = text.strip(' ')
file.close()


'''
try gensin
'''
from gensim.summarization.summarizer import summarize
from gensim.summarization import keywords
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')

# Set Russian stopwords
stopWords = set(stopwords.words('russian'))

# Sample Russian text
text = "Ваш текст здесь"

# Preprocess the text (tokenize and remove stopwords)
words = word_tokenize(text.lower())
words = [word for word in words if word not in stopWords]

# Join the words back into a string
text = ' '.join(words)

# Summarize the text
summary = summarize(text, ratio=0.3)

# Get keywords
key_words = keywords(text).split('\n')

print("Оригинальный текст:")
print(text)
print("\nСводка:")
print(summary)
print("\nКлючевые слова:")
for word in key_words:
    print(word)