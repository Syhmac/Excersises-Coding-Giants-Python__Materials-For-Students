while True:
	msg = input("Podaj wiadomość: ")

	if msg == "exit":
		break

	if msg == "skip":
		continue

	print(f"Wiadomość: {msg}")

print("Zakończono")