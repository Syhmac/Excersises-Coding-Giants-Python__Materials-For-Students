import turtle as t

## Zadanie: Napisz funkcję rysuj_figure(boki, dlugosc, kolor), która narysuje dowolny wielokąt foremny.
## Wymaganie: Użyj instrukcji if, aby sprawdzić, czy liczba boków jest większa niż 2.
# Jeśli nie, żółw powinien wypisać komunikat o błędzie na ekranie (turtle.write).
## Matematyka: Kąt obrotu to zawsze $360 / boki$ .

def rysuj_figure(boki, dlugosc, kolor):
    t.color(kolor)
    
    # Warunek sprawdzający, czy figura jest możliwa do narysowania
    if boki < 3:
        t.write("Błąd: Figura musi mieć co najmniej 3 boki!", font=("Arial", 12, "bold"))
    else:
        kat = 360 / boki
        t.begin_fill() # Wypełnienie figury kolorem
        for _ in range(boki):
            t.forward(dlugosc)
            t.left(kat)
        t.end_fill()

# Testowanie funkcji
rysuj_figure(6, 100, "purple") # Rysuje sześciokąt
# rysuj_figure(2, 100, "red")  # Odkomentuj, by zobaczyć błąd
t.done()