PIN = "1234"
ROK = "2004"
HASŁO = "tajne"

while True:
	input_pin = input("PIN: ")
	input_rok = input("Rok urodzenia: ")
	input_hasło = input("Hasło: ")

	if input_pin == PIN and input_rok == ROK and input_hasło == HASŁO:
		break

print("Zalogowano")