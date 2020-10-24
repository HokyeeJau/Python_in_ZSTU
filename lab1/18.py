import turtle
radius = int(input("Enter the radius of the circles:"))
turtle.hideturtle()

colors=("blue","black","red","yellow","green")
for i in range(5):
    turtle.penup()
    coordA=(-2.2*radius,0,2.2*radius,-1.1*radius,1.1*radius)#各圆绘制起点坐标x值, radius为半径
    coordB=(0,0,0,-1.1*radius,-1.1*radius)                  #各圆绘制起点坐标y值, radius为半径
    turtle.goto(coordA[i],coordB[i])
    turtle.pendown()
    turtle.pencolor(colors[i])
    turtle.circle(radius)
turtle.done()
