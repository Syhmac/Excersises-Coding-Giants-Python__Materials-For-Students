import turtle as t

## Zadanie: Stwórz program, w którym żółw podąża za myszą.
## Mechanika:
#    1. Kliknięcie w ekran przenosi żółwia w to miejsce (`onclick`).
#    2. Naciśnięcie klawisza "space" czyści ekran (`onscreenclick` lub `onkey`).
#    3. Użyj pętli `while True:`, w której żółw stale obraca się o 1 stopień dopóki program działa.
## Wyzwanie: Dodaj zmienną czy_rysowac (typ bool). Kliknięcie przycisku p powinno zmieniać jej wartość
# (True/False), co decyduje, czy żółw zostawia ślad (pendown/penup).

czy_rysowac = True

def przenies(x, y):
    if czy_rysowac:
        t.pendown()
    else:
        t.penup()
    t.goto(x, y)

def czysc():
    t.clear()

def przelacz_rysowanie():
    global czy_rysowac # Używamy zmiennej zdefiniowanej poza funkcją
    czy_rysowac = not czy_rysowac # Odwracamy True na False i odwrotnie
    print(f"Czy rysowanie włączone: {czy_rysowac}")

# Ustawienia ekranu
screen = t.Screen()
screen.listen() # Nasłuchiwanie klawiatury

# Reakcje na zdarzenia
screen.onclick(przenies)        # Lewy przycisk myszy: przenieś/rysuj
screen.onkey(czysc, "space")    # Spacja: czyść ekran
screen.onkey(przelacz_rysowanie, "p") # Klawisz 'p': włącz/wyłącz pisak

# Pętla animacji (żółw kręci się w miejscu)
while True:
    t.left(1)