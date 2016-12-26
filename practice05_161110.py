import turtle as t

t.penup()
t.goto(-200, 0)
t.pendown()

def polygon(length, angleNum):
    t.lt(360/angleNum)
    t.fd(length)

def translocation(length, angleNum):
    t.penup()
    t.fd(length * angleNum)
    t.pendown()
    
def polygonByFor(length, angleNum):
    for i in range(angleNum):
        polygon(length, angleNum)
    translocation(length, angleNum)
     
polygonByFor(20,3)
polygonByFor(25,4)
polygonByFor(30,5)
polygonByFor(35,6)
polygonByFor(40,8)

t.penup()
t.goto(-245, 9)
t.pendown()
t.lt(90)

