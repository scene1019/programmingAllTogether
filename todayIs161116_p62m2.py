from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x = 100
y = 20
z = 50
blockType = 103
mc.setBlock(x, y, z, blockType)
