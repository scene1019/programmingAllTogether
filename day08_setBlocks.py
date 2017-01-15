from mcpi.minecraft import Minecraft
mc = Minecraft.create()

playerPos = mc.player.getTilePos() #3차원 좌표를 한번에 리턴하므로 x, y, z를 따로 사용하려면 나줘주어야 함.
x = playerPos.x
y = playerPos.y
z = playerPos.z

blockType = 41

mc.setBlocks(x,y,z,x+3, y+3, z+3, blockType)

blockType = 8
mc.setBlocks(x-1,y-1,z-1,x+3-1, y+3-1, z+3-1, blockType)
