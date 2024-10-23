'''Лабораторная работа №5 
Задана рекуррентная функция. Область определения функции – натуральные числа. Написать программу сравнительного вычисления данной функции рекурсивно и итерационно (значение, время). 
Определить (смоделировать) границы применимости рекурсивного и итерационного подхода. Результаты сравнительного исследования времени вычисления представить в табличной и графической форме в виде отчета по лабораторной работе.
Вариант 14.	F(n<2) = -23; F(n) = (-1)n*(F(n-1)-(n-2)) (при n четном), F(n)=(n-2) /(2n)!- F(n-1) (при n нечетном)
'''
import timeit
import matplotlib.pyplot as plt

# Рекурсивная функция для вычисления F(n)
def recursive_F(n):
    if n < 2:
        return -23
    elif n % 2 == 0:
        return (-1)**n * (recursive_F(n-1) - (n-2))
    else:
        return (n-2) / (2*n) - recursive_F(n-1)

# Итеративная функция для вычисления F(n)
def iterative_F(n):
    if n < 2:
        return -23
    F = [-23, -23]  # F(0) = -23, F(1) = -23
    for i in range(2, n+1):
        if i % 2 == 0:
            F.append((-1)**i * (F[i-1] - (i-2)))
        else:
            F.append((i-2) / (2*i) - F[i-1])
    return F[n]

# Функция для записи времени
def score_time(func, n):
    return timeit.timeit(lambda: func(n), number=1000)

# Значения n для которых мы хотим измерить время выполнения
n_values = range(2, 21)
recursive_times = []
iterative_times = []

# Измерение времени выполнения для каждого значения n
for n in n_values:
    recursive_times.append(score_time(recursive_F, n))
    iterative_times.append(score_time(iterative_F, n))

# Вывод результатов в табличной форме
print(f"{'n':<10}{'Рекурсивное время (мс)':<25}{'Итерационное время (мс)':<25}")
for i, n in enumerate(n_values):
    print(f"{n:<10}{recursive_times[i]:<25}{iterative_times[i]:<25}")

# Построение и вывод графика результатов
plt.plot(n_values, recursive_times, label='Рекурсивно')
plt.plot(n_values, iterative_times, label='Итерационно')
plt.xlabel('n')
plt.ylabel('Время (в миллисекундах)')
plt.legend()
plt.title('Сравнение времени вычисления функции F(n)')
plt.show()
