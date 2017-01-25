name = 'lee seul'
x = 'aeiou'

print("이름:", name)
for i in x:
    print("%s: %d개" %(i, name.count(str(i))))

#print("a: %d개" %name.count('a'))
#print("e: %d개" %name.count('e'))
#print("i: %d개" %name.count('i'))
#print("o: %d개" %name.count('o'))
#print("u: %d개" %name.count('u'))

numX = 0
for i in range(5):
    numX += name.count(x[i])
print("모음은 모두 %d개" %numX)


noletters = ""
letters = "abcdefghijklmnopqrstuvwxyz"

for i in range(26):
    if name.count(letters[i]) == 0:
        noletters += letters[i] # 문자열 연산

print("없는 문자는 다음과 같다. %s" %noletters)