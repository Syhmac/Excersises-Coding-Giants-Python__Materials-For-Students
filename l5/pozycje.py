import time

pozycja = 0
przesuniecia = [2, 2, 3, 5, 7, 10]
print(f'Pozycja:  {pozycja}')

for p in przesuniecia:
	time.sleep(1)
	pozycja += p
	print(f'Pozycja:  {pozycja}')