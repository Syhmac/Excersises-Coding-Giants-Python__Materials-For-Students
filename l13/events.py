import turtle as t

t.setup(1080, 720)

t.up()

def after_click(x, y):
	t.goto(x, y)
	t.down()
	t.dot(15)
	t.up()

t.onscreenclick(after_click)

t.done()