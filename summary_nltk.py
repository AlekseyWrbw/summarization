import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

# Download Russian stopwords
nltk.download('stopwords-russian')

# Set Russian stopwords
stopWords = set(stopwords.words('russian'))

# Sample Russian text
file = open(r'C:/Users/user/Desktop/github/summarization/chunk_1.txt', encoding='utf-8')
# print(type(file))
text = file.read()

# Tokenize the text
words = word_tokenize(text.lower(), language='russian')
freqTable = dict()

for word in words:
    if word in stopWords:
        continue
    if word in freqTable:
        freqTable[word] += 1
    else:
        freqTable[word] = 1

sentences = sent_tokenize(text)
sentenceValue = dict()

for sentence in sentences:
    for word, freq in freqTable.items():
        if word in sentence.lower():
            if sentence in sentenceValue:
                sentenceValue[sentence] += freq
            else:
                sentenceValue[sentence] = freq

sumValues = 0
for sentence in sentenceValue:
    sumValues += sentenceValue[sentence]

average = int(sumValues / len(sentenceValue))

summary = ''
for sentence in sentences:
    if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)):
        summary += ' ' + sentence

# print("Оригинальный текст:")
# print(text)
print("\nСводка:")
print(summary)

