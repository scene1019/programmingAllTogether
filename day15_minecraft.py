from mcpi.minecraft import Minecraft
import random
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)

a = random.randint(-10, 10)
goldX = x + a
goldZ = z + a
goldY = mc.getHeight(goldX, goldZ)
#mc.setBlock()

while 1:
    pos = mc.player.getTilePos()
    x = int(pos.x)
    y = int(pos.y)
    z = int(pos.z)
    mc.postToChat("Me   x: %d, y: %d, z: %d" %(x, y, z))
    mc.postToChat("gold x: %d, y: %d, z: %d" %(goldX, goldY, goldZ))
    if mc.getBlock(x, y-1, z) == 41 #goldX == x:
        mc.postToChat("=" * 64)
        break

#mc.postToChat("hello")

