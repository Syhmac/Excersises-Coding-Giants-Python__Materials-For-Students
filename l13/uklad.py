import turtle as t

WIDTH, HEIGHT = 800, 650
COLOR = 'gold'
ALT_COLOR = "black"
BGCOLOR = 'beige'

def prepare():
	t.setup(WIDTH, HEIGHT)
	t.color(COLOR)
	t.bgcolor(BGCOLOR)

	t.shapesize(2, 2, 2)
	t.pensize(3)
	t.speed(0)
	t.delay(0)

def draw_axes():
	t.dot(10) # środek
	
	# linia pozioma X
	t.up()
	t.goto(-300, 0)
	t.down()
	t.forward(600)
	t.stamp()

	t.home()

	# linia pionowa Y
	t.up()
	t.goto(0, -300)
	t.down()
	t.left(90)
	t.forward(600)
	t.stamp()

	t.home()

prepare()
draw_axes()

def draw_point(x, y):
	t.up()
	t.goto(x, y)
	t.down()
	t.dot(10)
	t.color(ALT_COLOR)
	t.write(f"({x:.0f}, {y:.0f})")
	t.color(COLOR)

t.onscreenclick(draw_point)

t.done()