#1.12
import turtle
degree = 90

for i in range(4):
    turtle.forward(50)
    turtle.left(degree)
for i in range(4):
    turtle.backward(50)
    turtle.left(degree)

turtle.forward(50)
turtle.right(degree)
turtle.forward(50)
turtle.right(degree)
turtle.forward(100)
turtle.right(degree)
turtle.forward(100)
turtle.right(degree)
turtle.forward(50)
turtle.right(degree)
turtle.forward(50)
turtle.done()


# import turtle
# import time
# # 同时设置pencolor=color1, fillcolor=color2
# turtle.color("red", "yellow")
# turtle.begin_fill()
# for _ in range(50):
#     turtle.forward(200)
#     turtle.left(170)
#     turtle.end_fill()
# turtle.mainloop()
