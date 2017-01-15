from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
size = 5 #욕조 한 변의 크기

blockType = 41
mc.setBlocks(x, y, z, x+size, y+size, z+size, blockType)

blockType = 8
mc.setBlocks(x+1, y+1, z+1, x+size-1, y+size, z+size-1, blockType)
