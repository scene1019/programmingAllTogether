from mcpi.minecraft import Minecraft
mc = Minecraft.create()

playerPos = mc.player.getTilePos() #3차원 좌표를 한번에 리턴하므로 x, y, z를 따로 사용하려면 나줘주어야 함.
x = playerPos.x
y = playerPos.y
z = playerPos.z

blockType = 41

for col in range(10):
    for row in range(10):
        for i in range(10):
            mc.setBlock(x + col, y + i, z + row, blockType)
