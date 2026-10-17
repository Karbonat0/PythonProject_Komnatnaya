# Ввести 4 числа. Найти и вывести на экран количество четных чисел.

r = 0
k = 0

while r < 4:
    while True:
        try:
            a = int(input("Введите целое число: "))
        except ValueError:
            print("Ошибка! Введите целые числа.")
            continue
        break
    if a % 2 == 0:
        k += 1
    r += 1

print("Кол-во чётных чисел: ", k)