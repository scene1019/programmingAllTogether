from mcpi.minecraft import Minecraft

mc = Minecraft.create()

while True:
    playerPos = mc.player.getPos()
    x = playerPos.x
    y = playerPos.y
    z = playerPos.z
    highest = mc.getHeight(x,z)
    mc.postToChat("y: %d, HIGHEST: %d" %(y, highest))
