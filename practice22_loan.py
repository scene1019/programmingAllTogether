# 대출 상환금 계산 프로그램, 원작성자: 오아리
# 리팩토링: 이슬
#import locale
#locale.setlocale(locale.LC_ALL, '')

print("대출 상환금 계산을 시작합니다. 상환 방식은 '원리금 균등' 방식입니다.")

loanAmount = int(input("\n대출 금액을 '만 원 단위'로 입력하세요. (100만 원 이상)\n대출 금액: "))
loanAmount = loanAmount * 10000
#assert principal>=1000000 # assert 다음 구문이 옳을 때만 다음 행이 실행됨. 옳지 않으면 오류를 출력하며 종료됨.

loanYears = int(input("대출 기간을 '연 단위'로 입력하세요. \n대출 기간: "))
loanMonth = loanYears * 12
#assert 1<=years

interestYear = float(input("연이율을 입력하세요.\n연이율: "))
interestMonth = (interestYear / 12) * 0.01
#assert 0<=rate<=100

# 대출 상환금 계산
calcFactor = (1 + interestMonth) ** loanMonth
paymentMonth = (loanAmount * interestMonth * calcFactor) / (calcFactor - 1)
paymentMonth = int(paymentMonth)
#paymentMonth = int(locale.format('%f', paymentMonth, 1))

# 쉼표 넣기
strLoanAmount = str(loanAmount)
comma = ','
commaLoanAmount = ''

# 수치를 문자열로 바꾸고 1의 자리부터 연산하되 3의 배수 자릿수에서는 쉼표를 더한다.
for i in range(len(strLoanAmount)):
    i += 1
    minusIndex = i * -1
    if (i == (len(strLoanAmount))) or (minusIndex % 3 != 0): # 마지막 자리와 3의 배수 자릿수는 쉼표 없이 더하고
        commaLoanAmount = strLoanAmount[-i] + commaLoanAmount # 연산 순서 유의
    else:
        commaLoanAmount = comma + strLoanAmount[-i] + commaLoanAmount # 3의 배수 자릿수는 쉼표를 더한 다음 숫자를 더한다.

strPaymentMonth = str(paymentMonth)
commaPaymentMonth = ''

for j in range(len(strPaymentMonth)):
    j += 1
    minusIndex = j * -1
    if (j == (len(strPaymentMonth))) or (minusIndex % 3 != 0):
        commaPaymentMonth = strPaymentMonth[-j] + commaPaymentMonth
    else:
        commaPaymentMonth = comma + strPaymentMonth[-j] + commaPaymentMonth


# 계산 결과
print("\n입력하신 내용은 다음과 같습니다. \n 대출 금액: %s원\n 대출 기간: %s년\n 연이율:   %.2f%%" %(commaLoanAmount, loanYears, interestYear))
print("\n계산 결과는 다음과 같습니다.")
print("월 상환금: %s원" %commaPaymentMonth)

