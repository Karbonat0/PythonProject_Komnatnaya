# Ввести двухзначное число. Если сумма цифр числа четная, то увеличить число на 2,
# в противном случае уменьшить на 2.

while True:
    try:
        while  True:
            a = int(input("Введите двухзначное число: "))
            if (10 <= a <= 99):
                p, v = divmod(a, 10)
                if (p + v) % 2 == 0:
                    print(2*(p + v))
                else:
                    print((p + v)/2)
                break
            else:
                print("Ошибка, введите двухзначное число.")
    except ValueError:
        print("Ошибка, введите корректное целое число.")
        continue
    break