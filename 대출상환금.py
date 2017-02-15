#대출 상환금 계산
#
#대출금에 대해서 얼마나 갚아나가야 하는지 계산해주는 프로그램
#
#작성자 : 오아리
#작성일자 : 2011.9.11

#사용자 입력받음
print("대출 상환금 계산 서비스에 오신걸 환영합니다.")

principal=int(input("대출 원금을 입력해주세요. (백만원 이상만 계산해 드립니다..)\n"))
assert principal>=1000000
years=int(input("상환 기간(연 단위)을 입력해주세요.\n"))
assert 1<=years
rate=float(input("이자율을 백분률*(%)로 입력해주세요.\n"))
assert 0<=rate<=100

#상환금 계산
yearmoney=int(((1+rate/100)**years) * principal * rate/100/(((1+rate/100)**years)-1))
monthmoney=int(yearmoney/12)
totalmoney=int(yearmoney*years)

#출력
print("잘 입력하셨습니다. 원하시는 내용은 다음과 같습니다.")
print(principal,"원을",years,"년 동안 연 이자율",rate,"%로 빌리신다고 하셨습니다.")

print("계산 결과를 보여드리겠습니다.")
print("1년에 한번씩 상환하신다면 매년 약",yearmoney,"원 씩 지불하셔야 합니다.")
print("1달에 한번씩 상환하신다면 매년 약",monthmoney,"원 씩 지불하셔야 합니다.")
print("상환 완료시까지 총 상환금액은 약",totalmoney,"원 입니다.")
print("저희 서비스를 이용해주셔서 감사합니다.\n 또 들러주세요.")
