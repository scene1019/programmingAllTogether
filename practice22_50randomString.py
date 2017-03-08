import random
import string

'''
fifty_string = ''

for i in range(50):
    fifty_string += chr(random.randint(97,122))


print('생성된 문자열: %s' %fifty_string)
print('이 문자열의 길이: %d' %len(fifty_string))
'''


# string 모듈과 random 모듈의 choice 함수를 사용하면 더 간단하다

randomStr = string.ascii_letters
fifty_string = ''

for i in range(50):
    fifty_string += random.choice(randomStr)

print(fifty_string)
