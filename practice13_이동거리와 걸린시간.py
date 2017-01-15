from mcpi.minecraft import Minecraft
import time
import math
mc = Minecraft.create()

time1 = time.clock()

pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

time.sleep(20)

pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z


time2 = time.clock()

runTime = time2 - time1 

distance = math.sqrt((x2-x1)**2 + (z2-z1)**2) 

mc.postToChat("The player has moved: " + str(distance) + "  time: " + str(runTime))

