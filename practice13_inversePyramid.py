# 마인크래프트에 연결하기
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 플레이어의 현재 좌표
playerPos = mc.player.getTilePos()
x = playerPos.x #플레이어의 현재 x좌표
y = playerPos.y #플레이어의 현재 y좌표
z = playerPos.z #플레이어의 현재 z좌표

blockType = 41 # gold block

# 가로, 세로, 높이 10짜리 피라미드 만들기
#airArea = 100
#mc.setBlocks(x, y, z, x+airArea, y+airArea, z+airArea, 0)

length = 21
height = 11
y = y + height

for i in range(height):
    for col in range(length):
        for row in range(length):
            mc.setBlock(x+col+i, y-i, z+row+i, blockType)
    length = length - 2   
