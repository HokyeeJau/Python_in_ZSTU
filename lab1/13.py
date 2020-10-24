import turtle
radius = float(input("enter the radius:"))

turtle.penup()
turtle.goto(-radius,0)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius,0)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(-radius,-radius*2)
turtle.pendown()
turtle.circle(radius)

turtle.penup()
turtle.goto(radius,-radius*2)
turtle.pendown()
turtle.circle(radius)

turtle.exitonclick()