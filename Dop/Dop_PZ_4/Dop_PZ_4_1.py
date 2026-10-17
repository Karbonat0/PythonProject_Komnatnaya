# Ввести 4 числа. Найти и вывести на экран сумму и количество отрицательных чисел.

r = 0
s = 0
k = 0

while r < 4:
    while True:
        try:
            a = int(input("Введите целое число: "))
        except ValueError:
            print("Ошибка! Введите целые числа.")
            continue
        break
    s += a
    if a < 0:
        k += 1
    r += 1

print("Сумма чисел: ", s)
print("Кол-во отрицательных чисел: ", k)