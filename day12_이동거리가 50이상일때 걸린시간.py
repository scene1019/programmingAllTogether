
import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()

#from mcpi.minecraft import Minecraft
import time
import math
#mc = Minecraft.create()



pos1 = mc.player.getTilePos()
x1 = pos1.x
y1 = pos1.y
z1 = pos1.z
time1 = time.clock()

#time.sleep(15)

pos2 = mc.player.getTilePos()
x2 = pos2.x
y2 = pos2.y
z2 = pos2.z

distance = int(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)) 

while distance < 10: # < 대신 <=을 써도 되요.
    pos2 = mc.player.getTilePos()
    x2 = pos2.x
    y2 = pos2.y
    z2 = pos2.z
    distance = int(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)) 

time2 = time.clock()
runTime = round(time2 - time1, 2) 

mc.postToChat("The player has moved: " + str(int(distance)))
mc.postToChat("The moving time is " + str(int(runTime))) 
#print("애기가 이동한 시간은", str(int(runTime)), "입니다.")


