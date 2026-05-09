import math

def pole_kwadratu(długość: float):
	return długość * długość

def pitagoras(a: float, b: float):
	x2 = pole_kwadratu(a) + pole_kwadratu(b)
	return math.sqrt(x2)

x = pitagoras(3, 4)
print(x)