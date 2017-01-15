# version 1.1
from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

playerPos1 = mc.player.getPos()
x = playerPos1.x
y = playerPos1.y
z = playerPos1.z

blockType = 41

for i in range(3):
    time.sleep(5)
    where = random.randint(1,10)
    x = x + where
    y = y + where
    z = z + where
    mc.player.setTilePos(x,y,z)
    mc.setBlock(x,y-1,z,blockType) # 금 블록을 추가하는 코드(y-1)를 둔다.
