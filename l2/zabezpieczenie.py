num = input('Podaj liczbę: ')
try: # Co próbujemy zrobić
	num =int(num)
	print('Super, udało się')
except Exception as e: # Co zrobić, jeśli doszło do błędu
	print('Doszło do błędu')
	print(e) # Opcjonalne, tylko jeśli mamy "Exception as e"