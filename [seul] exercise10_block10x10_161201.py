from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 80 # 눈 블록

for i in range(10):
    mc.setBlock(x, y, z, blockType)
    x = x + 1 # for 루프가 한 번 실행될 때마다 y가 1씩 증가
#    mc.player.setTilePos(x, y, z)
