from mcpi.minecraft import Minecraft
mc = Minecraft.create()

#블록 스매싱 가능 여부
mc.setting("world_immutable", False)
