plecak = []

# nowy = input('Dodaj przedmiot: ')
# plecak.append(nowy)
# print(plecak)

plecak.append('Bomba') # 0
plecak.append('Komputer') # 1
plecak.append('Pałac młodzieży') # 2
plecak.append('Reaktor RBMK numer 4 z Czarnobyla') # 3

num = int(input('Podaj index przedmioty do wymiany: '))
nowy = input('Nowy przedmiot do wymiany: ')

plecak.pop(num) # Sposób 1
plecak.insert(num, nowy)

# plecak[num] = nowy # Sposób 2

print(plecak)

print(f'W plecaku znajduje się {len(plecak)} przedmiotów')