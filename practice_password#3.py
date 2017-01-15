pw = "1234"

#비밀번호 오류 3회 초과 시 접속 불허
for i in range(3):
    while input("pw를 입력하세요. : ") != pw:
        break
print("패스워드 불일치로 접속이 거부되었습니다.")

#새 비밀번호로 로그인
pw = input("새 비밀번호를 입력하세요. : ")
while input("다시 한번 입력하세요. : ") == pw:
    print("비밀번호가 변경되었습니다.")
    break

while input("pw를 입력하세요. : ") != pw:
    continue

print("로그인되었습니다.")