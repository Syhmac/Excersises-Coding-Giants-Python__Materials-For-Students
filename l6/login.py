login = 'user'
l = input("Podaj login: ")
password = 'hasło123'
a = input("Podaj hasło: ")

if a == password and l == login:
	print("Zalogowano")
else:
	print("Login lub hasło niepoprawne")