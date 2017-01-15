import turtle as t

t.penup()
t.goto(-300,0)
t.pendown()

def polygon(size, angle):
    t.left(360/angle)
    t.forward(size)

def translocation(size,angle):
    t.penup()
    t.forward(size*angle)
    t.pendown()

# 삼각형을 만들고 자리를 옮겨요.
polygon(15,3)
polygon(15,3)
polygon(15,3)
translocation(15,3)

polygon(20,4)
polygon(20,4)
polygon(20,4)
polygon(20,4)
translocation(20,4)

polygon(25,5)
polygon(25,5)
polygon(25,5)
polygon(25,5)
polygon(25,5)
translocation(25,5)

polygon(30,6)
polygon(30,6)
polygon(30,6)
polygon(30,6)
polygon(30,6)
polygon(30,6)
translocation(30,6)

polygon(35,8)
polygon(35,8)
polygon(35,8)
polygon(35,8)
polygon(35,8)
polygon(35,8)
polygon(35,8)
polygon(35,8)
