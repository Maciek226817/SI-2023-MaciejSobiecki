import np as np


def sigmoid(x, np=None):
    return 1 / (1 + np.exp(-x))

W1 = np.array([[0.15, 0.2], [0.25, 0.3]])
b1 = np.array([0.35, 0.35])
W2 = np.array([[0.4, 0.45]])
b2 = np.array([0.6])

x = np.array([[0.6, 0.1], [0.2, 0.3]])
y = np.array([[1], [0]])

alpha = 0.1

epochs = 10000

for epoch in range(epochs):
    z1 = np.dot(x, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2.T) + b2
    a2 = sigmoid(z2)

    delta2 = (a2 - y) * a2 * (1 - a2)
    delta1 = np.dot(delta2, W2) * a1 * (1 - a1)

    W2 = W2 - alpha * np.dot(a1.T, delta2)
    b2 = b2 - alpha * np.sum(delta2, axis=0, keepdims=True)
    W1 = W1 - alpha * np.dot(x.T, delta1)
    b1 = b1 - alpha * np.sum(delta1, axis=0)

print(f"{x} -> {a2}")