import random

MIN = 1
MAX = 50

sekret = random.randint(MIN, MAX+1)
próby = 0
strzał = None

while strzał != sekret:
	strzał = int(input("Podaj liczbę: "))
	próby +=1
	if strzał < sekret:
		print("Musisz strzelać wyżej")
	elif strzał > sekret:
		print("Musisz strzelać niżej")
	elif strzał == sekret:
		print(f"Odgadłeś liczbę w {próby} próbach")
	else:
		print(f"To nie jest liczba z zakresu {MIN} - {MAX}")
