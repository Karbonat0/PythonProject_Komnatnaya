# Дано целое число. Если оно является положительным, то прибавить к нему 20, в
# противном случае вычесть из него 5.

while True:
    try:
        a = int(input("Введите число: "))
        if a > 0:
           print(a+20)
        else:
            print(a-5)
    except ValueError:
        print("Неправильно, введите целое число. ")
        continue
    break