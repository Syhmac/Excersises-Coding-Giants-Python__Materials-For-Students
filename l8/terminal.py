# Stworzyć prosty terminal z kilkoma komendami
# help - wyświetla dostępne komendy
# info - wyświetla wersję terminala
# exit - wyłączy program

print("Terminal - wpisz exit, aby zakończyć")
komenda = ""

while komenda != "exit":
	komenda = input("> ")
	if komenda == "help":
		print("Dostępne komendy: help, info, exit")
	elif komenda == "info":
		print("Wersja 1.0")
	elif komenda == "exit":
		print("Wyłączanie")
	else:
		print(f"Nieznana komenda: {komenda}")