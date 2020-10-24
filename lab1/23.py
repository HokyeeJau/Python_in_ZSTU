import turtle 
turtle.color("red", "yellow")
turtle.speed(40)
turtle.begin_fill()
for _ in range(0,36):
	turtle.forward(200)
	turtle.right(170)
turtle.end_fill()
turtle.exitonclick()