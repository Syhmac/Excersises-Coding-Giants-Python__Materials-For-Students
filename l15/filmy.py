class Film:
	def __init__(self, tytuł, rok):
		self.tytuł = tytuł
		self.rok = rok

	def wyświetl(self):
		print(f"{self.tytuł} ({self.rok})")

pdp = Film("Powrót do przyszłości", 1990)
mc = Film("The Minecraft Movie", 2025)
mando = Film("Mandalorianin i Grogu", 2026)
hp = Film("Harry Potter", 2001)
gig = Film("Głupi i głupszy", 2000)

hp.wyświetl()

hp.tytuł = "Harry Potter i zakon kaucyjny"

hp.wyświetl()

