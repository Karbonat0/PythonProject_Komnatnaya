#С помощью функций получить вертикальную и горизонтальную линии.

while True:
    try:
        ttt = input("Введите текст: ")
    except ValueError:
        print("Ошибка!")
        continue
    break

def ramka(text):
    k = len(text)
    rv = (2 + k) * "—"
    rs = "| " + text + " |"
    print(" " + rv, rs, " " + rv, sep = "\n")

ramka(ttt)