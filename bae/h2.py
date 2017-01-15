# version 1.2: 1 / 2 / q(Q) 이외의 메뉴 입력 시 다시 입력 요구
# thePass = "1234"
choice = input("뭐 할래?\n로그인(1), 암호 변경(2), 종료(q): ")

while (choice.lower() != "1") and (choice.lower() != "2") and (choice.lower() != "q"):
    choice = input("다시 골라라!\n로그인(1), 암호 변경(2), 종료(q): ")

if choice.lower() == "1":
    print("로그인했다.")
if choice.lower() == "2":
    print("암호를 바꿨다.")
if choice.lower() == "q":
    print("잘 가!")
