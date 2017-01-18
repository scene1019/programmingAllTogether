import time
import random
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getPos()
x = pos.x
y = pos.y
z = pos.z

a = random.randint(5, 10)
mc.setBlock(x + a, y, z + a, 41)

while 1:
    pos = mc.player.getTIlePos()
    x = pos.x
    y = pos.y
    z = pos.z
    blockType = mc.getBlock(x, y, z)
    if blockType == 41:
        mc.postToChat("Treasure!")
        break
