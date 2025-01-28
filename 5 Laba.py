'''Лабораторная работа №5 
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно (значение, время). 
Определить (смоделировать) границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
Вариант 14.	F(n<2) = -23; F(n) = (-1)n*(F(n-1)-(n-2)) (при n четном), F(n)=(n-2) /(2n)!- F(n-1) (при n нечетном)
'''
import time
import math
import matplotlib.pyplot as plt

# Рекурсивная функция для вычисления факториала
def recursive_factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * recursive_factorial(n - 1)

# Итеративная функция для вычисления факториала
def iterative_factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Рекурсивная функция для вычисления F(n)
def recursive_F(n):
    if n < 2:
        return -23
    elif n % 2 == 0:
        return (-1)**n * (recursive_F(n - 1) - (n - 2))
    else:
        return ((n - 2) / math.factorial(2 * n)) - recursive_F(n - 1)

# Итеративная функция для вычисления F(n)
def iterative_F(n):
    if n < 2:
        return -23
    result = -23
    for i in range(2, n + 1):
        if i % 2 == 0:
            result = (-1)**i * (result - (i - 2))
        else:
            result = ((i - 2) / math.factorial(2 * i)) - result
    return result

# Функция для измерения времени
def score_time(func, n):
    start_time = time.time()
    try:
        func(n)
    except (RecursionError, OverflowError):
        return float('inf')  # Для случаев, когда функция не может быть вычислена
    end_time = time.time()
    return (end_time - start_time) * 1000  # перевод в миллисекунды

# Значения n для которых мы хотим измерить время выполнения
n_values = range(2, 100)
recursive_times = []
iterative_times = []

# Границы применимости
recursive_limit = None
iterative_limit = None
# Измерение времени выполнения для каждого значения n
for n in n_values:
    rec_time = score_time(recursive_F, n)
    iter_time = score_time(iterative_F, n)

    # Проверка, где рекурсивная функция перестает работать
    if rec_time == float('inf') and recursive_limit is None:
        recursive_limit = n - 1  # Предыдущее значение было последним успешным

    # Проверка времени итеративной функции
    if iter_time != float('inf'):
        iterative_limit = n  # Последнее успешное значение

    recursive_times.append(rec_time)
    iterative_times.append(iter_time)

# Вывод результатов в табличной форме
print(f"{'n':<10}{'Рекурсивное время (мс)':<25}{'Итерационное время (мс)':<25}")
for i, n in enumerate(n_values):
    print(f"{n:<10}{recursive_times[i]:<25.5f}{iterative_times[i]:<25.5f}")

# Построение и вывод графика результатов
plt.figure(figsize=(10, 6))
plt.plot(n_values, recursive_times, label='Рекурсивно', marker='o')
plt.plot(n_values, iterative_times, label='Итерационно', marker='o')
plt.xlabel('n')
plt.ylabel('Время (в миллисекундах)')
plt.legend()
plt.title('Сравнение времени вычисления функции F(n)')
plt.grid()
plt.show()

    plot_results(values, recursive_times, iterative_times)

