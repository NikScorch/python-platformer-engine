# First test level

from os import path
import sys
sys.path.append(path.abspath('../20200205 Platformer Game'))

from core import *

# Variables
startY = int(250)
level1Done = False

# Platforms
plat = platform(200, 300, (150, 300))
#plat.spriteAnimation("assets/char", "image")
plat.hitbox.fill((100, 100, 255))

floatPlat = platform(200, 25, (450, 200))
floatPlat.hitbox.fill((100, 100, 255))
floatPlat2 = platform(200, 25, (750, 200))
floatPlat2.hitbox.fill((100, 100, 255))

ceilingBlock1 = platform(25, 350, (1100, 0))
ceilingBlock1.hitbox.fill((100, 100, 255))
ceilingBlock2 = platform(25, 350, (1275, 0))
ceilingBlock2.hitbox.fill((100, 100, 255))
ceilingBlockTop = platform(150, 250, (1125, 0))
ceilingBlockTop.hitbox.fill((100, 100, 255))
ceilingBlockBase = platform(100, 25, (1175, 325))
ceilingBlockBase.hitbox.fill((100, 100, 255))
ceilingBlockOpening = platform(50, 100, (1125, 250))
ceilingBlockOpening.hitbox.fill((100, 100, 255))
ceilingBlockOpening.makeLiquid()

floorBlock = platform(200, 150 , (1100, 450))
floorBlock.hitbox.fill((100, 100, 255))

plat2 = platform(200, 200, (1450, 400))
plat2.hitbox.fill((100, 100, 255))
# Walls
wall = platform(250, 475, (-100, 125))
wall.hitbox.fill((100, 100, 255))

# Checkpoint
checkP = checkpoint((1550, 300))
checkP.hitbox.fill((255, 150, 50))

# Region Point
regionP = regionPoint((1225, 275))
regionP.hitbox.fill((150, 200, 255))
