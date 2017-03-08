numbers = [9, 56, 75, 31, 18, 19, 3, 4, 6, 7, 8, 2, 13, 56, 79, 23, 44, 56, 67, 87, 88]
even = []
odd = []

# 홀수, 짝수 판단, 새 리스트 생성
for i in numbers:
    if (int(i) % 2) == 0:
        even.append(i)
    else:
        odd.append(i)

print("odd numbers: ", odd)
print("even numbers: ", even)


'''
num = '123456789'

odd = ''
even = ''

for i in num:
    if (int(i) % 2) == 0:
        even = even + i
    else:
        odd = odd + i

print(even)
print(odd)
'''

