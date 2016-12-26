from mcpi.minecraft import Minecraft
mc = Minecraft.create()

playerPos = mc.player.getTilePos()
x = playerPos.x 
y = playerPos.y 
z = playerPos.z

blockType = 41

for i in range(0, 10, 2):
    mc.setBlock(x+i, y, z, blockType)
