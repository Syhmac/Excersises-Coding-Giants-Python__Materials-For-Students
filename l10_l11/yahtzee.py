import random
kości = [0, 0, 0, 0, 0]

def rzut_kośćmi(numery_kości: str = "12345") -> None:
	# np. rzut_kośćmi("245")
	for i in numery_kości:
		index = int(i) - 1
		kości[index] = random.randint(1, 6)

def pokaż_kości() -> None:
	print("_______________________________________________")
	print("Indeksy:\t", end="")
	for i in range(len(kości) - 1):
		print(f"{i+1} | ", end="")
	print("5")
	print("Kości:\t\t", end="")
	for i in range(len(kości) - 1):
		print(f"{kości[i]} | ", end="")
	print(kości[4])
	print("________________________________________________")

def czy_przerzut() -> bool:
	odp = input("Czu chcesz przerzucić kośćmi: [t/n]")
	if odp == "t" or odp == "T":
		return True
	return False



rzut_kośćmi()
pokaż_kości()