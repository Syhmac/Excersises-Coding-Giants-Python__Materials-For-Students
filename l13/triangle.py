import turtle  as t

t.color("dark olive green")
t.fillcolor("yellow green")

t.begin_fill()
t.forward(100)
t.left(120)
t.forward(100)
t.left(120)
t.forward(100)
t.end_fill()

## Zrób drugi trójkąt w innym miejscu ekrany. Trójkąt musi być większy i obrócony o 45 stopni.

t.up()
t.goto(-200, 100)
t.right(45)
t.down()

t.begin_fill()
t.forward(200)
t.left(120)
t.forward(200)
t.left(120)
t.forward(200)
t.end_fill()

t.done()