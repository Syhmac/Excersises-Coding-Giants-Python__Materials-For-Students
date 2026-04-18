tekst = 'Hello worLd'

count = 0
for letter in tekst:
	if letter.lower() == 'l': # Konwersja na małą literę .lower()
		count+=1

print(count)

tekst = tekst.upper()
print(tekst)