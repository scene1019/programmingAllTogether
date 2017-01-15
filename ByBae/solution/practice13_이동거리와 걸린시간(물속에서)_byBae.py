from mcpi.minecraft import Minecraft
import time
import math
mc = Minecraft.create()

playerPos1 = mc.player.getPos()
x1 = playerPos1.x
y1 = playerPos1.y
z1 = playerPos1.z

pos1Time = time.clock() # 첫 번째 위치에서 시간을 기록한다.

playerPos2 = mc.player.getPos()
x2 = playerPos2.x
y2 = playerPos2.y
z2 = playerPos2.z

inWater = 9 # 물 블록
# getBlock(x,y,z): 지정된 좌표의 블록ID를 리턴한다.
while mc.getBlock(x2,y2,z2) != inWater:
    # 물로 들어가면 루프가 종료된다.
    playerPos2 = mc.player.getPos()
    x2 = playerPos2.x
    y2 = playerPos2.y
    z2 = playerPos2.z

pos2Time = time.clock()

howFar = int(math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2))
howLong = round(pos2Time - pos1Time, 2)
mc.postToChat("You moved: "+str(howFar))
mc.postToChat("It took: "+str(howLong))
print(str(howFar)+"블록만큼 이동하는 데 "+str(howLong)+" cpu time이 걸렸군.")
