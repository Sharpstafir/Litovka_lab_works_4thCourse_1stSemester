import math

import numpy as np
import matplotlib.pyplot as plt

#Общие данные
a = 0.013
delta_x=0.1
delta_tau = 0.4 * delta_x ** 2 / a
X = 1
tau_max = 100
#Данные варианта
def fi(x):
    return 21 - x
def f1(tau):
    return 15+9/(math.exp(0.1*tau)+0.5)
def f2(tau):
    return 0.0005*tau*tau + 0.07*tau + 20
def solve_heat_equation(fi, f1, f2, a, delta_x, X, tau_max, delta_tau):
    if delta_tau > 0.5 * delta_x ** 2 / a:
        print(f"Предупреждение: условие устойчивости может быть нарушено!")
        print(f"Рекомендуемый dt <= {0.5 * delta_x ** 2 / a:.6f}")

    # Количество узлов по пространству и времени
    Nx = int(X / delta_x) + 1
    Nt = int(tau_max / delta_tau) + 1

    # Сетка
    x = np.linspace(0, X, Nx)
    tau = np.linspace(0, tau_max, Nt)

    # Матрица решения
    T = np.zeros((Nt, Nx))

    # Начальное условие
    for i in range(Nx):
        T[0, i] = fi(x[i])

    # Коэффициент для разностной схемы
    r = a * delta_tau / delta_x ** 2

    # Основной цикл по времени
    for j in range(Nt - 1):
        # Граничные условия
        T[j + 1, 0] = f1(tau[j + 1])  # Левая граница
        T[j + 1, -1] = f2(tau[j + 1])  # Правая граница

        # Внутренние точки
        for i in range(1, Nx - 1):
            T[j + 1, i] = r * (T[j, i + 1] - 2 * T[j, i] + T[j, i - 1]) + T[j, i]

    return T, x, tau

def plot_results(T, x, tau):
    """Визуализация результатов в 3D"""
    from mpl_toolkits.mplot3d import Axes3D

    Tau, X = np.meshgrid(tau, x, indexing='ij')

    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111, projection='3d')

    surf = ax.plot_surface(X, Tau, T, cmap='hot', alpha=0.8)
    ax.set_xlabel('x, м')
    ax.set_ylabel('τ, с')
    ax.set_zlabel('T, °C')
    ax.set_title('Распределение температуры в пластине')

    # Добавляем цветную полосу
    fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

    plt.tight_layout()
    plt.show()

# Решение задачи
print("Решение задачи теплопроводности...")
T, x, tau = solve_heat_equation(fi, f1, f2, a, delta_x, X, tau_max, delta_tau)

# Визуализация результатов
print("Построение графиков...")
plot_results(T, x, tau)