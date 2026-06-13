import turtle as t

## Zadanie: Stwórz funkcję mozaika(), która narysuje wzór składający się z obróconych figur.
## Opis: Narysuj kwadrat, obróć żółwia o 10 stopni i powtórz to 36 razy.
## Wymagania: Wykorzystaj zmienną rozmiar, która przy każdym kolejnym kwadracie
# będzie się zwiększać o 5 pikseli. Powstanie efekt "rozrastającej się" spirali kwadratów.

t.speed(0)
t.bgcolor("black") # Zmieniamy tło na czarne dla lepszego efektu
t.color("cyan")

rozmiar = 20 # Zmienna początkowa

# Zewnętrzna pętla: 36 obrotów po 10 stopni (pełne koło 360)
for _ in range(36):
    # Wewnętrzna pętla: rysuje jeden kwadrat
    for _ in range(4):
        t.forward(rozmiar)
        t.left(90)
    
    t.left(10)      # Obrót o 10 stopni
    rozmiar = rozmiar + 5 # Zwiększamy rozmiar kolejnego kwadratu

t.done()