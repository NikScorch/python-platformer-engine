# Second test level

from os import path
import sys
sys.path.append(path.abspath('../20200205 Platformer Game'))

from core import *

# Variables
startY = int(450)
level2Done = False

# Platforms
plat = platform(200, 100, 150, 500)
plat.hitbox.fill((100, 100, 255))

spike = platform(150, 200, 450, 400)
spike.hitbox.fill((100, 100, 255))
spike2 = platform(100, 300, 700, 300)
spike2.hitbox.fill((100, 100, 255))
spike3 = platform(50, 400, 900, 200)
spike3.hitbox.fill((100, 100, 255))
spike4 = platform(25, 500, 1050, 100)
spike4.hitbox.fill((100, 100, 255))
spike5 = platform(25, 125, 1200, 475)
spike5.hitbox.fill((100, 100, 255))

plat = platform(500, 25, 1300, 150)
plat.hitbox.fill((100, 100, 255))
ceiling = platform(500, 25, 1300, 0)
ceiling.hitbox.fill((100, 100, 255))
longCeiling = platform(1000, 25, 800, -25)

hiddenPlat = platform(350, 10, 1400, 500)
hiddenPlat.hitbox.fill((250, 250, 250))

# Walls
wall = platform(250, 475, -100, 125)
wall.hitbox.fill((100, 100, 255))
wall2 = platform(525, 600, 1800, 0)
wall2.hitbox.fill((100, 100, 255))

# Checkpoint
checkP = checkpoint(1700, 75)
checkP.hitbox.fill((255, 150, 50))

# Region Point
regionP = regionPoint(1700, 425)
regionP.hitbox.fill((150, 200, 225))
