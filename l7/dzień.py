day = int(input("Podaj numer dnia: "))

days = ['pn', 'wt', 'śr', 'cz', 'pt', 'so', 'nd']

if day in range(1,8):
	print(days[day-1])

# Alternatywnie
if day == 1:
	print('pn')
elif day == 2:
	print('wt')
else:
	pass #...