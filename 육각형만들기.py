import turtle as t

size=100
angle=6

def multisqure():
    t.right(360/angle)
    t.forward(size)

multisqure()
multisqure()
multisqure()
multisqure()
multisqure()
multisqure()

t.penup()
t.goto(0,100)
t.pendown()

size=50
angle=3

multisqure()
multisqure()
multisqure()

t.penup()
t.goto(0,200)
t.pendown()

size=40
angle=4

multisqure()
multisqure()
multisqure()
multisqure()

t.penup()
t.goto(200,200)
t.pendown()

size=20
angle=5

multisqure()
multisqure()
multisqure()
multisqure()
multisqure()

t.penup()
t.goto(200,0)
t.pendown()

size=55
angle=8

multisqure()
multisqure()
multisqure()
multisqure()
multisqure()
multisqure()
multisqure()
multisqure()
