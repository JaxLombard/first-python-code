# ColorSpiralInput.py -
import turtle               # Set up turtle graphics
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
colors = ["red", "yellow", "blue", "green", "orange",
          "purple", "white", "gray"]


sides = int( turtle.numinput("Number of sides",
                             "How many sides do you want (1-8)?", 4, 1, 8))


for x in range(100):
    t.pencolor( colors[ x % sides] )
    t.circle(x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
     



