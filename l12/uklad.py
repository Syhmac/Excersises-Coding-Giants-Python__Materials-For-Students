import turtle as t
import time

t.color('white') # Kolor pisaka
t.bgcolor('medium purple') # Kolor tła
t.shape("classic") # Wygląd pisaka
t.speed(100) # Szybkość
t.pensize(5) # Grubość lini

t.forward(200)
t.left(90)
t.forward(200)
t.left(90)
t.forward(400) # 400
t.left(90)
t.forward(200)
t.left(90)
t.forward(200)

t.forward(200)
t.right(90)
t.forward(200)
t.right(90)
t.forward(400) # 400
t.right(90)
t.forward(200)
t.right(90)
t.forward(200)

t.right(90)
t.forward(200)
t.right(180)
t.forward(400)

t.color("red")
t.pensize(7)

t.up()
t.goto(100,100)
t.dot(10)
t.forward(20)
t.left(90)
t.fd(30)
t.right(90)
t.write("(+x , +y)", font=("Arial", 22, "bold"))

t.goto(100,-100)
t.dot(10)
t.forward(20)
t.left(90)
t.fd(30)
t.right(90)
t.write("(+x , -y)", font=("Arial", 22, "bold"))


t.goto(-100,-100)
t.dot(10)
t.forward(20)
t.left(90)
t.fd(30)
t.right(90)
t.write("(-x , -y)", font=("Arial", 22, "bold"))

t.goto(-100,100)
t.dot(10)
t.forward(20)
t.left(90)
t.fd(30)
t.right(90)
t.write("(-x , +y)", font=("Arial", 22, "bold"))

t.goto(0,0)

t.exitonclick()