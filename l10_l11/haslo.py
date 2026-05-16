# Zmodyfikuj ten kod w taki sposób, aby wykorzystywał funkcję. Funkcja powinna przyjmować od użytkownika hasło i sprawdzić czy jest poprawne i zwrócić True/False.

def sprawdź_hasło(hasło_poprawne):
	hasło = input("Podaj hasło: ")
	return hasło == hasło_poprawne

hasło_poprawne = "jakieś_hasło_123"

while not sprawdź_hasło(hasło_poprawne):
	print("Błędne hasło, spróbuj ponownie")

print("Hasło poprawne")