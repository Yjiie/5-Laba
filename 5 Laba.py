'''Лабораторная работа №5 
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно (значение, время). 
Определить (смоделировать) границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
Вариант 14.	F(n<2) = -23; F(n) = (-1)n*(F(n-1)-(n-2)) (при n четном), F(n)=(n-2) /(2n)!- F(n-1) (при n нечетном)
'''
import math
import time
import matplotlib.pyplot as plt

def iterative_f(n):
    if n < 2:
        return -23
    prev = -23  # F(1)
    for k in range(2, n + 1):
        if k % 2 == 0:
            current = (-1) ** k * (prev - (k - 2))
        else:
            factorial = math.factorial(2 * k)
            current = ( (k - 2) / factorial ) - prev
        prev = current
    return prev

def recursive_f(n):
    if n < 2:
        return -23
    else:
        prev = recursive_f(n - 1)
        if n % 2 == 0:
            return (-1) ** n * (prev - (n - 2))
        else:
            factorial = math.factorial(2 * n)
            return ( (n - 2) / factorial ) - prev

def measure_time(func, n):
    start = time.time()
    result = func(n)
    end = time.time()
    return end - start, result

def main():
    n_values = list(range(1, 201, 10))  # Диапазон значений n с шагом 10 до 200
    data = []

    for n in n_values:
        # Итеративный метод
        time_iter, result_iter = measure_time(iterative_f, n)
        # Рекурсивный метод
        time_rec, result_rec = None, None
        try:
            time_rec, result_rec = measure_time(recursive_f, n)
        except RecursionError:
            time_rec = float('inf')
            result_rec = "Ошибка"
        data.append( (n, time_iter, time_rec, result_iter, result_rec) )

    # Поиск границы для рекурсии
    max_rec_n = 0
    try:
        while True:
            recursive_f(max_rec_n + 1)
            max_rec_n += 1
    except RecursionError:
        pass

    # Вывод таблицы
    print("n | Время итеративный (с) | Время рекурсивный (с) | F(n) итер | F(n) рекурс")
    for row in data:
        print(f"{row[0]} | {row[1]:.6f} | {row[2] if row[2] != float('inf') else 'Ошибка'} | {row[3]} | {row[4]}")

    # Построение графика
    n_list = [row[0] for row in data]
    time_iter_list = [row[1] for row in data]
    time_rec_list = [row[2] if row[2] != float('inf') else None for row in data]

    plt.figure(figsize=(12, 6))
    plt.plot(n_list, time_iter_list, label='Итеративный', marker='o')
    plt.plot(n_list, time_rec_list, label='Рекурсивный', marker='x', linestyle='--')
    plt.xlabel('n')
    plt.ylabel('Время (секунды)')
    plt.title('Сравнение времени вычисления функции')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(f"\nМаксимальное n для рекурсии: {max_rec_n}")

main()  

