# Stwórz prosty program który spyta się użytkownika od jakie do jakiej liczby ma wypisać zakres.
# Np. od 5 do 10. Program powinien wtedy wypisać liczby od 5 do 10 po kolei.

a = int(input("Podaj pierwszą liczbę: "))
b = int(input("Podaj drugą liczbę: "))

if b < a:
	for i in range(a, b-1, -1):
		print(i)
else:
	for i in range(a, b+1):
		print(i)