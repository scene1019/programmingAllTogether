from mcpi.minecraft import Minecraft
import time
import math
mc = Minecraft.create()

time1 = time.clock()

pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z

pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

inWater = 9

while mc.getBlock(x2, y2, z2) != inWater:
    pos2 = mc.player.getTilePos()
    x2, y2, z2 = pos2.x, pos2.y, pos2.z


time2 = time.clock()

howLong = round(time2 - time1, 2) #round 함수 = 지정한 (소수점 뒤) 자릿수로 반올림

distance = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)

mc.postToChat("The player has moved: " + str(distance) + "  time: " + str(howLong))

