# 과제 20. name에 없는 알파벳이 무엇인지 출력하라.

name = 'lee seul'
print("%s" %name)

# 1. name에서 모음 a, e, i, o, u가 각각 몇 개인지 출력하라.
vowel = 'aeiou'

numVowel = 0
for i in vowel:
    print("%s: %d개" %(i, name.count(str(i))))
    numVowel += name.count(str(i))

# 2. name에 모음이 모두 몇 개인지 출력하라.
print("모음은 모두 %d개" %numVowel)

# 3. name에 없는 알파벳이 무엇인지 출력하라.
noletters = ""
letters = "abcdefghijklmnopqrstuvwxyz"

for i in range(26): #test fot i in lettets:
    if name.count(letters[i]) == 0:
        noletters += letters[i]
print("없는 알파벳: %s" %noletters)