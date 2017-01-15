from mcpi.minecraft import Minecraft as M
mc = M.create() #마인크래프트 플레이어에 연결
#mc.player.setTilePos(x,y,z) #int
#mc.player.setPos(x,y,z) #float
#time.sleep() #time 모듈에서 sleep을 가져오세요.

x=20
y=20
z=20

blockType = 103
mc.setBlock(x, y, z, blockType)
