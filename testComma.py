won1 = '7654321'
won2 = '9876'
comma = ','
new1 = ''

#def commaComma(won, new):
for i in range(len(won)):
    i += 1
    minusIndex = i * -1
    if (i == (len(won))) or (minusIndex % 3 != 0):
        new = won[-i] + new
       print(new)
    else:
        new = comma + won[-i] + new

#print(commaComma(won2, new1))
print(new)

'''
for i in range(len(won)):
    i += 1
    minusIndex = i * -1
    if (i == (len(won))) or (minusIndex % 3 != 0):
        new = won[-i] + new
        print(new)
    else:
        new = comma + won[-i] + new
print(new)
'''
