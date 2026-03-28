ceny = [5.5, 2.99, 6.80, 10.25]

# Policz średnią cen i wypisz na ekran
# Magic numbers - sztywno wpisane numery w program, które nie wiadomo skąd się wzięły
# Numery te zepsułyby nam program, gdyby coś się zmieniło w programie, np. byłoby więcej elementów w liście

suma = ceny[0] + ceny[1] + ceny[2] + ceny[3]
avg = suma / len(ceny)
print(f'Średnia = {avg}')