from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import random

blockID = 41

pos = mc.player.getPos()
x = int(pos.x)
y = int(pos.y)
z = int(pos.z)

rx = random.randint(-10, 10)
ry = random.randint(5, 10)
rz = random.randint(-10, 10)

mc.setBlocks(x+rx-1, y+ry, z+rz-1, x+rx, y+ry, z+rz, blockID)

for i in range(ry):
    mc.setBlock(x+rx, y+ry-i, z+rz-i, blockID)
    mc.setBlock(x+rx+1, y+ry-i, z+rz-i, blockID)
