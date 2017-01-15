import getpass
import random

gawi = "가위"
bawi = "바위"
bo = "보"

GBB = [gawi, bawi, bo]

userInput = input("뭐 낼래? \n가위(0), 바위(1), 보(2): ")
userInput = int(userInput)
computer = GBB[random.randint(0,2)]

print(GBB[userInput])
print("난 " + computer+ "지롱")

#print(GBB)
#for i in GBB:
#    print(i) # not print(GBB[i])

