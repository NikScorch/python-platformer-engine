# Third test level

from os import path
import sys
sys.path.append(path.abspath('../20200205 Platformer Game'))

from core import *

# Variables
startY = int(250)
level3Done = False
crusherLoop = 0
crusherState = "Opening"
rotatingPlatClock = 0

# Platforms
plat = platform(200, 275, 150, 325)
plat.hitbox.fill((100, 100, 255))

overhead = platform(300, 200, 300, 0)
overhead.hitbox.fill((100, 100, 255))
landing = platform(200, 350, 495, 250)
landing.hitbox.fill((100, 100, 255))

floatPlat = platform(200, 25, 1100, 275)
floatPlat.hitbox.fill((100, 100, 255))

rotatingPlat = platform(200, 100, 1100, 500)
rotatingPlat.hitbox.fill((100, 100, 255))

endPlat = platform(200, 25, 1425, 250)
endPlat.hitbox.fill((100, 100, 255))
endPlat2 = platform(75, 25, 1625, 425)
endPlat2.hitbox.fill((100, 100, 255))
endPlat3 = platform(75, 25, 1700, 350)
endPlat3.hitbox.fill((100, 100, 255))

# Walls
wall = platform(250, 475, -100, 125)
wall.hitbox.fill((100, 100, 255))

topCrusher = platform(150, 300, 850, 0)
topCrusher.hitbox.fill((100, 100, 255))
bottomCrusher = platform(150, 300, 850, 300)
bottomCrusher.hitbox.fill((100, 100, 255))

barrier = platform(25, 375, 1400, 0)
barrier.hitbox.fill((100, 100, 255))
barrier2 = platform(525, 600, 1775, 0)
barrier2.hitbox.fill((100, 100, 255))

# Checkpoint
checkP = checkpoint(1500, 150)
checkP.hitbox.fill((255, 150, 50))
