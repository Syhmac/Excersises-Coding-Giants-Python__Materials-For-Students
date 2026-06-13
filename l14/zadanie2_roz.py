import turtle as t

## Zadanie: Stwórz listę kolorów (np. ["red", "blue", "green", "orange", "purple"]).
# Następnie za pomocą pętli for narysuj 5 kwadratów w różnych miejscach na ekranie.
## Wymaganie: Każdy kwadrat musi mieć inny kolor pobrany z Twojej listy.
## Zagnieżdżanie: Pętla for (do kwadratów) powinna być wewnątrz innej pętli for
# (przesuwającej żółwia w nowe miejsce).
## Podpowiedź: Użyj turtle.penup() i turtle.goto(x, y) przed rysowaniem każdego kształtu,
# żeby nie zostawiać śladu przejścia.

kolory = ["red", "blue", "green", "orange", "purple"]
pozycje_x = [-200, -100, 0, 100, 200]

t.speed(0)

for i in range(5):
    # Skok w nowe miejsce bez rysowania
    t.penup()
    t.goto(pozycje_x[i], 0)
    t.pendown()
    
    # Wybór koloru z listy
    t.color(kolory[i])
    
    # Zagnieżdżona pętla rysująca kwadrat
    for _ in range(4):
        t.forward(50)
        t.left(90)

t.done()