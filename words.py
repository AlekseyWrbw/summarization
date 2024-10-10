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
sorted1 = sorted(words_dict.items(), key=x)
print(sorted1)
stripped_text = text.strip(' ')
file.close()