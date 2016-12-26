from turtle import *

def drawSide(length, angleNum):
    angleNum = angleNum + 3
    fd(length)
    lt(360/angleNum)

angleNum = int(input("어떤 다각형을 그릴까요?  "))

for i in range(angleNum):
    drawSide(100, angleNum)
print("메인의 angleNum:", angleNum)
