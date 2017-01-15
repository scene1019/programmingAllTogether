import turtle as t

t.penup()
t.goto(-300,0)
t.pendown()

def polygon(size, angle):
    t.lt(360/angle)
    t.fd(size)

def translocation(size,angle):
    t.penup()
    t.fd(size*angle)
    t.pendown()

# draw a triangle
for i in range(3):
    polygon(15,3)
translocation(15,3)

for i in range(4):
    polygon(20,4)
translocation(20,4)

for i in range(5):
    polygon(25,5)
translocation(25,5)

for i in range(6):
    polygon(30,6)
translocation(30,6)

for i in range(8):
    polygon(35,8)
translocation(35,8)
