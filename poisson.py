import numpy as np
import matplotlib.pyplot as plt

# Задаємо параметри
intensity = 1  # середня інтенсивність подій
total_time = 50  # загальний час спостереження
event_type = 5
num_simulations = 1500
event_type_times = []
event_type1_times = []

N = intensity * total_time


# МОДЕЛЮВАННЯ ПУАСОНІВСЬКОГО ПРОЦЕСУ (15)
def poisson_process(intensity, total_time):
    time = 0
    event_times = []

    while time < total_time:
        # Генеруємо експоненційно розподілений час до наступної події
        time_to_next_event = np.random.exponential(1/intensity)
        time += time_to_next_event

        # Додаємо час до події до списку
        if time < total_time:
            event_times.append(time)

    return event_times


# Моделюємо та візуалізуємо 15 Пуассонівських процесів
def model_small():
    plt.figure(figsize=(10, 6))
    for _ in range(15):
        event_times = poisson_process(intensity, total_time)
        plt.step(event_times, range(len(event_times)), where='post')

    plt.title('Моделювання 15 Пуассонівських процесів')
    plt.xlabel('Час')
    plt.ylabel('Кількість подій')
    plt.show()


# МОДЕЛЮВАННЯ ПУАСОНІВСЬКОГО ПРОЦЕСУ (100)
def poisson_process1(intensity, total_time, event_type):
    time = 0
    event_times = []
    event_count = 0
    event_type_time = 0.0

    while time < total_time:
        # Генеруємо експоненційно розподілений час до наступної події
        time_to_next_event = np.random.exponential(1/intensity)
        time += time_to_next_event
        event_count += 1

        # Додаємо час до події до списку
        if time < total_time:
            event_times.append(time)

        # Якщо досягли вказаної події, повертаємо час до її виникнення
        if event_count == event_type:
            event_type_time = time

    return event_times, event_type_time


# Моделюємо та зберігаємо часи появи певної події
def model_event():
    all_interval_times = []
    num_events_list = []

    for _ in range(num_simulations):
        event_times, event_appearance = poisson_process1(intensity, total_time, event_type)
        num_events = len(event_times)
        num_events_list.append(num_events)
        if event_appearance is not None:
            event_type_times.append(event_appearance)
        # Рахуємо інтервали між подіями
        interval_times = np.diff(event_times)
        # Зберігаємо інтервали
        all_interval_times.extend(interval_times)

    # Створюємо гістограму розподілу часу появи 5-ої події
    plt.figure(figsize=(10, 6))
    plt.hist(event_type_times, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Гістограма розподілу часу появи 5-ої події в 1500 симуляціях Пуассонівського процесу')
    plt.xlabel('Час появи 5-ої події')
    plt.ylabel('Кількість симуляцій')
    plt.show()

    # Створюємо гістограму розподілу інтервалів між подіями
    plt.figure(figsize=(10, 6))
    plt.hist(all_interval_times, bins=30, edgecolor='black', alpha=0.7)
    plt.title('Гістограма розподілу інтервалів між подіями в симуляціях Пуассонівського процесу')
    plt.xlabel('Інтервал між подіями')
    plt.ylabel('Кількість подій')
    plt.show()

    # Define the conditions
    less_than_50 = np.array(num_events_list) < 50
    equal_to_50 = np.array(num_events_list) == 50
    greater_than_50 = np.array(num_events_list) > 50

    # Count occurrences based on conditions
    counts = [np.sum(less_than_50), np.sum(equal_to_50), np.sum(greater_than_50)]

    # Plot the histogram
    labels = ['Менше 50', 'Рівно 50', 'Більше 50']
    plt.bar(labels, counts, edgecolor='black')
    plt.title('Розподіл кількості подій')
    plt.xlabel('Кількість подій')
    plt.ylabel('Частота')
    plt.show()


model_event()
