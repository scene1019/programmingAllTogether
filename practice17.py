# practice17. 1번 메뉴 기능 확장
# 로그인 기회를 5번까지 부여
# 5회 오류 시 강제 종료

import getpass

thePass = "1234"
choice = input("메뉴를 고르세요. \n로그인(1), 암호 변경(2), 종료(q): ")
choice = choice.lower()

# 메뉴 선택 5번 오류 시 강제 종료
choiceErrorCount = 0
while (choice != "1") and (choice != "2") and (choice != "q"):
    choiceErrorCount += 1
    if choiceErrorCount < 5:
        choice = input("다시 눌러주세요. \n로그인(1), 암호 변경(2), 종료(q): ")
    else:
        print("너무 많이 틀렸습니다.")
        choice = "q"

# 로그인(1) 메뉴
pwErrorCount = 0
if choice == "1":
    yourPass = getpass.getpass("암호를 입력하세요. \n비밀번호: ")
    while yourPass != thePass:
        pwErrorCount += 1
        if pwErrorCount < 5:
            yourPass = getpass.getpass("올바른 비밀번호를 눌러주세요. \n비밀번호: ")
        else:
            print("너무 많이 틀렸습니다.")
            break
    if yourPass == thePass:
        print("로그인되었습니다.")
    else:
        print("종료하겠습니다.")


# 암호 변경(2) 메뉴
if choice == "2":
    print("변경할 암호를 입력하세요.")

# 종료(q) 메뉴
if choice.lower() == "q":
    print("종료합니다.")
