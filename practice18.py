from mcpi.minecraft import Minecraft
import time
import random

mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

a = random.randint(50, 100)
highestBlockY = mc.getHeight(x, z)
y = highestBlockY
mc.setBlock(x + a, y, z + a, 41)

time1 = time.clock()

while True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    blockType = mc.getBlock(x, y-1, z)
    if blockType == 41:
        time2 = time.clock()
        timeTo = str(round(time2 - time1, 2))
        mc.postToChat("Treasure! time: " + timeTo)
        break


