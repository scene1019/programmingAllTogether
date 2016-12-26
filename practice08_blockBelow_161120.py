from mcpi.minecraft import Minecraft
mc = Minecraft.create()
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
blockType = 80 # 눈 블록


for i in range(10):
    y = y + 1 # for 루프가 한 번 실행될 때마다 y가 1씩 증가
    mc.player.setTilePos(x, y, z)
    mc.setBlock(x, y - 1, z, blockType)
    
