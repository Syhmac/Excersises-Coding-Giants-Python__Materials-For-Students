lista_zakupów = ['chleb', 'ser', 'mleko', 'czekolada'] # już nie ruszamy
print(lista_zakupów[0]) # pierwszy element
print(lista_zakupów[-1]) # ostatni element

lista_zakupów[1] = 'ser żółty'
print(lista_zakupów)

# lista_zakupów[4] = 'ziemniaki' - błąd
lista_zakupów.append('ziemianki') # dodajemy element na koniec
print(lista_zakupów)

# lista_zakupów.insert(1000, "aa") # Dodanie w miejscu, w którym chcemy
# print(lista_zakupów)

lista_zakupów.remove('czekolada') # usuwanie po wartości
print(lista_zakupów)

lista_zakupów.pop(-1) # usuwanie po indeksie
print(lista_zakupów)

# ['chleb', 'ser żółty', 'mleko']
ceny = [6.0, 4.5, 5.5]

# --- Zakupy ---
# chleb: 6.0 zł
# ser żółty: 4.5 zł
# mleko: 5.5 zł

print('--- Zakupy ---')
print(f'{lista_zakupów[0]}: {ceny[0]} zł')
print(f'{lista_zakupów[1]}: {ceny[1]} zł')
print(f'{lista_zakupów[2]}: {ceny[2]} zł')

print(len(lista_zakupów) - 1) # Ostatni index
lista_zakupów.append('ziemniaki')
lista_zakupów.append('kiełbasa')
lista_zakupów.append('kawa')

# Losowanie elementów z listy
import random
num = random.randint(0, len(lista_zakupów) - 1) # od 0 do numeru ostatniego indexu
print(f'Losowy produkt: {lista_zakupów[num]}')

