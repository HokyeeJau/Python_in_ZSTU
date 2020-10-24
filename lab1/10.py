import turtle
turtle.hideturtle()
turtle.circle(100)
turtle.write("6")

turtle.penup()
turtle.goto(90,100)
turtle.write("3")
turtle.goto(-5,185)
turtle.write("12")
turtle.goto(-95,100)
turtle.write("9")
turtle.goto(-15,-15)
turtle.write("9:15:00")

turtle.goto(0,100)
turtle.pendown()
turtle.goto(0,175)
turtle.penup()

turtle.goto(0,100)
turtle.pendown()
turtle.color("red")
turtle.goto(-50,100)
turtle.penup()

turtle.width(2)
turtle.color("black")
turtle.goto(0,100)
turtle.pendown()
turtle.goto(60,100)

turtle.exitonclick()