import math

import numpy as np
import matplotlib.pyplot as plt

#Общие данные
a = 0.013
delta_x=0.1
X = 1
tau_max = 100

#Данные варианта
def fi(x):
    return 21 - x
def f1(tau):
    return 15+9/(math.exp(0.1*tau)+0.5)
def f2(tau):
    return 0.0005*tau*tau + 0.07*tau + 20

# 1. Создание фигуры и 3D-осей
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# 2. Подготовка данных
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# 3. Построение поверхности
ax.plot_surface(X, Y, Z, cmap='viridis')

# Добавление меток осей
ax.set_xlabel('X-ось')
ax.set_ylabel('Y-ось')
ax.set_zlabel('Z-ось')

# 4. Отображение графика
plt.show()