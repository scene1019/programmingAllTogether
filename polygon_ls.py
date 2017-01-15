import turtle as t

t.penup()
t.goto(-300,0)
t.pendown()

def polygon():
    t.left(360/angle)
    t.forward(size)

def translocation():
    t.penup()
    t.forward(size*angle)
    t.pendown()


size = 15
angle = 3

polygon()
polygon()
polygon()

translocation()


size = 20
angle = 4

polygon()
polygon()
polygon()
polygon()

translocation()


size = 25
angle = 5

polygon()
polygon()
polygon()
polygon()
polygon()

translocation()


size = 30
angle = 6

polygon()
polygon()
polygon()
polygon()
polygon()
polygon()

translocation()


size = 35
angle = 8

polygon()
polygon()
polygon()
polygon()
polygon()
polygon()
polygon()
polygon()

