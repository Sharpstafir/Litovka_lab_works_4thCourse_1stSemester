import math
import numpy as np
import matplotlib.pyplot as plt

# Параметры
lambda1 = 5**9
lambda2 = 3**10
N = 200
x0 = 1  # начальное значение

# Генерация случайных чисел
x = [x0]
for i in range(1, N):
    x.append((lambda1 * x[i-1]) % lambda2)
x_centered = [xi / lambda2 - 0.5 for xi in x]

# Проверка характеристик
M_x = np.mean(x_centered)
sigma_x2 = np.var(x_centered)

print(f"x = {x}")
print(f"M_x = {M_x:.6f}")
print(f"σ_x^2 = {sigma_x2:.6f}")

# Параметры процесса
M0 = 100
sigma0_2 = 900
alpha0 = 0.1
A1 = A2 = 1.0
Ns = 10

# Вычисление z(k)
z = []
for k in range(N - Ns):
    sum_val = 0
    for i in range(k, k + Ns):
        sum_val += x_centered[i] * math.sqrt(sigma0_2 / (sigma_x2 * alpha0)) * A1 * math.exp(-A2 * alpha0 * (i - k))
    z.append(sum_val / Ns + M0)

# Характеристики процесса z
M_z = np.mean(z)
sigma_z2 = np.var(z)
print(f"M_z = {M_z:.2f}")
print(f"σ_z^2 = {sigma_z2:.2f}")

K = []
for s in range(20):
    sum_k = 0
    for i in range(len(z) - s):
        sum_k += (z[i] - M_z) * (z[i + s] - M_z)
    K.append(sum_k / (len(z) - s))

# Аппроксимация K(s) = σ_z^2 * exp(-α_c * |s|)
# Находим α_c через логарифмирование:
alpha_c = -math.log(abs(K[1]) / sigma_z2) if K[1] != 0 else alpha0
print(f"α_c = {alpha_c:.3f}")
print(K)

tol = 0.1  # 10%
if (abs(M_z - M0) / M0 > tol or
    abs(sigma_z2 - sigma0_2) / sigma0_2 > tol or
    abs(alpha_c - alpha0) / alpha0 > tol):
    print("Требуется уточнение A1, A2")
    # Здесь можно добавить цикл подбора A1, A2
else:
    print("Характеристики в пределах допуска")

plt.plot(x)
plt.show()

plt.plot(z)
plt.show()