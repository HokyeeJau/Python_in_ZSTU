import turtle
turtle.hideturtle()
turtle.forward(100)
turtle.goto(75,-25)
turtle.backward(100)
turtle.goto(0,0)

turtle.goto(0,-50)
turtle.forward(100)
turtle.goto(75,-75)
turtle.backward(100)
turtle.goto(0,-50)

turtle.penup()
turtle.goto(-25,-25)
turtle.pendown()
turtle.goto(-25,-75)

turtle.penup()
turtle.goto(100,0)
turtle.pendown()
turtle.goto(100,-50)

turtle.penup()
turtle.goto(75,-25)
turtle.pendown()
turtle.goto(75,-75)

turtle.exitonclick()