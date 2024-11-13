import numpy as np

# Функция активации: сигмоида
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Производная сигмоиды
def sigmoid_derivative(x):
    return x * (1 - x)

# Класс нейросети
class NeuralNetwork:
    def __init__(self, x, y):
        self.input = x  # Входные данные
        self.weights1 = np.random.rand(self.input.shape[1], 4)  # Случайные веса для первого слоя
        self.weights2 = np.random.rand(4, 1)  # Случайные веса для второго слоя
        self.y = y  # Ожидаемые выходные данные
        self.output = np.zeros(self.y.shape)  # Инициализация выходных данных

    def feedforward(self):
        # Прямое распространение
        self.layer1 = sigmoid(np.dot(self.input, self.weights1))  # Первый скрытый слой
        self.output = sigmoid(np.dot(self.layer1, self.weights2))  # Выходной слой

    def backprop(self):
        # Обратное распространение
        d_weights2 = np.dot(self.layer1.T, (2 * (self.y - self.output) * sigmoid_derivative(self.output)))
        d_weights1 = np.dot(self.input.T, (np.dot(2 * (self.y - self.output) * sigmoid_derivative(self.output), self.weights2.T) * sigmoid_derivative(self.layer1)))

        # Обновление весов
        self.weights1 += d_weights1
        self.weights2 += d_weights2

# Пример использования нейросети
if __name__ == "__main__":
    # Входные данные (например, логические И)
    x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    # Ожидаемые выходные данные
    y = np.array([[0], [0], [0], [1]])

    # Создание нейросети
    nn = NeuralNetwork(x, y)

    # Обучение нейросети
    for epoch in range(1500):
        nn.feedforward()  # Прямое распространение
        nn.backprop()     # Обратное распространение

    # Вывод результатов
    print("Выходные данные после обучения:")
    print(nn.output)