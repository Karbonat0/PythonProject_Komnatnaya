# С помощью функций получить вертикальную и горизонтальную линии. Линия
# проводится многократной печатью символа. Заключить слово в рамку из
# полученных линий.

def gorLine(text):
    k = len(text)
    gl = " " + (2 + k) * "—"
    print(gl)
    return
def vertLine(text):
    vl = "| " + text + " |"
    print(vl)
    return
def ramka(text):
    gorLine(text)
    vertLine(text)
    gorLine(text)
    return

while True:
    try:
        vashText = input("Введите текст: ")
    except ValueError:
        print("Ошибка!")
        continue
    break

ramka(vashText)