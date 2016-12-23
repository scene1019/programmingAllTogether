from turtle import *

angleNum = input("3/4/5/6/8각형 중에 그리고 싶은 다각형의 숫자를 고르세요.  ")
angleNum = int(angleNum)

def polygon(angleNum):
    fd(100) # 다각형의 한 변의 길이는 100으로 통일 
    lt(360/angleNum)

for i in range(angleNum):
    polygon(angleNum)
