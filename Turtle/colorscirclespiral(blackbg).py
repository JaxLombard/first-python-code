# ColorSquareSpiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
sides = 6
colors = ["red", "yellow", "blue", "green","purple","orange"]
for x in range(100):
    t.pencolor( colors[ x % sides ] )
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x*sides/100)
 
