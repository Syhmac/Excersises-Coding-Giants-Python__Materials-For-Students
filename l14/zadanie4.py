import turtle as t

## Zadanie: Stwórz program, w którym żółw podąża za myszą.
## Mechanika:
#    1. Kliknięcie w ekran przenosi żółwia w to miejsce (`onclick`).
#    2. Naciśnięcie klawisza "space" czyści ekran (`onscreenclick` lub `onkey`).
#    3. Użyj pętli `while True:`, w której żółw stale obraca się o 1 stopień dopóki program działa.
## Wyzwanie: Dodaj zmienną czy_rysowac (typ bool). Kliknięcie przycisku p powinno zmieniać jej wartość
# (True/False), co decyduje, czy żółw zostawia ślad (pendown/penup).