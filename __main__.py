### Basic platformer with object detection and sprites

import pygame
from pygame.locals import *
from core import *

## Start pygame
pygame.init()
screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

## Variables
resetOriginalPos = 0
levelHeight = 0

globalTick = 40
currentTick = 0
currentSecond = 0
# Movement
up = False
down = False
left = False
right = False
jump = False
jumpTime = 0

# Character Sprite
char = pygame.image.load("assets/char/frame1.png")
char = pygame.transform.scale(char, (25, 25))
PosX, PosY = int(250), int(250)
charTick = 0

# Levels
platforms = []
checkpoints = []
level = 1
from levels.testLevel1 import *

running = True
while running:
	if currentTick < globalTick:
		currentTick += 1
	if currentTick/globalTick == 1:
		currentSecond += 1
		print(currentSecond)
		currentTick = 0

	charTick += 1
	if charTick/10 == 1:
		char = pygame.image.load("assets/char/frame1.png")
		char = pygame.transform.scale(char, (25, 25))
	if charTick/10 == 2:
		char = pygame.image.load("assets/char/frame2.png")
		char = pygame.transform.scale(char, (25, 25))
	if charTick/10 == 3:
		char = pygame.image.load("assets/char/frame3.png")
		char = pygame.transform.scale(char, (25, 25))
		charTick = 0


	clock.tick(globalTick)
	fps = font.render(str("FPS:"), True, (100, 100, 100))
	fpsNum = font.render(str(int(clock.get_fps())), True, (100,100,100))
	screen.blit(fps, (50, 50))
	screen.blit(fpsNum, (100, 50))

	# Update display
	pygame.display.update()
	screen.fill((255, 255, 255))
	screen.blit(char, (PosX, PosY))
	screen.blit(checkpoints[0].hitbox, checkpoints[0].PosXY)
	for i in range(len(platforms)):
		screen.blit(platforms[i].hitbox, platforms[i].PosXY)

	# Search for commands
	for event in pygame.event.get():
		# Detect for exit commands
		if event.type == QUIT:
			running = False
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

		# Detect for movement commands
		if event.type == KEYDOWN:
			# Y axis
			if event.key == K_w:
				up = True
				down = False
			if event.key == K_s:
				down = True
				up = False
			# X axis
			if event.key == K_a:
				left = True
				right = False
			if event.key == K_d:
				right = True
				left = False
		# Stop Movement
		if event.type == KEYUP:
			if event.key == K_w:
				up = False
			if event.key == K_s:
				down = False
			# X axis
			if event.key == K_a:
				left = False
			if event.key == K_d:
				right = False

		# Jump command
		# Only allow jumping if on a surface
		for i in range(len(platforms)):
			if collision(char, platforms[i].hitbox, (PosX, PosY + 10), platforms[i].PosXY):
				if event.type == KEYDOWN:
					if event.key == K_SPACE:
						jump = True

	## Update sprite position
	# Y axis
	if up == True:
		PosY -= 10
	elif down == True:
		PosY += 10
	# X axis, update platform pos rather than player
	# must go in opposite direction to player in order for it to work intuitively
	if left == True:
		for i in range(len(platforms)):
			platforms[i].PosXY[0] += 10
		checkpoints[0].PosXY[0] += 10
		resetOriginalPos += 10
	elif right == True:
		for i in range(len(platforms)):
			platforms[i].PosXY[0] -= 10
		checkpoints[0].PosXY[0] -= 10
		resetOriginalPos -= 10

	# Jump mechanics
	if jump == True:
		if jumpTime < 10:
			jumpTime += 1
			PosY -= 20
		elif jumpTime == 10:
			jumpTime = 0
			jump = False

	# Gravity
	PosY += 10
	# Out of bounds
	# Below
	if PosY > 600:
		if levelHeight == 0:
			PosX, PosY = int(250), int(startY)
			for i in range(len(platforms)):
				platforms[i].PosXY[0] -= resetOriginalPos
			checkpoints[0].PosXY[0] -= resetOriginalPos
			resetOriginalPos = 0
		else:
			PosX, PosY = int(250), int(0)
			for i in range(len(platforms)):
				platforms[i].PosXY[1] -= 600
			checkpoints[0].PosXY[1] -= 600
			levelHeight -= 1
	# Above
	if PosY < 0:
		PosX, PosY = int(250), int(600)
		for i in range(len(platforms)):
			platforms[i].PosXY[1] += 600
		checkpoints[0].PosXY[1] += 600
		levelHeight += 1

	# Prevent falling through the floor
	# Do twice to avoid conflict with gravity
	for i in range(2):
		for p in range(len(platforms)):
			if collision(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
				if "Above" in relativeLocation(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
					PosY -= 10
				if "Below" in relativeLocation(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
					PosY += 10
				if "Right" in relativeLocation(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
					for i in range(len(platforms)):
						platforms[i].PosXY[0] += 10
					checkpoints[0].PosXY[0] += 10
					resetOriginalPos += 10
				if "Left" in relativeLocation(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
					for i in range(len(platforms)):
						platforms[i].PosXY[0] -= 10
					checkpoints[0].PosXY[0] -= 10
					resetOriginalPos -= 10

	# Level specific code
	# Level changer and loading system
	if collision(char, checkpoints[0].hitbox, (PosX, PosY), checkpoints[0].PosXY):
		level += 1
	# launch level 2
	if level == 2:
		# if level 1 isnt completed
		if level1Done == False:
			level1Done = True
			for i in range(len(platforms)):
				platforms[i].PosXY[0] -= resetOriginalPos
			checkpoints[0].PosXY[0] -= resetOriginalPos
			resetOriginalPos = 0
			for i in range(len(platforms)):
				del platforms[0]
			del checkpoints[0]
			from levels.testLevel2 import *
	# launch level 3
	if level == 3:
		# if level 2 isnt completed
		if level2Done == False:
			level2Done = True
			for i in range(len(platforms)):
				platforms[i].PosXY[0] -= resetOriginalPos
			checkpoints[0].PosXY[0] -= resetOriginalPos
			resetOriginalPos = 0
			for i in range(len(platforms)):
				del platforms[0]
			del checkpoints[0]
			from levels.testLevel3 import *

		# Custom level code
		# Crusher movement
		if crusherLoop < 15:
			if crusherState == "Opening":
				topCrusher.movePos("Up")
				bottomCrusher.movePos("Down")
				crusherLoop += 1
			if crusherLoop == 15:
				crusherState = "Closing"
		if crusherLoop > 0:
			if crusherState == "Closing":
				topCrusher.movePos("Down")
				bottomCrusher.movePos("Up")
				crusherLoop -= 1
			if crusherLoop == 0:
				crusherState = "Opening"

		# Rotating Platform Position
		rotatingPlatClock += 1
		if rotatingPlatClock/40 == 1:
			rotatingPlat.PosXY[0] += 400
		if rotatingPlatClock/40 == 2:
			rotatingPlat.PosXY[1] += 300
		if rotatingPlatClock/40 == 3:
			rotatingPlat.PosXY[0] -= 400
			rotatingPlat.PosXY[1] -= 300
			rotatingPlatClock = 0
