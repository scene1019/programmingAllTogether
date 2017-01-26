name = "juan manuel santos"

print("이름: %s" %name)
print("a: %d개" %name.count('a'))
print("e: %d개" %name.count('e'))
print("i: %d개" %name.count('i'))
print("o: %d개" %name.count('o'))
print("u: %d개" %name.count('u'))

vowels = ''

vowels = vowels + "aeiou"
numVowels = 0

for i in range(5):
	numVowels += name.count(vowels[i])
print("모음은 모두: %d개" %numVowels)
