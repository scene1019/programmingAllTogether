from mcpi.minecraft import Minecraft
mc = Minecraft.create()

pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z

highBlockY = mc.getHeight(x, z)
mc.postToChat(highBlockY)