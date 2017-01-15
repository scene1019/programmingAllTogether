# version 1.3: 깔끔하게
# thePass = "1234"
choice = input("뭐 할래?\n로그인(1), 암호 변경(2), 종료(q): ")
menu = choice.lower()

while (menu != "1") and (menu != "2") and (menu != "q"):
    choice = input("다시 골라라!\n로그인(1), 암호 변경(2), 종료(q): ")
    menu = choice.lower()

if menu == "1":
    print("로그인했다.")
if menu == "2":
    print("암호를 바꿨다.")
if menu == "q":
    print("잘 가!")
