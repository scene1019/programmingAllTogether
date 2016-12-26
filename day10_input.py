from mcpi.minecraft import Minecraft
mc = Minecraft.create()


    
#height = int(input("몇층으로 할까요?: "))

#height = 5
playerPos = mc.player.getTilePos()
x = playerPos.x 
y = playerPos.y 
z = playerPos.z

try:
    blockType = int(input("어떤 블록을 놓을까요?: "))
    for i in range(5):
        mc.setBlock(x,y+i,z, blockType)

except:
    mc.postToChat("enter the number!")


