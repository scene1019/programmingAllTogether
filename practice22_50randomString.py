import random

fifty_string = ''

for i in range(50):
    fifty_string += chr(random.randint(97,122))


print('생성된 문자열: %s' %fifty_string)
print('이 문자열의 길이: %d' %len(fifty_string))
