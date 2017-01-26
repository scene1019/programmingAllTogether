from mcpi.minecraft import Minecraft
import random

mc = Minecraft.create()

playerPos = mc.player.getPos()
ox = playerPos.x
oy = playerPos.y
oz = playerPos.z
goldx = ox+random.randint(-10,10)
goldz = oz+random.randint(-10,10)
goldy = mc.getHeight(goldx,goldz)

while True:
    playerPos = mc.player.getPos()
    x = playerPos.x
    y = playerPos.y
    z = playerPos.z
    mc.postToChat("GOLD: %d, %d, %d" %(goldx,goldy,goldz))
    mc.postToChat(" NOW: %d, %d, %d" %(x,y,z))
    if int(goldx) == int(x):
        mc.postToChat("*"*50)
        break
