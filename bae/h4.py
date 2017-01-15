# version 1.4: 오류 횟수 5회까지 허용
# thePass = "1234"
errorCount = 0
choice = input("뭐 할래?\n로그인(1), 암호 변경(2), 종료(q): ")
menu = choice.lower()

while (menu != "1") and (menu != "2") and (menu != "q"):
    errorCount += 1
    if errorCount < 5:
        choice = input("다시 골라라!\n로그인(1), 암호 변경(2), 종료(q): ")
        menu = choice.lower()
    else:
        menu = "q"

if menu == "1":
    print("로그인했다.")
if menu == "2":
    print("암호를 바꿨다.")
if menu == "q":
    print("잘 가!")
