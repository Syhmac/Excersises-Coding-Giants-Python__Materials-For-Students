koszty = [193, 824, 12, 483, 15]

# Minimum, maksimum i suma
print(f'Minimum: {min(koszty)}')
print(f'Maksimum: {max(koszty)}')

# suma = koszty[0] + koszty[1] + koszty[2] + koszty[3] + koszty[4]

print(f'Suma: {sum(koszty)}')

for k in koszty:
	print(k)

# DONE: Policzyć sumę elementów w tablicy koszty bez użycia funkcji sum(), wykorzystaj pętle for

# TODO: Zmodyfikuj ten kod tak, aby przy każdej iteracji (wykonaniu pętli) wypisywała się aktualna suma częściowa

suma = 0
for k in koszty:
	print('Suma częściowa: ', suma)
	suma += k
print(f"Suma: {suma}")