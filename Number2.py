import numpy as np
import matplotlib.pyplot as plt

x = [3, 21, 22, 34, 54, 34, 55, 67, 89, 99]
x = np.array(x)
y = [2, 22, 24, 65, 79, 82, 55, 130, 150, 199]
y = np.array(y)
plt.scatter(x, y)


def model(a, b, x):
    return a * x + b


def lossFunction(a, b, x, y):
    num = len(x)
    prediction = model(a, b, x)
    return (0.5 / num) * (np.square(prediction - y)).sum()


def optimize(a, b, x, y, Lr):
    num = len(x)
    prediction = model(a, b, x)
    da = (1.0 / num) * ((prediction - y) * x).sum()
    db = (1.0 / num) * ((prediction - y).sum())
    a -= Lr * da
    b -= Lr * db
    return a, b


def iterate(a, b, x, y, times, Lr):
    for i in range(times):
        a, b = optimize(a, b, x, y, Lr)
    return a, b


a = np.random.rand(1)
print(a)
b = np.random.rand(1)
print(b)
Lr = 0.0001
a, b = iterate(a, b, x, y, 1, Lr)
prediction = model(a, b, x)
loss = lossFunction(a, b, x, y)
print(a, b, loss)
plt.scatter(x, y)
plt.plot(x, prediction)
plt.show()
