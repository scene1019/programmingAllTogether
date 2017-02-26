# 가위바위보 승패 출력하기
import getpass
import random

gawi = "가위"
bawi = "바위"
bo = "보"

GBB = [gawi, bawi, bo]

userInput = input("뭐 낼래? \n가위(0), 바위(1), 보(2): ")
userInput = int(userInput)

while (userInput != 0) and (userInput != 1) and (userInput != 2):
    userInput = input("아니, 셋 중에 하나를 골라! \n가위(0), 바위(1), 보(2): ")
    userInput = int(userInput)

comInput = int(random.randint(0,2))

print("사용자: %s\n컴퓨터: %s\n" %(GBB[userInput], GBB[comInput]))

if userInput == 0:
    if comInput == 2:
        print("사용자가 이겼습니다.")
    if comInput == 1:
        print("사용자가 졌습니다.")
    if comInput == userInput:
        print("비겼습니다.")

if userInput == 1:
    if comInput == 0:
        print("사용자가 이겼습니다.")
    if comInput == 2:
            print("사용자가 졌습니다.")
    if comInput == userInput:
            print("비겼습니다.")

if userInput == 2:
    if comInput == 1:
        print("사용자가 이겼습니다.")
    if comInput == 0:
            print("사용자가 졌습니다.")
    if comInput == userInput:
            print("비겼습니다.")
