o_string = "aBCdeFgHiJkLmnOpqRsTuVwXyZ"
upper = ''
lower = ''

# 원래 문자열 출력
print(o_string)

for i in o_string:
    if 65 <= ord(i) <= 90:
        upper += i
    if 97 <= ord(i) <= 122:
        lower += i
        
print("대문자 문자열: %s" %upper)
print("소문자 문자열: %s" %lower)
