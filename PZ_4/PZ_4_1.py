# Практическое задание 4, вариант 14, №1.
# Дано вещественное число A и целое число N (>0). Используя один цикл, вывести все
# целые степени числа A от 1 до N.

while True:
    try:
        A = float(input("Введите число с плавающей точкой: "))
        while True:
            N = int(input("Введите  положительное целое число: "))
            if N < 0:
                print("Введите положительное число!")
                continue
            else:
                break
    except ValueError:
        print("Ошибка! Введите корректные числа.")
        continue
    break

k = 0
s = 0

while k < N:
    k += 1
    s = A ** k
    print(s)

