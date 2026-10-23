# Ввести N чисел. Посчитать и вывести количество чисел равных нулю.

while True:
    try:
        N = int(input("Введите, сколько чисел вы хотите ввести: "))
    except ValueError:
        print("Ошибка! Введите целое числа.")
        continue
    break

k = 0
c = 0

while c < N:
    while True:
        try:
            a = int(input("Введите целое число: "))
        except ValueError:
            print("Ошибка! Введите целые числа.")
            continue
        break
    if a == 0:
        k += 1
    c += 1

print("Кол-во чисел, равных нулю:", k)