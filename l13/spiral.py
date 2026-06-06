import turtle as t

t.speed(0)
t.bgcolor('black')
t.pensize(2)

colors = ["#003bae", "#a14493", "#cb066c"]

for i in range(360):
	t.color(colors[(i//len(colors))%3])
	t.circle(i)
	t.left(5)

t.done()