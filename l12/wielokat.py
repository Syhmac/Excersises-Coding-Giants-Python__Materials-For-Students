import turtle as t

boki = int(t.numinput("Info", "Podaj ilość boków: "))
if boki < 3:
	exit(-1)

kat = 360 / boki
bok = 2

for i in range(boki):
	t.fd(bok)
	t.left(kat)

t.exitonclick()