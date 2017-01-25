from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)

blockType = 41
randomRange = random.randint(-10, 10)
goldX = x + randomRange
goldZ = z + randomRange
goldY = mc.getHeight(goldX, goldZ)
mc.setBlock(goldX, goldY, goldZ, blockType)

while True:
    pos = mc.player.getTilePos()
    x = int(pos.x)
    y = int(pos.y)
    z = int(pos.z)
    distanceX = goldX - x
    distanceY = goldY - y
    distanceZ = goldZ - z
    # 금 블록까지 남은 거리를 x, y, z로 대화창에 출력하라.
    mc.postToChat("The Gold is x: %d, y: %d, z: %d block from here." %(distanceX, distanceY, distanceZ))
    # 어느쪽으로 가야 할지 방향을 대화창에 출력하라.

    #mc.postToChat("gold x: %d, y: %d, z: %d" %(goldX, goldY, goldZ))
    if mc.getBlock(x, y-1, z) == blockType:
        mc.postToChat("=" * 64)
        break

#mc.postToChat("go north/south/east/west")
