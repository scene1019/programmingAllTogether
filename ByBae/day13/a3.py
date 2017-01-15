# version 1.3: 사용자의 선택 가리기
import getpass

gawi = "가위"
bawi = "바위"
bo = "보"
gbb = [gawi, bawi, bo]

you = gbb[int(getpass.getpass("가위: 0, 바위: 1, 보: 2\n너 뭐 할래? "))]
print(you+"라고?")
