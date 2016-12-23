# 마인크래프트에 연결하기
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 플레이어의 현재 좌표
Pos = mc.player.getTilePos()

x = Pos.x    #x = 플레이어의 현재 x좌표
y = Pos.y    #y = 플레이어의 현재 y좌표
z = Pos.z    #z = 플레이어의 현재 z좌표

blockType = 5      # 블럭 종류


# 가로, 세로 10짜리 정사각형 블록 만들기
for z in range(z, z + 10, 1):   # for 
    for x in range(10):         # for 
        mc.player.setTilePos(x, y, z)
        mc.setBlock(x, y, z, blockType)




