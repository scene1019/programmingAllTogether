import getpass

thePass = "1234"
choice = input("뭐 할래? \n로그인(1), 암호 변경(2), 종료(q): ")
#choice = choice.lower()

errorCount = 0
while (choice != "1") and (choice != "2") and (choice != "q"):
    errorCount += 1
    if errorCount < 5:
        choice = input("다시 눌러주세요. \n로그인(1), 암호 변경(2), 종료(q): ")
    else:
        print("너무 많이 틀렸어, 종료할거야.")
        choice = "q"
        #break

if choice == "1":
    yourpass = getpass.getpass("암호를 입력하세요.: ")
    if yourPass == thePass:
        print("로그인되었습니다.")
    else:
        print("틀렸어. 넌 누구니?")

if choice == "2":
    print("변경할 암호를 입력하세요.")
if choice.lower() == "q":
    print("종료합니다.")
