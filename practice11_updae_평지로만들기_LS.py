from mcpi.minecraft import Minecraft
mc = Minecraft.create()
 
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
size = 100

blockType = 0
mc.setBlocks(x, y, z, x+size, y+size, z+size, blockType)

