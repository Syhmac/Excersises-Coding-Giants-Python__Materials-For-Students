import random

czas = random.randint(0, 10)
życie = random.randint(-15, 15)

print(f"Czas {czas}")
print(f"Życie: {życie}")

if czas < 1 or życie < 1:
	print("Game over")
else:
	print('Gra się toczy dalej')