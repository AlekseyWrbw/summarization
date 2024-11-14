import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer

def load_model():
    # Загружаем предобученную модель и токенизатор
    model_name = 'gpt2'  # Можно использовать 'gpt2-medium', 'gpt2-large' и т.д.
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    model = GPT2LMHeadModel.from_pretrained(model_name)
    model.eval()  # Устанавливаем модель в режим оценки
    return model, tokenizer

def generate_text(model, tokenizer, prompt, max_length=100):
    # Токенизируем вводимый текст
    inputs = tokenizer.encode(prompt, return_tensors='pt')

    # Генерируем текст
    with torch.no_grad():
        outputs = model.generate(inputs, max_length=max_length, num_return_sequences=1, no_repeat_ngram_size=2)

    # Декодируем сгенерированный текст
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text

def main():
    model, tokenizer = load_model()
    print("Текстовый генератор на основе GPT-2.")
    print("Введите текст для продолжения (или 'exit' для выхода):")

    while True:
        prompt = input("Ввод: ")
        if prompt.lower() == 'exit':
            break
        generated = generate_text(model, tokenizer, prompt)
        print("Сгенерированный текст:")
        print(generated)

if __name__ == "__main__":
    main()