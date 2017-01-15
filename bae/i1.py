# version 1.1: 2번 메뉴 - 암호 변경, 새 암호 두 번 입력, 서로 일치하는지 확인
import getpass
thePass = "1234"
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
    yourPass = getpass.getpass("암호 알지? 입력해: ")
    if yourPass == thePass:
        print("로그인했다.")
    else:
        print("너 누구냐?")
        menu = "q"
if menu == "2":
    yourPass = getpass.getpass("원래 암호 알지? 입력해: ")
    newPass1 = getpass.getpass("새 암호 입력해: ")
    newPass2 = getpass.getpass("새 암호 다시 입력해: ")
    if newPass1 == newPass2:
        thePass = newPass1
        print("암호를 바꿨다.")
    else:
        print("암호를 못 바꿨다.")
        menu = "q"
if menu == "q":
    print("잘 가!")
