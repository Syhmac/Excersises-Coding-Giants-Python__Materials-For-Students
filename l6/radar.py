v = int(input("Podaj swoją prędkość: "))

if v > 50:
	print("Jedziesz za szybko, zwolnij!")
else:
	if v < 20:
		print("Jedziesz za wolno, przyspiesz!")
	else:
		print("Jedziesz prawidłową prędkością")

