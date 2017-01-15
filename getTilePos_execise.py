from mcpi.minecraft import Minecraft as M
mc = M.create()

playerPos = mc.player.getTilePos()
x = playerPos.x
y = playerPos.y
z = playerPos.z

print("플레이어의 현재 x 좌표:", x)
print("플레이어의 현재 y 좌표:", y)
print("플레이어의 현재 z 좌표:", z)

mc.player.setTilePos(10, 110, 12)
