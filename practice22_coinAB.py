# 동전 던지기 확률 확인

import random

front = '앞면'
back = '뒷면'

coin = [front, back]

n = 10000
p = 0

for i in range(n):
    if coin[random.randint(0,1)] == front:
        p += 1

frontP = p / n
backP = (n - p) / n

print("동전은 %s번 던질 때 동전 앞면과 뒷면이 나올 확률은 다음과 같습니다." %n)
print("앞면: %s, 뒷면: %s" %(frontP, backP))


