from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 41


x1 = random.randint(x-10, x+10)
y1 = y + 10
z1 = random.randint(z-10, z+10)
mc.player.setTilePos(x1, y1, z1)
mc.setBlock(x1, y1-1, z1, blockType)

x2 = random.randint(x-10, x+10)
y2 = y + 10
z2 = random.randint(z-10, z+10)
mc.player.setTilePos(x2, y2, z2)
mc.setBlock(x2, y2-1, z2, blockType)

x3 = random.randint(x-10, x+10)
y3 = y + 10
z3 = random.randint(z-10, z+10)
mc.player.setTilePos(x3, y3, z3)
mc.setBlock(x3, y3-1, z3, blockType)


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

