name = "juan manuel santos"

alphabet = "abcdefghijklmnopqrstuvwxyz"
noletters = ''

for i in range(26):
	if name.count(alphabet[i]) == 0:
		noletters = noletters + alphabet[i]
print("이름: %s" %name)
print("없는 알파벳: %s" %noletters)
