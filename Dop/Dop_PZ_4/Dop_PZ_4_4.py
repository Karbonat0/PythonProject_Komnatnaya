# Найти и вывести на экран S=1!+2!+3!+4!+…+n! (n>1).

while True:
    try:
        while True:
            n = int(input("Введите целое число больше единицы: "))
            if n <= 1:
                print("Ошибка! Число должно быть больше единицы.")
                continue
    except ValueError:
        print("Ошибка! Введите целое число.")
        continue

