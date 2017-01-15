# practice16
# 한 번 게임 진행 후 종료하기
# 항상 컴퓨터가 이기기
# 사용자의 선택 가리기
import getpass
import random

gawi = "가위"
bawi = "바위"
bo = "보"

GBB = [gawi, bawi, bo]

userInput = getpass.getpass("뭐 낼래? \n가위(0), 바위(1), 보(2): ")
userInput = int(userInput)

while (userInput != 0) and (userInput != 1) and (userInput != 2):
    userInput = getpass.getpass("아니, 셋 중에 하나를 골라! \n가위(0), 바위(1), 보(2): ")
    userInput = int(userInput)

comInput = userInput - 2

print("넌 '" + GBB[userInput] + "'를 냈구나?")
print("난 '" + GBB[comInput] + "'야~ 내가 이겼다!")


