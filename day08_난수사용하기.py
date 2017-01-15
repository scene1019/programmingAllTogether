import turtle as t
import random

def setTurtlePos(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

#setTurtlePos(-100,-100)
#t.circle(100, 180) #extent
#t.circle(100, steps=10)

t.speed(0)
#rad = random.randint(10, 50)
for i in range(20):
    x= random.randint(-100, 100)
    y= random.randint(-100, 100)
    rad = random.randint(10, 50)
    setTurtlePos(x, y)
    t.circle(rad)

