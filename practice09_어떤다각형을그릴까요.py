from turtle import *

angleNum = input("어떤 다각형을 그릴까요?  ")
#input은 str만 리턴해줌.
angleNum = int(angleNum) #이 angleNum은 전역 변수, 아래의 angleNum과 다름


def polygon(angleNum): #이 angleNum은 함수 안에서 사용하는 지역변수(인수)
    fd(100) # 다각형의 한 변의 길이는 100으로 통일
    lt(360/angleNum)

for i in range(angleNum):
    polygon(angleNum)
