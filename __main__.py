### Basic platformer with object detection and sprites

import pygame
from pygame.locals import *
from core import *
import sys

## Start pygame
pygame.init()
info = pygame.display.Info()
width, height = (info.current_w, info.current_h)
screen = pygame.display.set_mode((800,600))
screen.fill((255,255,255))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

## Variables
resetOriginalPos = 0

TotalRP = 0
timeBar = progressBar(60)
# Display
sFullscreen = False
F11Mode = "enlarge"
#         "shrink"
# Game Speed
globalTick = 40
currentTick = 0
currentSecond = 0
moveMod = 1
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

# Pause Menu
def quitButtonPressed():
	running = False
	return running
quitButton = UIEngine.Button("Quit", quit, (50, 12))

# Levels
level = 1
# If level specified use that instead of default
del sys.argv[0]
if len(sys.argv) > 0:
	str(sys.argv[0]).split()
	import importlib
	module = importlib.import_module(sys.argv[0])
else:
	from levels.testLevel1 import *

running = True
while running:
	# Game tick and time code
	if currentTick < globalTick:
		currentTick += 1
	if currentTick/globalTick == 1:
		currentSecond += 1
		currentTick = 1
		# Represent game time with progress bars
		if timeBar.progress == timeBar.barLen:
			del timeBar
			timeBar = progressBar(60)
		timeBar.update()
	### if moveMod == 0 or clock.get_fps() == 0:
	### 	moveMod = 1
	### else:
	### 	moveMod = int(globalTick/clock.get_fps())
	### 	print(moveMod)

	# Update player charater animation
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

	# Update Entitys
	for i in range(len(entitys)):
		entitys[i].update()

	# Update display
	screen.fill((255, 255, 255))
	for i in range(len(platforms)):
		screen.blit(platforms[i].hitbox, platforms[i].PosXY)
	for i in range(len(entitys)):
		screen.blit(entitys[i].hitbox, entitys[i].PosXY)
	for i in range(len(checkpoints)):
		screen.blit(checkpoints[i].hitbox, checkpoints[i].PosXY)
	for i in range(len(regionpoints)):
		screen.blit(regionpoints[i].hitbox, regionpoints[i].PosXY)
	screen.blit(char, (PosX, PosY))
	for i in range(len(UIWidgets)):
		screen.blit(UIWidgets[i].hitbox, UIWidgets[i].PosXY)
		screen.blit(UIWidgets[i].Text, [UIWidgets[i].PosXY[0] + 5, UIWidgets[i].PosXY[1] + 4])

	fps = font.render(str("FPS:"), True, (100, 100, 100))
	fpsNum = font.render(str(int(clock.get_fps())), True, (100, 100, 100))
	screen.blit(fps, (50, 50))
	screen.blit(fpsNum, (100, 50))

	rp = font.render(str("RP: "), True, (100, 100, 100))
	rpNum = font.render(str(TotalRP), True, (100, 100, 100))
	screen.blit(rp, (50, 75))
	screen.blit(rpNum, (100, 75))

	clock.tick(globalTick)
	pygame.display.update()


	# Search for commands
	for event in pygame.event.get():
		# Detect for exit commands
		if event.type == QUIT:
			running = False
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False

		# enable fullscreen
		if event.type == KEYDOWN:
			if event.key == K_F11:
				if sFullscreen == False and F11Mode == "enlarge":
					screen = pygame.display.set_mode((width, 600), FULLSCREEN)
					pygame.display.update()
					sFullscreen = True
					#globalTick = 30
					#moveMod = clock.get_fps()/globalTick
				if sFullscreen == True and F11Mode == "shrink":
					screen = pygame.display.set_mode((800,600))
					sFullscreen = False
					globalTick = 40
					moveMod = 1
				if sFullscreen == True:
					F11Mode = "shrink"
				if sFullscreen == False:
					F11Mode = "enlarge"

		# Detect if mouse has clicked any UI elements
		if event.type == MOUSEBUTTONUP:
			for i in range(len(UIWidgets)):
				if collision(pygame.Surface((0,0)), UIWidgets[i].hitbox, pygame.mouse.get_pos(), UIWidgets[i].PosXY):
					UIWidgets[i].Function()

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
			platforms[i].PosXY[0] += 10 * moveMod
		for i in range(len(entitys)):
			entitys[i].PosXY[0] += 10 * moveMod
		for i in range(len(checkpoints)):
			checkpoints[i].PosXY[0] += 10 * moveMod
		for i in range(len(regionpoints)):
			regionpoints[i].PosXY[0] += 10 * moveMod
		resetOriginalPos += 10 * moveMod
	elif right == True:
		for i in range(len(platforms)):
			platforms[i].PosXY[0] -= 10 * moveMod
		for i in range(len(entitys)):
			entitys[i].PosXY[0] -= 10 * moveMod
		for i in range(len(checkpoints)):
			checkpoints[i].PosXY[0] -= 10 * moveMod
		for i in range(len(regionpoints)):
			regionpoints[i].PosXY[0] -= 10 * moveMod
		resetOriginalPos -= 10 * moveMod

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
			for i in range(len(entitys)):
				entitys[i].PosXY[0] -= resetOriginalPos
			for i in range(len(checkpoints)):
				checkpoints[i].PosXY[0] -= resetOriginalPos
			for i in range(len(regionpoints)):
				regionpoints[i].PosXY[0] -= resetOriginalPos
			resetOriginalPos = 0
		else:
			PosX, PosY = int(250), int(0)
			for i in range(len(platforms)):
				platforms[i].PosXY[1] -= 600
			for i in range(len(entitys)):
				entitys[i].PosXY[1] -= 600
			for i in range(len(checkpoints)):
				checkpoints[i].PosXY[1] -= 600
			for i in range(len(regionpoints)):
				regionpoints[i].PosXY[1] -= 600
			levelHeight -= 1
	# Above
	if PosY < 0:
		PosX, PosY = int(250), int(600)
		for i in range(len(platforms)):
			platforms[i].PosXY[1] += 600
		for i in range(len(entitys)):
			entitys[i].PosXY[1] += 600
		for i in range(len(checkpoints)):
			checkpoints[i].PosXY[1] += 600
		for i in range(len(regionpoints)):
			regionpoints[i].PosXY[1] += 600
		levelHeight += 1

	# Prevent falling through the floor
	# Do twice to avoid conflict with gravity
	for i in range(2):
		for p in range(len(platforms)):
			if platforms[p].physicalState == "Solid":
				lift = 10
			if platforms[p].physicalState == "Liquid":
				lift = -4
			if platforms[p].physicalState == "Gas":
				lift = 0
			if collision(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
				if "Above" in relativeLocation(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
					PosY -= lift
				if "Below" in relativeLocation(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
					PosY += lift
				if lift == 10:
					if "Right" in relativeLocation(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
						for i in range(len(platforms)):
							platforms[i].PosXY[0] += lift
						for i in range(len(entitys)):
							entitys[i].PosXY[0] += lift
						for i in range(len(checkpoints)):
							checkpoints[i].PosXY[0] += lift
						for i in range(len(regionpoints)):
							regionpoints[i].PosXY[0] += lift
						resetOriginalPos += lift
					if "Left" in relativeLocation(char, platforms[p].hitbox, (PosX, PosY), platforms[p].PosXY):
						for i in range(len(platforms)):
							platforms[i].PosXY[0] -= lift
						for i in range(len(entitys)):
							entitys[i].PosXY[0] -= lift
						for i in range(len(checkpoints)):
							checkpoints[i].PosXY[0] -= lift
						for i in range(len(regionpoints)):
							regionpoints[i].PosXY[0] -= lift
						resetOriginalPos -= lift


	# Detect new region points and update counter
	for i in range(len(regionpoints)):
		if collision(char, regionpoints[i].hitbox, (PosX, PosY), regionpoints[i].PosXY):
			if regionpoints[i].Collected == False:
				TotalRP += 1
				regionpoints[i].Collected = True

	# Level specific code
	# Level changer and loading system
	for i in range(len(checkpoints)):
		if collision(char, checkpoints[i].hitbox, (PosX, PosY), checkpoints[i].PosXY):
			level += 1
	# launch level 2
	if level == 2:
		# if level 1 isnt completed
		if level1Done == False:
			level1Done = True
			resetOriginalPos = clearLevel(resetOriginalPos)
			from levels.testLevel2 import *
	# launch level 3
	if level == 3:
		# if level 2 isnt completed
		if level2Done == False:
			level2Done = True
			resetOriginalPos = clearLevel(resetOriginalPos)
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
			rotatingPlat.PosXY[1] += 200
		if rotatingPlatClock/40 == 3:
			rotatingPlat.PosXY[0] -= 400
			rotatingPlat.PosXY[1] -= 200
			rotatingPlatClock = 0
	if level == 4:
		if level3Done == False:
			level3Done = True
			resetOriginalPos = clearLevel(resetOriginalPos)
			from levels.testLevel4 import *
	if level == 5:
		if level4Done == False:
			level4Done = True
			resetOriginalPos = clearLevel(resetOriginalPos)
			from levels.testLevel5 import *
	if level == 6:
		running = False
