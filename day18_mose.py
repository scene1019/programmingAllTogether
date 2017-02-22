from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

mc.setBlocks(x+2, y, z, x+2+10, y+5, z+10, 41)

while 1:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlock(x, y+2, z, 0)
