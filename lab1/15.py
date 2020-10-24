import turtle
x , y = map(int,input("Enter the center of the rectangle with a space inside: ").split(' '))
length = int(input("Length: "))
width = int(input("Width: "))

turtle.penup()
turtle.goto(x-length/2,y-width/2)
turtle.pendown()

turtle.hideturtle()
turtle.forward(length)
turtle.left(90)
turtle.forward(width)
turtle.left(90)
turtle.forward(length)
turtle.left(90)
turtle.forward(width)

turtle.exitonclick()
