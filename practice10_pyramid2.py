from mcpi.minecraft import Minecraft
mc = Minecraft.create()

playerPos = mc.player.getTilePos() 
x = playerPos.x
y = playerPos.y
z = playerPos.z

blockType = 41

for i in range(20):
    for col in range(10):
        for row in range(10):
            mc.setBlock(x+i+col, y+i, z+i+row, blockType)

