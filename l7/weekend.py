# Zapytać użytkownika jaki jest dzień tygodnia (numer)
# Sprawdzić na podstawie numeru czu jest weekend i wyświetlić odpowiednią informację.

a = input("Jaki jest dzień tygodnia? Wpisz liczbę od 1 do 7: ")

if a == "6" or a == "7":
	print('Ten dzień to weekend')
elif int(a) not in range(1,8):
	print("To nie jest prawidłowy numer dnia!")
else:
	print("Ten dzień to nie weekend")