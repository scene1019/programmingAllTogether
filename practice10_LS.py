#practice10_LS
from mcpi.minecraft import Minecraft
mc = Minecraft.create() 

playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
z = playerPos.z

blockType = 41

for i in range(10):
    for i in range(10):
        mc.setBlock(x, y, z, blockType)
        x = x + 1
    z = z + 1
    x = x - 10
