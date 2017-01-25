# 과제 19. name의 글자들을 한 줄에 하나씩 출력하라. (코드 말고 캡처화면 제출)

# 1. 문자열 변수 name을 정의하고 자신의 영문 이름으로 초기화하라.
name = 'lee seul'

# 2. name을 출력하라.
print("이름:", name)

# 3. name의 길이를 구하고 화면에 출력하라.
print("길이:", len(name))

# 4. name을 전부 대문자로 변환하여 출력하라.
print("대문자로:", name.upper())

# 5. name에서 마지막 글자만 출력하라.
print("마지막 글자:", name[-1])

# 6. name의 마지막 글자를 name의 길이만큼 반복 출력하라.
print("마지막 글자를 이름의 길이만큼 반복하면:", name[-1] * len(name))

# 7. name의 글자들을 한 줄에 하나씩 출력하라.
for i in name:
    print(i)