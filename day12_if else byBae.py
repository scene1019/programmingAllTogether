thePass = "1234"
newPass = input("암호: ")

wrongNum = 0
while thePass != newPass:
    print("어쭈?")
    newPass = input("암호: ")
    wrongNum = wrongNum + 1
    if wrongNum < 5:
        print("너무 많이 틀렸어, 그만 눌러!")
    else:
        break
if thePass == newPass:
    print("반가워요!")
else:
    print("꺼져!")


