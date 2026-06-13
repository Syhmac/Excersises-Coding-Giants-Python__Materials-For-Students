import turtle as t
import random

## Zadanie: Stwórz program, który narysuje "las" składający się z co najmniej 3 różnych typów obiektów
# (np. drzewa, kwiaty, chmury).
## - **Struktura programu:**
#    1. Każdy obiekt (drzewo, chmura) musi mieć własną **funkcję**.
#    2. Użyj **listy współrzędnych** `[[x1, y1], [x2, y2], ...]`, aby określić,
#       gdzie mają pojawić się obiekty.
#    3. Użyj pętli `for`, która przejdzie przez listę współrzędnych i wylosuje (moduł `random`),
#       którą funkcję (jaki obiekt) wywołać w danym miejscu.

t.speed(0)
t.Screen().bgcolor("skyblue")

def rysuj_drzewo(x, y):
    # Pień
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    for _ in range(2):
        t.forward(20)
        t.left(90)
        t.forward(40)
        t.left(90)
    t.end_fill()
    # Korona
    t.penup()
    t.goto(x - 20, y + 40)
    t.pendown()
    t.color("green")
    t.begin_fill()
    for _ in range(3):
        t.forward(60)
        t.left(120)
    t.end_fill()

def rysuj_chmure(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("white")
    t.begin_fill()
    for _ in range(6):
        t.circle(20)
        t.forward(15)
    t.end_fill()

def rysuj_kwiat(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("yellow")
    for _ in range(8):
        t.circle(10, 180)
        t.left(135)

# Lista współrzędnych, gdzie chcemy coś narysować
miejsca = [[-200, -100], [-100, -150], [0, -100], [150, -120], [-150, 150], [50, 180]]

for poz in miejsca:
    losowa_liczba = random.randint(1, 3) # Losujemy typ obiektu
    
    if losowa_liczba == 1:
        rysuj_drzewo(poz[0], poz[1])
    elif losowa_liczba == 2:
        rysuj_chmure(poz[0], poz[1])
    else:
        rysuj_kwiat(poz[0], poz[1])

t.hideturtle()
t.done()