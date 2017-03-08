from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random


pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 41

x1 = random.randint(x-10, x+10)
y1 = random.randint(y+1, y+10)
z1 = random.randint(z-10, z+10)

mc.player.setTilePos(x1, y1, z1)
mc.setBlock(x1, y1, z1, 41)

high = y1 - y
for i in range(high):
    mc.setBlock(x1+i, y1-i, z1, 17)