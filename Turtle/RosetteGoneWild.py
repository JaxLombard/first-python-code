import turtle
turtle.bgcolor('black')
t = turtle.Pen()
t.speed(0)
# The User's Input
numberofcircles = int(turtle.numinput("Number of circles",
                                     "How many circles in your rosette?", 6))
# The Loop
for x in range(numberofcircles) :
    t.pencolor('red')
    t.circle(100)
    t.pencolor('yellow')
    t.circle(50)
    t.left(360/numberofcircles)
