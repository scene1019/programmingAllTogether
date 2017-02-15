from mcpi.minecraft import Minecraft
import time
mc = Minecraft.create()

'''
while 1:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.postToChat("Now: %s, %s, %s" %(x, y, z))
'''
for i in range(10):
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    time.sleep(2)
    mc.player.setPos(x, y, z+2)
    mc.setBlock(x, y-1, z+2, 41)



