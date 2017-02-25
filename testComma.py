won = '7654321'
comma = ','
new = ''

for i in range(len(won)):
    i += 1
    minusIndex = i * -1
    if (i == (len(won))) or (minusIndex % 3 != 0):
        new = won[-i] + new
        print(new)
    else:
        new = comma + won[-i] + new
print(new)
