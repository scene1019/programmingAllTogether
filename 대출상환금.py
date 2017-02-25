# 대출 상환금 계산 프로그램, 원작성자: 오아리
# 리팩토링: 이슬

print("대출 상환금 계산을 시작합니다. 상환 방식은 '원리금 균등' 방식입니다.")

loanAmount = int(input("\n대출 금액을 '만 원 단위'로 입력하세요. (100만 원 이상)\n대출 금액: "))
loanAmount = loanAmount * 10000
#assert principal>=1000000

loanYears = int(input("대출 기간을 '연 단위'로 입력하세요. \n대출 기간: "))
loanMonth = loanYears * 12
#assert 1<=years

interestYear = float(input("연이율을 입력하세요.\n연이율: "))
interestMonth = (interestYear / 12) * 0.01
#assert 0<=rate<=100

# 대출 상환금 계산
calcFactor = (1 + interestMonth) ** loanMonth
paymentMonth = (loanAmount * interestMonth * calcFactor) / (calcFactor - 1)


# 계산 결과
print("\n입력하신 내용은 다음과 같습니다. \n 대출 금액: %s원\n 대출 기간: %s년\n 연이율:   %.2f%%" %(loanAmount, loanYears, interestYear))
#print(principal,"원을",years,"년 동안 연 이자율",rate,"%로 빌리신다고 하셨습니다.")

print("\n계산 결과는 다음과 같습니다.")
print("월 상환금: %d원" %paymentMonth)

