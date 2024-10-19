from transformers import BartTokenizer, BartForConditionalGeneration

# Load pre-trained BART model and tokenizer
model_name = "IlyaGusev/bart-large-finetuned-ru-summarization"
tokenizer = BartTokenizer.from_pretrained(model_name)
model = BartForConditionalGeneration.from_pretrained(model_name)

# Input text to be summarized
file = open(r'C:/Users/user/Desktop/github/summarization/chunk_1.txt', encoding='utf-8')
# print(type(file))
text = file.read()

# Tokenize and summarize the input text using BART
inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", max_length=1024, truncation=True)
summary_ids = model.generate(inputs, max_length=100, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)

# Decode and output the summary
summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
# print("Original Text:")
# print(text)
print("\nSummary:")
print(summary)