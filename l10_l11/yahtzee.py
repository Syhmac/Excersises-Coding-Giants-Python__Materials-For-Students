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
	odp = input("Czy chcesz przerzucić kośćmi: [t/n]")
	if odp == "t" or odp == "T":
		return True
	return False

nazwy_punktów = ["Jedynki", "Dwójki", "Trójki", "Czwórki", "Piątki", "Szóstki", "Full"]
punkty = [""] * len(nazwy_punktów)
# ["", "", "", "", "", ""]

def pokaż_tabelę():
	print("__________________")
	for i in range(len(punkty)):
		print(f"{i+1}.{nazwy_punktów[i]}\t{punkty[i]}")
		# 1.Jedynki    0
	print("__________________")

def wstaw_punkty():
	pole = int(input("Gdzie chcesz wstawić punkty? Podaj numer kategorii: "))
	if punkty[pole-1] == "":
		if 1 <= pole <= 6:
			wstaw_liczbowe(pole)
		if pole == 7:
			wstaw_full(pole)
	else:
		print("To pole jest już zajete")
		wstaw_punkty()

def wstaw_liczbowe(liczba: int) -> None:
	liczba_punktów = 0
	for kość in kości:
		if kość == liczba:
			liczba_punktów += kość
	punkty[liczba-1] = liczba_punktów

def wstaw_full(pole: int) -> None:
	liczba_wystąpień = [0, 0, 0, 0, 0, 0]
	for kość in kości:
		liczba_wystąpień[kość-1] += 1
	if 3 in liczba_wystąpień and 2 in liczba_wystąpień:
		punkty[pole-1] = 25
	else:
		punkty[pole-1] = 0

if __name__ == "__main__":
	for tura in range(len(punkty)):
		rzut_kośćmi()
		pokaż_tabelę()
		pokaż_kości()

		for i in range(2):
			przerzut = czy_przerzut()
			if przerzut:
				kości_do_przerzutu = input("Wpisz numery kości do przerzucenia (bez spacji): ")
				rzut_kośćmi(kości_do_przerzutu)
				pokaż_kości()
			else:
				break

		pokaż_tabelę()
		wstaw_punkty()
		pokaż_tabelę()

	print(f"Twój wynik to: {sum(punkty)}")
