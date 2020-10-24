from turtle import *
color("red")
fillcolor("yellow")
begin_fill()
while True:
    fd(200)
    right(144)
    if abs(pos()) < 1:
        break
end_fill()
pu()
fd(76.9)
pd()
fillcolor("yellow")
begin_fill()
for i in range(5):
    fd(46.2)
    right(72)
end_fill()
exitonclick()