from mcpi.minecraft import Minecraft
mc = Minecraft.create()


while True:
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    blockType = mc.getBlock(x, y, z)
    if blockType == 9:
        mc.postToChat("in water!")
        break


