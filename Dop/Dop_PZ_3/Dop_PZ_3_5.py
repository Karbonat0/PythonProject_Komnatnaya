# Дано два числа. Если их сумма кратна 5, то прибавить 1, иначе вычесть 2.

while True:
    try:
        a = int(input("Введите перовое целое число: "))
        b = int(input("Введите второе целое число: "))
        if (a+b) % 5 == 0:
            print(a+b+1)
        else:
            print(a + b -2)
    except ValueError:
        print("Неправильно, введите целые числа. ")
        continue
    break