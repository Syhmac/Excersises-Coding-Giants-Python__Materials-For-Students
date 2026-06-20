class Dzień:
	def __init__(self, numer):
		self.numer = numer

	def następny(self):
		if self.numer > 6:
			self.numer = 1
		else:
			self.numer += 1

	def wyświetl(self):
		match self.numer:
			case 1:
				print("Poniedziałek")
			case 2:
				print("Wtorek")
			case 3:
				print("Środa")
			case 4:
				print("Czwartek")
			case 5:
				print("Piątek")
			case 6:
				print("Sobota")
			case 7:
				print("Niedziela")
			case _:
				print("Nieprawidłowy numer dnia")

dzień = Dzień(7)
print(dzień.numer)
dzień.wyświetl()
dzień.następny()
print(dzień.numer)
dzień.wyświetl()
