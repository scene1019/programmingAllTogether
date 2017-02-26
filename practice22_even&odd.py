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


