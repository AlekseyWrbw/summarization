from gensim.summarization import summarize
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