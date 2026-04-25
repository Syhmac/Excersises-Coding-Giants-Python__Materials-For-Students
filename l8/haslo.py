HASŁO = "1234"
hasło = input("Podaj hasło: ")

while hasło != HASŁO:
	print("Złe hasło, spróbuj ponownie")
	hasło = input("Podaj hasło: ")

print("Zalogowano!")
