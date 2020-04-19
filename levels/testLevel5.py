# Fifth test level

from os import path
import sys
sys.path.append(path.abspath('../20200205 Platformer Game'))

from core import *

# Variables
startY = int(250)
level5Done = False

# Platforms
plat = platform(700, 300, (50, 300))
plat.hitbox.fill((100, 100, 255))