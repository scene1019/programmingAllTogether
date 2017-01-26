name = "juan manuel santos"

print("이름:", name)
print("길이:", len(name))
print("대문자로:", name.upper())
print("마지막 글자:", name[-1])
print("마지막 글자를 이름의 길이만큼 반복하면:", name[-1] * len(name))
print("이름 세로쓰기:")
for i in range(len(name)):
	print(name[i])
