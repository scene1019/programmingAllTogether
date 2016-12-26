import turtle as t

t.speed(0)
t.color("red", "blue")

t.penup()
t.goto(-100,0)
t.pendown()

def drawStar():
    t.fd(200)
    t.rt(144)

t.begin_fill()
for i in range(5):
    drawStar()
t.end_fill()

