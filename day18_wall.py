from mcpi.minecraft import Minecraft
import time
import random
mc = Minecraft.create()

'''
pos = mc.player.getTilePos()
x = pos.x
y = pos.y
z = pos.z
'''

answer = input("Create a crater? Y/N ").upper()

while (answer != 'Y') and (answer != 'N'):
    answer = input("Create a crater? Y/N ").upper()

if answer == "Y":
    pos = mc.player.getTilePos()
    x = pos.x
    y = pos.y
    z = pos.z
    mc.setBlocks(x+1, y-1, z+1, x-1, y-1, z-1, 0)
    mc.postToChat("Boom!")


    '''
tall = random.randint(5,10)

for i in range(tall):
    y += 1
    for i in range(10):
        mc.setBlock(x, y, z+2+i, 41)
        time.sleep(1)
'''
