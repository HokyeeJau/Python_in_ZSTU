import turtle
# turtle.right(75)
turtle.hideturtle()
colors=("","","","blue","black","red","yellow","","green")
turtle.penup()
turtle.goto(-150, 200)
turtle.pendown()
turtle.color("red")
turtle.write("Cool Colorful Shapes",font=("Arial",23))


for i in range(3,8):
    #60 3 45 4 36 5
    # turtle.left(15)
    turtle.penup()
    turtle.goto(-300+(i-3)*120, 0)
    turtle.pendown()
    if i == 7:
        i = i + 1
    turtle.setheading(0)
    turtle.right(180/i)
    turtle.color(colors[i],colors[i])
    turtle.begin_fill()
    turtle.circle(50, steps=i)
    turtle.end_fill()

turtle.done()