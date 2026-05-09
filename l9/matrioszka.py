def matrioszka(rozmiar: int):
	if rozmiar <= 1: 
		return "matrioszka"
	
	return "M" + matrioszka(rozmiar-1)

print(matrioszka(3))

f = matrioszka
print(f(5))