# version 1.1: q/Q 입력 처리
# thePass = "1234"
choice = input("뭐 할래?\n로그인(1), 암호 변경(2), 종료(q): ")
if choice == "1":
    print("로그인했다.")
if choice == "2":
    print("암호를 바꿨다.")
if choice.lower() == "q":
    print("잘 가!")
