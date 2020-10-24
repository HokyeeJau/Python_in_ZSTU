import turtle
turtle.pensize(25)
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.right(45)
n=0
while n<9:
    turtle.forward(7)
    turtle.left(10)
    n+=1

color_set = ['grey', 'green', 'yellow', 'pink', 'purple', 'green']
for i in color_set:
	n = 0
	turtle.color(i)
	while n < 9:
		turtle.forward(7)
		turtle.right(10)
		n += 1
	n = 0
	while n < 9:
		turtle.forward(7)
		turtle.left(10)
		n+=1