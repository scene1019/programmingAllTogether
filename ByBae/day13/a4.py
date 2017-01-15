# version 1.4: 컴퓨터의 임의 선택 후 출력
import getpass
import random

gawi = "가위"
bawi = "바위"
bo = "보"
gbb = [gawi, bawi, bo]

you = gbb[int(getpass.getpass("가위: 0, 바위: 1, 보: 2\n너 뭐 할래? "))]
com = gbb[random.randint(0,2)]
print(you+"라고?")
print("난 "+com+"라네~")
