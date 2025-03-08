# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 21:30:32 2025

@author: AM4
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('data.csv')

print(df.head())

y = df.iloc[:, 4].values
y = np.where(y == "Iris-setosa", 1, -1)

X = df.iloc[:, [0, 1, 2]].values  # Теперь используем три признака

plt.figure()
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='red', marker='o', label='Class 1')
plt.scatter(X[y == -1, 0], X[y == -1, 1], color='blue', marker='x', label='Class -1')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()
plt.show()

def neuron(w, x):
    value = w[0] + w[1] * x[0] + w[2] * x[1] + w[3] * x[2]
    predict = 1 if value >= 0 else -1
    return predict

w = np.array([0, 0.1, 0.4, 0.2])  # Добавляем вес для третьего признака
print(neuron(w, X[2]))

w = np.random.random(4)  # Теперь весов на один больше
eta = 0.01
w_iter = []

for xi, target, j in zip(X, y, range(X.shape[0])):
    predict = neuron(w, xi)
    w[1:] += eta * (target - predict) * xi
    w[0] += eta * (target - predict)
    if j % 10 == 0:
        w_iter.append(w.tolist())

sum_err = 0
for xi, target in zip(X, y):
    predict = neuron(w, xi)
    sum_err += (target - predict) / 2

print("Всего ошибок: ", sum_err)

xl = np.linspace(min(X[:, 0]), max(X[:, 0]))

plt.figure()
plt.scatter(X[y == 1, 0], X[y == 1, 1], color='red', marker='o', label='Class 1')
plt.scatter(X[y == -1, 0], X[y == -1, 1], color='blue', marker='x', label='Class -1')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.legend()

for i, w in zip(range(len(w_iter)), w_iter):
    yl = -(xl * w[1] + w[0]) / w[2]
    plt.plot(xl, yl)
    plt.text(xl[-1], yl[-1], i, dict(size=10, color='gray'))
    plt.pause(1)

plt.text(xl[-1] - 0.3, yl[-1], 'END', dict(size=14, color='red'))
plt.show() 


