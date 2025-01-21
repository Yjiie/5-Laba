'''Лабораторная работа №5 
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно (значение, время). 
Определить (смоделировать) границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
Вариант 14.	F(n<2) = -23; F(n) = (-1)n*(F(n-1)-(n-2)) (при n четном), F(n)=(n-2) /(2n)!- F(n-1) (при n нечетном)
'''
import time
import math
import matplotlib.pyplot as plt
import sys

def recursive_f(n):
    if n < 2:
        return -23
    if n % 2 == 0:
        return (-1)**n * (recursive_f(n-1) - (n-2))
    else:
        return (n-2) / math.factorial(2*n) - recursive_f(n-1)

def iterative_f(n):
    if n < 2:
        return -23
    f_prev = -23
    for i in range(2, n+1):
        if i % 2 == 0:
            f_curr = (-1)**i * (f_prev - (i-2))
        else:
            f_curr = (i-2) / math.factorial(2*i) - f_prev
        f_prev = f_curr
    return f_prev

def compare_times_and_limits(max_n):
    recursive_times = []
    iterative_times = []
    values = []
    recursion_limit = sys.getrecursionlimit()
    max_recursive_n = None

    for n in range(1, max_n + 1):
        start_time = time.time()
        try:
            recursive_f(n)
            recursive_times.append(time.time() - start_time)
            max_recursive_n = n
        except RecursionError:
            recursive_times.append(None)
            break

        start_time = time.time()
        iterative_f(n)
        iterative_times.append(time.time() - start_time)

        values.append(n)

    return values, recursive_times, iterative_times, max_recursive_n, recursion_limit

def plot_results(values, recursive_times, iterative_times):
    plt.figure(figsize=(10, 6))
    filtered_recursive_times = [t if t is not None else float('nan') for t in recursive_times]
    plt.plot(values, filtered_recursive_times, label='Рекурсивный подход', marker='o')
    plt.plot(values, iterative_times, label='Итерационный подход', marker='s')
    plt.xlabel('n')
    plt.ylabel('Время выполнения (секунды)')
    plt.title('Сравнение времени выполнения рекурсивного и итерационного подходов')
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    max_n = 100
    values, recursive_times, iterative_times, max_recursive_n, recursion_limit = compare_times_and_limits(max_n)

    print("n\tРекурсивный (с)\tИтерационный (с)")
    for i in range(len(values)):
        if recursive_times[i] is not None:
            recursive_time_str = f"{recursive_times[i]:.6f}"
        else:
            recursive_time_str = "RecursionError"
        print(f"{values[i]}\t{recursive_time_str}\t\t{iterative_times[i]:.6f}")

    print("\nГраницы применимости:")
    print(f"Максимальное значение n для рекурсии: {max_recursive_n}")
    print(f"Ограничение стека рекурсии: {recursion_limit}")

    plot_results(values, recursive_times, iterative_times)

