# DONE: Zaprogramuj listą zadań, która będzie zawierać czynności do wykonania (np. pranie)
# Stwórz pętle, która wyświetli każde zadanie i zapyta, czy zostało już wykonane. Wyniki umieść w osobnej liście.

zadania = ['Nakarmić kota', 'Odebrać paczkę', 'Zrobić zakupy']
status = []

for zadanie in zadania:
	odp = input(f'Czy {zadanie} zostało wykonane? ')
	status.append(odp)

print(zadania)
print(status)