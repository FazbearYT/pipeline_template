import matplotlib.pyplot as plt
import numpy as np

# 1. Исходные данные (из расчетов выше)
# Масса (кг)
m = np.array([0.020, 0.010, 0.0067])
# Скорость (м/с)
v = np.array([3.21, 4.59, 5.38])
# Погрешность скорости (м/с)
dv = np.array([0.06, 0.14, 0.16])

# 2. Вычисление координаты X: 1/sqrt(m)
x = 1 / np.sqrt(m)

# 3. Настройка графика
fig, ax = plt.subplots(figsize=(8, 6))

# Построение точек с ошибками (errorbar)
ax.errorbar(x, v, yerr=dv, fmt='o', color='black',
            ecolor='gray', capsize=5, markersize=8, label='Экспериментальные данные')

# 4. Построение линии тренда (аппроксимация)
# Согласно физике задачи (E = mv^2/2 = const), зависимость линейная v = k * (1/sqrt(m))
# Строим линейную регрессию.
# Если нужно, чтобы линия шла строго через 0, используем np.polyfit(x, v, 1) и корректируем.
# Для простоты здесь используется стандартный линейный тренд (y = kx + b).
coefficients = np.polyfit(x, v, 1)
polynomial = np.poly1d(coefficients)
x_trend = np.linspace(0, 14, 100)
y_trend = polynomial(x_trend)

ax.plot(x_trend, y_trend, color='red', linestyle='--', linewidth=2, label='Линейная аппроксимация')

# 5. Оформление
ax.set_title('Зависимость скорости пули от обратной величины корня из массы', fontsize=14)
ax.set_xlabel('1/√m (кг^(-1/2))', fontsize=12)
ax.set_ylabel('v (м/с)', fontsize=12)
ax.grid(True, which='both', linestyle='-', alpha=0.5)
ax.legend()

# Устанавливаем пределы осей для красоты
ax.set_xlim(0, 14)
ax.set_ylim(0, 6.5)

# 6. Сохранение и показ
plt.tight_layout()
plt.savefig('graph_ballistic_pendulum.png', dpi=300)
print("График сохранен как 'graph_ballistic_pendulum.png'")
plt.show()