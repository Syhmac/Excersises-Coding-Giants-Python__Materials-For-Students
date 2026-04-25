import random, time

META = 20
pozycja = 0
tura = 0

print("Wyścig do mety!")
print(f"Musisz dojść do pozycji numer {META}")

while pozycja < META:
	input("Naciśnij ENTER, aby rzucić kostką...")

	krok = random.randint(1, 6)
	pozycja += krok
	tura += 1

	print(f"🎲 Wyrzuciłeś: {krok}")
	print(f"📍 Twoja pozycja: {pozycja}/{META}")
	print()

print(f"Gratulacje, Dotarłeś do mety w {tura} turach.")