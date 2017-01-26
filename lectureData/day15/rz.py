from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()
treasure = 41 # gold block

playerPos = mc.player.getPos()
ox = int(playerPos.x)
oy = int(playerPos.y)
oz = int(playerPos.z)
goldx = ox+random.randint(-10,10)
goldz = oz+random.randint(-10,10)
goldy = mc.getHeight(goldx,goldz)
mc.setBlock(goldx,goldy,goldz, treasure)

while True:
    playerPos = mc.player.getPos()
    x = int(playerPos.x)
    y = int(playerPos.y)
    z = int(playerPos.z)
    mc.postToChat("GOLD: %d, %d, %d" %(goldx,goldy,goldz))
    mc.postToChat(" NOW: %d, %d, %d" %(x,y,z))
    if mc.getBlock(x,y-1,z) == treasure:
        mc.postToChat("="*53)
        break
