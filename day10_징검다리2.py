# 마인크래프트에 연결하기
from mcpi.minecraft import Minecraft
mc = Minecraft.create()

# 플레이어의 현재 좌표
playerPos = mc.player.getTilePos()
x = playerPos.x #플레이어의 현재 x좌표
y = playerPos.y #플레이어의 현재 y좌표
z = playerPos.z #플레이어의 현재 z좌표

blockType = 41 # gold block

for i in range(6):
    mc.setBlock(x+i, y, z, 0)
    mc.setBlock(x+i+1, y, z, blockType)
    x= x+1
