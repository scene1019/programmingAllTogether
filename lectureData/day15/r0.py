from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    playerPos = mc.player.getPos()
    x = playerPos.x
    y = playerPos.y
    z = playerPos.z
    mc.postToChat("x: %d, y: %d, z: %d" %(x, y, z))
