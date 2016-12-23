from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x,y,z = pos.x, pos.y, pos.z
blockType = 41

size = 10
height = size//2 + 1

for i in range(height):
    mc.setBlocks(x+i, y+i, z+i, x+size-i, y+i, z+size-i, blockType) 
