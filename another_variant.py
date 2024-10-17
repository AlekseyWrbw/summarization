from transformers import T5ForConditionalGeneration, T5Tokenizer


# Load pre-trained T5 model and tokenizer

model = T5ForConditionalGeneration.from_pretrained("t5-small")

tokenizer = T5Tokenizer.from_pretrained("t5-small")


# Sample Russian text

file = open(r'C:/Users/user/Desktop/github/summarization/chunk_1.txt', encoding='utf-8')
# print(type(file))
text = file.read()

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

def extractive_summarization(text):
    # Токенизация текста
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    # Удаление stopwords
    stop_words = set(stopwords.words('russian'))
    words = [word for word in words if word.lower() not in stop_words]

    # Создание графа
    graph = {}
    for sentence in sentences:
        for word in word_tokenize(sentence):
            if word not in graph:
                graph[word] = []
            for other_word in word_tokenize(sentence):
                if other_word != word and other_word not in graph[word]:
                    graph[word].append(other_word)

    # Ранжирование предложений
    scores = {}
    for sentence in sentences:
        score = 0
        for word in word_tokenize(sentence):
            score += len(graph.get(word, []))
        scores[sentence] = score

    # Выбор наиболее важных предложений
    top_sentences = sorted(scores, key=scores.get, reverse=True)[:3]

    return top_sentences

# Пример использования

print(extractive_summarization(text))