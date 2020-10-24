import turtle
turtle.hideturtle()
turtle.begin_fill()
turtle.color("red")
for i in range(6):
    turtle.forward(100)
    turtle.left(60)
turtle.end_fill()

turtle.color("white")
turtle.penup()
turtle.goto(0,60)
turtle.pendown()
turtle.write("STOP",font=("Arial",35))
turtle.done()