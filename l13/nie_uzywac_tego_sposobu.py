from turtle import *

def left(distance):
	up()
	pos = position()
	new_pos = (pos[0] - distance, pos[1])
	goto(pos)
	down()

forward(100)
left(100)

done()