import turtle as t

def p_side(length, angle):
    t.fd(length)
    t.lt(angle)
    
def move_turtle(posX,posY):
    t.penup()
    t.goto(posX,posY)
    t.pendown()

p_side(30,360/3)
p_side(30,360/3)
p_side(30,360/3)
move_turtle(150,150)

p_side(30,360/4)
p_side(30,360/4)
p_side(30,360/4)
p_side(30,360/4)
move_turtle(-150,150)
