# Fourth test level

from os import path
import sys
sys.path.append(path.abspath('../20200205 Platformer Game'))

from core import *

# Variables
startY = int(250)
level4Done = False

# Platforms
plat = platform(200, 300, 150, 300)
plat.hitbox.fill((100, 100, 255))

floatPlat = platform(200, 25, 475, 200)
floatPlat.hitbox.fill((100, 100, 255))

mainPlat1 = platform(100, 300, 775, 300)
mainPlat1.hitbox.fill((100, 100, 255))
mainPlat2 = platform(250, 350, 875, 250)
mainPlat2.hitbox.fill((100, 100, 255))
mainPlat3 = platform(200, 250, 1125, 350)
mainPlat3.hitbox.fill((100, 100, 255))
mainPlat4 = platform(250, 300, 1325, 300)
mainPlat4.hitbox.fill((100, 100, 255))
mainPlat5 = platform(100, 350, 1575, 250)
mainPlat5.hitbox.fill((100, 100, 255))

plat2 = platform(100, 25, 1825, 175)
plat2.hitbox.fill((100, 100, 255))

# Walls
wall = platform(250, 475, -100, 125)
wall.hitbox.fill((100, 100, 255))

EndWallFront1 = platform(25, 500, 1925, 0)
EndWallFront1.hitbox.fill((100, 100, 255))
EndWallFront2 = platform(25, 50, 1925, 550)
EndWallFront2.hitbox.fill((100, 100, 255))
EndWallBarrier = platform(525, 600, 2075, 0)
EndWallBarrier.hitbox.fill((100, 100, 255))
EndWallBase = platform(125, 50, 1950, 550)
EndWallBase.hitbox.fill((100, 100, 255))
EndWallTop = platform(125, 25, 1950, 0)
EndWallTop.hitbox.fill((100, 100, 255))
EndWallLedge = platform(25, 25, 1900, 550)
EndWallLedge.hitbox.fill((100, 100, 255))

EndWallEntrance = platform(25, 50, 1925, 500)
EndWallEntrance.hitbox.fill((100, 100, 255))
EndWallEntrance.makeGas()
EndWallClimb = platform(125, 400, 1950, 150)
EndWallClimb.hitbox.fill((100, 100, 255))
EndWallClimb.makeLiquid()
EndWallClimb2 = platform(125, 125, 1950, 25)
EndWallClimb2.hitbox.fill((255, 255, 255))
EndWallClimb2.makeLiquid()

# Mobs
Mob = entity(775, 60)
Mob = entity(1150, 70)
Mob = entity(1200, 80)
Mob = entity(1250, 90)
Mob = entity(1300, 100)

# Checkpoints
checkP = checkpoint(1875, 125)
checkP.hitbox.fill((255, 150, 100))

# Region Point
regionP = regionPoint(2000, 75)
regionP.hitbox.fill((150, 200, 255))
