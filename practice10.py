# 마인크래프트에 연결하기
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 플레이어의 현재 좌표
playerPos = mc.player.getTilePos()
x = playerPos.x #x = 플레이어의 현재 x좌표
y = playerPos.y #y = 플레이어의 현재 y좌표
z = playerPos.z #z = 플레이어의 현재 z좌표

blockType = 41      # gold block

# 가로, 세로 10짜리 정사각형 블록 만들기
for i in range(10):
    mc.setBlock(x, y, z, blockType)
    x = x + 1

for i in range(10):
    z = z + 1
    mc.setBlock(x - 1, y, z, blockType)
        

    
# for
