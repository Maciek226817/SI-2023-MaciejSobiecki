#WERSJA1--------------------------------------------------------------------------------


# import numpy as np
#
# # Wektor cech wejściowych (bias ustawiony na 1)
# X = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
#
# # Wektor oczekiwanych wyników
# Y_AND = np.array([0, 0, 0, 1])
# Y_NOT = np.array([1, 1, 0, 0])
#
# # Inicjalizacja wag
# w_AND = np.zeros(X.shape[1])
# w_NOT = np.zeros(X.shape[1])
#
# # Funkcja progowa
# def step(x):
#     return 1 if x > 0 else 0
#
# # Algorytm uczenia perceptronu
# def perceptron_learn(X, Y, w):
#     learning_rate = 0.1
#     epoch = 20
#     for _ in range(epoch):
#         for i in range(X.shape[0]):
#             y_pred = step(np.dot(X[i], w))
#             error = Y[i] - y_pred
#             w += learning_rate * error * X[i]
#     return w
#
# # Uczenie perceptronu dla funkcji logicznej AND
# w_AND = perceptron_learn(X, Y_AND, w_AND)
#
# # Uczenie perceptronu dla funkcji logicznej NOT
# w_NOT = perceptron_learn(X, Y_NOT, w_NOT)
#
# # Testowanie perceptronów
# test_input = np.array([[1, 0, 0], [1, 0, 1], [1, 1, 0], [1, 1, 1]])
# for x in test_input:
#     and_result = step(np.dot(x, w_AND))
#     not_result = step(np.dot(x, w_NOT))
#
# print(f"For inputs {x}, AND output is {and_result} and NOT output is {not_result}")
#
# # Przykładowy wynik działania programu:
# # For inputs [1 0 0], AND output is 0 and NOT output is 1
# # For inputs [1 0 1], AND output is 0 and NOT output is 1
# # For inputs [1 1 0], AND output is 0 and NOT output is 0
# # For inputs [1 1 1], AND output is 1 and NOT output is 0

# WERSJA2-----------------------------------------------------------------------------------

import numpy as np

class Perceptron:
    def __init__(self, input_size, learning_rate=0.1):
        self.weights = np.random.rand(input_size + 1)
        self.learning_rate = learning_rate

    def predict(self, inputs):
        inputs = np.append(inputs, 1)  # Dodanie stałej wartości 1 dla biasu
        summation = np.dot(inputs, self.weights)
        return 1 if summation > 0 else 0

    def train(self, training_inputs, training_outputs, epochs):
        for _ in range(epochs):
            for inputs, target in zip(training_inputs, training_outputs):
                prediction = self.predict(inputs)
                error = target - prediction
                weight_update = self.learning_rate * error
                self.weights[:-1] += weight_update * inputs
                self.weights[-1] += weight_update  # Aktualizacja biasu

# 1. Napisz Perceptron-Learn Program
and_training_inputs = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
and_training_outputs = np.array([0, 0, 0, 1])
and_perceptron = Perceptron(2)
and_perceptron.train(and_training_inputs, and_training_outputs, 100)

not_training_inputs = np.array([[0], [1]])
not_training_outputs = np.array([1, 0])
not_perceptron = Perceptron(1)
not_perceptron.train(not_training_inputs, not_training_outputs, 100)

# 2. Projektowanie perceptronu z dwoma wejściami reprezentującymi funkcję boolowską x1 ∧ ¬x2
and_not_perceptron = Perceptron(2)
def and_not(x1, x2):
    not_x2 = not_perceptron.predict([x2])
    return and_perceptron.predict([x1, not_x2])

# 3. Projektowanie dwuwarstwowej sieci perceptronów implementujących x1 XOR x2
def xor(x1, x2):
    and_result = and_perceptron.predict([x1, x2])
    or_result = and_perceptron.predict([x1, 1]) or and_perceptron.predict([0, x2])  # Zakładając, że mamy już perceptron OR
    return and_not(or_result, and_result)

# Testowanie kodu
print("AND perceptron:")
for i in and_training_inputs:
    print(f"{i} -> {and_perceptron.predict(i)}")

print("\nNOT perceptron:")
for i in not_training_inputs:
    print(f"{i} -> {not_perceptron.predict(i)}")

print("\nAND-NOT perceptron:")
for i in and_training_inputs:
    print(f"{i} -> {and_not(i[0], i[1])}")

print("\nXOR perceptron:")
for i in and_training_inputs:
    print(f"{i} -> {xor(i[0], i[1])}")