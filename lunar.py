import turtle							#imports turtle
t = turtle.Pen()                                          #sets t as turtle.Pen()
t.pencolor("white")
turtle.bgcolor("black")
t.fillcolor("white")
t.begin_fill()
t.circle(200)
t.end_fill()
t.pencolor("black")
t.forward(400)
t.fillcolor("black")
t.begin_fill()
t.circle(200)
t.speed(10)
t.end_fill()
for x in range(400):
	t.backward(400/14)
	t.fillcolor("black")
	t.begin_fill()
	t.circle(200)
	t.end_fill()

t.fillcolor("white")
t.begin_fill()
t.circle(200)
t.end_fill()
t.clear()
turtle.bgcolor("black")

for x in range(400):
	t.fillcolor("white")
	t.begin_fill()
	t.circle(200)
	t.end_fill()
	t.backward(1)
	t.fillcolor("black")
	t.begin_fill()
	t.circle(200)
	t.end_fill()
