# stworzyć listę w której będzie 4 - 5 kolorów
# Wyświetlić zawartość listy razem z indeksami
# Wyświetlić ile kolorów jest w liście
# Unikamy "Magic Numbers"

colors = ['yellow', 'blue', 'green', 'white']

# print('Lista kolorów: ', colors)
# print(f'0: {colors[0]}')
# print(f'1: {colors[1]}')
# print(f'2: {colors[2]}')
# print(f'3: {colors[3]}')

print(*range(5)) # Od 0 - 4
print(*range(10, 20)) # Od 10 - 19
print(*range(10, 20, 2)) # Co druga liczba w zakresie od 10 do 19
print(*range(5, 25, 5))
print(*range(5, 0, -1)) # Liczenie w tył

for i in range(0, len(colors)):
	print(colors[i])

# for color in colors:
# 	print(color)

# print(f'Długość listy: {len(colors)}')