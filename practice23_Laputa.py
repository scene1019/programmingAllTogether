from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

# 첫 번째 블록은 금 블록, blockType = 41
x1 = random.randint(x-10, x+10)
y1 = y + 10
z1 = random.randint(z-10, z+10)
mc.player.setTilePos(x1, y1, z1)
mc.setBlock(x1, y1-1, z1, 41)


# 두 번째 블록은 다이아몬드, blockType = 57
x2 = random.randint(x-10, x+10)
y2 = y + 10
z2 = random.randint(z-10, z+10)
mc.player.setTilePos(x2, y2, z2)
mc.setBlock(x2, y2-1, z2, 57)

# 세 번째 블록은 에메랄드, blockType = 133
x3 = random.randint(x-10, x+10)
y3 = y + 10
z3 = random.randint(z-10, z+10)
mc.player.setTilePos(x3, y3, z3)
mc.setBlock(x3, y3-1, z3, 133)


i = 0
while 0 == mc.getBlock(x1+1, y1-1-i, z1+1+i):
    mc.setBlock(x1+1, y1-1-i, z1+1+i, 41)
    i += 1

i = 0
while 0 == mc.getBlock(x2+1, y2-1-i, z2+1+i):
    mc.setBlock(x2+1, y2-1-i, z2+1+i, 57)
    i += 1

i = 0
while 0 == mc.getBlock(x3+1, y3-1-i, z3+1+i):
    mc.setBlock(x3+1, y3-1-i, z3+1+i, 133)
    i += 1

mc.postToChat("1: (%d, %d, %d)  2: (%d, %d, %d)  3: (%d, %d, %d)" %(x1, y1, z1, x2, y2, z2, x3, y3, z3))

# 1 to 2
if (x2 - x1 > 0) and (z2 - z1 > 0):
    while x2 - x1 != 0:
        mc.setBlock(x1+1, y1-1, z1, 17) # blockType = 17 = 가문비나무
        x1 += 1
    while z2 - z1 != 0:
        mc.setBlock(x1, y1-1, z1, 1) # blockType = 1 = 돌
        z1 += 1

elif (x2 - x1 > 0) and (z2 - z1 < 0):
    while x2 - x1 != 0:
        mc.setBlock(x1+1, y1-1, z1, 17)
        x1 += 1
    while z2 - z1 != 0:
        mc.setBlock(x1, y1-1, z1, 1)
        z1 -= 1

elif (x2 - x1 < 0) and (z2 - z1 > 0):
    while x2 - x1 != 0:
        mc.setBlock(x1-1, y1-1, z1, 17)
        x1 -= 1
    while z2 - z1 != 0:
        mc.setBlock(x1, y1-1, z1, 1)
        z1 += 1

else:
    while x2 - x1 != 0:
        mc.setBlock(x1-1, y1-1, z1, 17)
        x1 -= 1
    while z2 - z1 != 0:
        mc.setBlock(x1, y1-1, z1, 1)
        z1 -= 1

'''
# 1 to 3
if (x3 - x1 > 0) and (z3 - z1 > 0):
    while x3 - x1 != 0:
        mc.setBlock(x1+1, y1-1, z1, 17)
        x1 += 1
    while z3 - z1 != 0:
        mc.setBlock(x1, y1-1, z1, 1)
        z1 += 1

elif (x3 - x1 > 0) and (z3 - z1 < 0):
    while x3 - x1 != 0:
        mc.setBlock(x1+1, y1-1, z1, 17)
        x1 += 1
    while z3 - z1 != 0:
        mc.setBlock(x1, y1-1, z1, 1)
        z1 -= 1

elif (x3 - x1 < 0) and (z3 - z1 > 0):
    while x3 - x1 != 0:
        mc.setBlock(x1-1, y1-1, z1, 17)
        x1 -= 1
    while z3 - z1 != 0:
        mc.setBlock(x1, y1-1, z1, 1)
        z1 += 1

else:
    while x3 - x1 != 0:
        mc.setBlock(x1-1, y1-1, z1, 17)
        x1 -= 1
    while z3 - z1 != 0:
        mc.setBlock(x1, y1-1, z1, 1)
        z1 -= 1
'''

'''
# 2 to 1
if (x1 - x2 > 0) and (z1 - z2 > 0):
    while x1 - x2 != 0:
        mc.setBlock(x2+1, y2-1, z2, 17)
        x2 += 1
    while z1 - z2 != 0:
        mc.setBlock(x2, y2-1, z2, 1)
        z2 += 1

elif (x1 - x2 > 0) and (z1 - z2 < 0):
    while x1 - x2 != 0:
        mc.setBlock(x2+1, y2-1, z2, 17)
        x2 += 1
    while z1 - z2 != 0:
        mc.setBlock(x2, y2-1, z2, 1)
        z2 -= 1

elif (x1 - x2 < 0) and (z1 - z2 > 0):
    while x1 - x2 != 0:
        mc.setBlock(x2-1, y2-1, z2, 17)
        x2 -= 1
    while z1 - z2 != 0:
        mc.setBlock(x2, y2-1, z2, 1)
        z2 += 1

else:
    while x1 - x2 != 0:
        mc.setBlock(x2-1, y2-1, z2, 17)
        x2 -= 1
    while z1 - z2 != 0:
        mc.setBlock(x2, y2-1, z2, 1)
        z2 -= 1
'''
# 2 to 3
if (x3 - x2 > 0) and (z3 - z2 > 0):
    while x3 - x2 != 0:
        mc.setBlock(x2+1, y2-1, z2, 17)
        x2 += 1
    while z3 - z2 != 0:
        mc.setBlock(x2, y2-1, z2, 1)
        z2 += 1

elif (x3 - x2 > 0) and (z3 - z2 < 0):
    while x3 - x2 != 0:
        mc.setBlock(x2+1, y2-1, z2, 17)
        x2 += 1
    while z3 - z2 != 0:
        mc.setBlock(x2, y2-1, z2, 1)
        z2 -= 1

elif (x3 - x2 < 0) and (z3 - z2 > 0):
    while x3 - x2 != 0:
        mc.setBlock(x2-1, y2-1, z2, 17)
        x2 -= 1
    while z3 - z2 != 0:
        mc.setBlock(x2, y2-1, z2, 1)
        z2 += 1

else:
    while x3 - x2 != 0:
        mc.setBlock(x2-1, y2-1, z2, 17)
        x2 -= 1
    while z3 - z2 != 0:
        mc.setBlock(x2, y2-1, z2, 1)
        z2 -= 1

# 3 to 1
if (x1 - x3 > 0) and (z1 - z3 > 0):
    while x1 - x3 != 0:
        mc.setBlock(x3+1, y3-1, z3, 17)
        x3 += 1
    while z1 - z3 != 0:
        mc.setBlock(x3, y3-1, z3, 1)
        z3 += 1

elif (x1 - x3 > 0) and (z1 - z3 < 0):
    while x1 - x3 != 0:
        mc.setBlock(x3+1, y3-1, z3, 17)
        x3 += 1
    while z1 - z3 != 0:
        mc.setBlock(x3, y3-1, z3, 1)
        z3 -= 1

elif (x1 - x3 < 0) and (z1 - z3 > 0):
    while x1 - x3 != 0:
        mc.setBlock(x3-1, y3-1, z3, 17)
        x3 -= 1
    while z1 - z3 != 0:
        mc.setBlock(x3, y3-1, z3, 1)
        z3 += 1

else:
    while x1 - x3 != 0:
        mc.setBlock(x3-1, y3-1, z3, 17)
        x3 -= 1
    while z1 - z3 != 0:
        mc.setBlock(x3, y3-1, z3, 1)
        z3 -= 1

'''
# 3 to 2
if (x2 - x3 > 0) and (z2 - z3 > 0):
    while x2 - x3 != 0:
        mc.setBlock(x3+1, y3-1, z3, 17)
        x3 += 1
    while z2 - z3 != 0:
        mc.setBlock(x3, y3-1, z3, 1)
        z3 += 1

elif (x2 - x3 > 0) and (z2 - z3 < 0):
    while x2 - x3 != 0:
        mc.setBlock(x3+1, y3-1, z3, 17)
        x3 += 1
    while z2 - z3 != 0:
        mc.setBlock(x3, y3-1, z3, 1)
        z3 -= 1

elif (x2 - x3 < 0) and (z2 - z3 > 0):
    while x2 - x3 != 0:
        mc.setBlock(x3-1, y3-1, z3, 17)
        x3 -= 1
    while z2 - z3 != 0:
        mc.setBlock(x3, y3-1, z3, 1)
        z3 += 1

else:
    while x2 - x3 != 0:
        mc.setBlock(x3-1, y3-1, z3, 17)
        x3 -= 1
    while z2 - z3 != 0:
        mc.setBlock(x3, y3-1, z3, 1)
        z3 -= 1
'''
'''
roadx21 = x2 - x1
roadz21 = z2 - z1
reviseZ21 = abs(roadz21) - 1

if (roadx21 > 0):
    for i in range(roadx21):
        i += 1
        mc.setBlock(x1+i, y1-1, z1, 17)
    if roadz21 > 0:
        for j in range(reviseZ21):
            j += 1
            mc.setBlock(x1+roadx21, y1-1, z1+j, 1) #
    else:
        for j in range(reviseZ21):
            j += 1
            mc.setBlock(x1+abs(roadx21), y1-1, z1-j, 1) #
else:
    for i in range(abs(roadx21)):
        i += 1
        mc.setBlock(x1-i, y1-1, z1, 17)
    if roadz21 > 0:
        for j in range(reviseZ21):
            j += 1
            mc.setBlock(x1+abs(roadx21), y1-1, z1+j, 1)
    else:
        for j in range(reviseZ21):
            j += 1
            mc.setBlock(x1+roadx21, y1-1, z1-j, 1)

roadx32 = x3 - x2
roadz32 = z3 - z2
reviseZ32 = abs(roadz21) - 1

if (roadx32 > 0):
    for i in range(roadx32):
        i += 1
        mc.setBlock(x2+i, y2-1, z2, 17)
    if roadz32 > 0:
        for j in range(reviseZ32):
            j += 1
            mc.setBlock(x2+roadx32, y2-1, z2+j, 1) #
    else:
        for j in range(reviseZ32):
            j += 1
            mc.setBlock(x2+roadx32, y2-1, z2-j, 1) #
else:
    for i in range(abs(roadx32)):
        i += 1
        mc.setBlock(x2-i, y2-1, z2, 17)
    if roadz32 > 0:
        for j in range(reviseZ32):
            j += 1
            mc.setBlock(x2+roadx32, y2-1, z2+j, 1)
    else:
        for j in range(reviseZ32):
            j += 1
            mc.setBlock(x2+roadx32, y2-1, z2-j, 1)

'''
'''
roadx32 = x3 - x2
roadz32 = z3 - z2

if (roadx32 > 0):
    for i in range(roadx32):
        i += 1
        mc.setBlock(x2+i, y2-1, z2, 17)
    if roadz32 > 0:
        for j in range(roadz32):
            j += 1
            mc.setBlock(x2+roadx32, y2-1, z2+j-1, 1)
    else:
        for j in range(abs(roadz32)):
            j += 1
            mc.setBlock(x2+roadx32, y2-1, z2-j-1, 1)
else:
    for i in range(abs(roadx32)):
        i += 1
        mc.setBlock(x2-i, y2-1, z2, 17)
    if roadz32 > 0:
        for j in range(roadz32):
            j += 1
            mc.setBlock(x2+roadx32, y2-1, z2+j-1, 1)
    else:
        for j in range(abs(roadz32)):
            j += 1
            mc.setBlock(x2+roadx32, y2-1, z2-j-1, 1)

'''

'''
        for j in range(roadx21):
            j += 1
            mc.setBlock(x1+j, y1, z1+i, 17)
elif (roadx21 > 0) and (roadz21 < 0):
    for i in range(roadz21):
        i += 1
        for j in range(abs(roadx21)):
            j += 1
            mc.setBlock(x1+j, y1, z1-i, 17)
elif (roadx21 < 0) and (roadz21 > 0):
    for i in range(roadz21):
        i += 1
        for j in range(abs(roadx21)):
            j += 1
            mc.setBlock(x1-j, y1, z1+i, 17)
else:
    for i in range(abs(roadz21)):
        i += 1
        for j in range(abs(roadx21)):
            j += 1
            mc.setBlock(x1-j, y1, z1-i, 17)
            '''

'''
if roadx12 > 0:
    for i in range(roadx12):
        i += 1
        mc.setBlock(x1 + i, y1, z1, 17)
    if roadz12 > 0:
        for i in range(roadz12):
            i += 1
            mc.setBlock(x2, y2, z2-i, 17)
    else:
        for i in range(abs(roadz12)):
            i += 1
            mc.setBlock(x2, y2, z2+i, 17)
else:
    for i in range(abs(roadx12)):
        i += 1
        mc.setBlock(x1+i, y1, z1, 17)
    if roadz12 > 0:
        for i in range(roadz12):
            i += 1
            mc.setBlock(x2, y2, z2-i, 17)
    else:
        for i in range(abs(roadz12)):
            i += 1
            mc.setBlock(x2, y2, z2+i, 17)
'''

'''
if road1 > 0:
    for i in range(road1):
        i += 1
        mc.setBlock(x1+i, y1, z1, 17)
else:
    for i in range(abs(road1)):
        i += 1
        mc.setBlock(x1-1, y1, z1, 17)

if road2 > 0:
    for i in range(road2):
        i += 1
        mc.setBlock(x1, y1, z1+i, 17)
else:
    for i in range(abs(road2)):
        i += 1
        mc.setBlock(x1, y1, z1-i, 17)

#mc.postToChat("%s, %s, %s" %(x1, y1, z1))
'''

