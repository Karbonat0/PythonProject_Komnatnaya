# Ввести число. Если оно четное, разделить его на 4, если нечетное - умножить на 5.

while True:
    try:
        a = int(input("Введите число: "))
        cel, ost = divmod(a, 2)
        if ost == 0:
            print(a/4)
        else:
            print(a*5)
    except ValueError:
        print("Неправильно, введите целое число.")
        continue
    break