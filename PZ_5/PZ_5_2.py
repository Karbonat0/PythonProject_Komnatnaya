# Описать функцию ShiftLeft3(A, B, C), выполняющую левый циклический сдвиг:
#значение A переходит в C, значение C — в B, значение B — в A (A, B, C —
#вещественные параметры, являющиеся одновременно входными и выходными). С
#помощью этой функции выполнить левый циклический сдвиг для двух данных
#наборов из трех чисел: (A1, B1, C1) и (A2, B2, C2).

while True:
    try:
        A = float(input("Введите число: "))
    except ValueError:
        print("Ошибка!")
        continue
    break

while True:
    try:
        B = float(input("Введите число: "))
    except ValueError:
        print("Ошибка!")
        continue
    break

while True:
    try:
        C = float(input("Введите число: "))
    except ValueError:
        print("Ошибка!")
        continue
    break

def ShiftLeft3(A, B, C):
    spisok = []
    spisok.append(A)
    spisok.append(B)
    spisok.append(C)
    spisok.pop(0)
    spisok.insert(2, A)
    print(spisok)
    return

ShiftLeft3(A, B, C)

ShiftLeft3(B, C, A)