# Ввести N чисел. Найти и вывести их среднее арифметическое.

while True:
    try:
        N = int(input("Введите, сколько чисел вы хотите ввести: "))
    except ValueError:
        print("Ошибка! Введите целое числа.")
        continue
    break

k = 0
S = 0

while k < N:
    while True:
        try:
            a = int(input("Введите целое число: "))
        except ValueError:
            print("Ошибка! Введите целые числа.")
            continue
        break
    S += a
    k += 1

print("Среднее арифметическое:", S/N)