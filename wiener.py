import numpy as np
import matplotlib.pyplot as plt


def brownian_bridge_operator(t, nu, num_terms=50):
    result = t * nu[0]
    for i in range(1, num_terms + 1):
        result += np.sqrt(2) * (np.sin(i * np.pi * t) / (i * np.pi)) * nu[i]
    return result


def generate_wiener_process_operator(T, N, num_terms=50):
    t = np.linspace(0, T, N + 1)
    nu = np.random.normal(0, 1, num_terms + 1)
    epsilon_t = np.array([brownian_bridge_operator(t[i], nu) for i in range(N + 1)])
    return epsilon_t


def first_exit_time(t, W, a):
    for i in range(len(W)):
        if W[i] >= a:
            return t[i]
    return None


def simulate_multiple_processes(num_simulations, T, N):
    mean_values = np.zeros(num_simulations)
    variance_values = np.zeros(num_simulations)

    for i in range(num_simulations):
        epsilon_t = generate_wiener_process_operator(T, N)
        mean_values[i] = np.mean(epsilon_t)
        variance_values[i] = np.var(epsilon_t)

    return mean_values, variance_values


# Параметри
T = 1.0  # часовий інтервал
N = 250  # кількість кроків
num_simulations = 100  # кількість реалізацій
a = 0.5  # рівень
t = np.linspace(0, T, N + 1)

# Генеруємо Вінерівський процес з оператором броунівського мосту
epsilon_t = generate_wiener_process_operator(T, N)

# Знаходимо час першого виходу за рівень
exit_time = first_exit_time(t, epsilon_t, a)

print(f'Час першого виходу за рівень {a}: {exit_time}')

# Будуємо графік
plt.step(t, epsilon_t)
plt.title('Вінерівський процес з використанням оператора броунівського мосту')

plt.hlines(y=a, xmin=0, xmax=exit_time, color='green', linestyle='--')
plt.vlines(x=exit_time, ymin=min(epsilon_t), ymax=a, color='red', linestyle='--')

plt.xlabel('Час')
plt.ylabel('Значення')
plt.show()

mean_values, variance_values = simulate_multiple_processes(num_simulations, T, N)

nums = []
for i in range(0, num_simulations):
    nums.append(i + 1)

# Будуємо графік середнього значення
plt.plot(nums, mean_values, marker='o', linestyle='None')
plt.title('Середнє значення для 100 реалізацій')
plt.xlabel('Номер реалізації')
plt.ylabel('Середнє значення')
plt.show()

# Будуємо графік дисперсії
plt.plot(nums, variance_values, marker='o', linestyle='None')
plt.title('Дисперсія для 100 реалізацій')
plt.xlabel('Номер реалізації')
plt.ylabel('Дисперсія')
plt.show()