import turtle as t

def drawSide(length):
    t.fd(length)
    t.lt(90)

def drawSquare(length):
    i=0
    while i < 4:
       drawSide(length)
       i = i + 1
        
t.speed(0)

i=0
while i < 36:
    drawSquare(100)
    t.lt(10)    
    i = i + 1



    
