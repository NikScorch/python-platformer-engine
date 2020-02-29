### Functions and Classes that will be used in the program

import pygame
from pygame.locals import *
import os
import sys
platforms = []
checkpoints = []
regionpoints = []
entitys = []
levelHeight = 0

## Functions
def clearLevel(resetOriginalPos):
	for i in range(len(platforms)):
		platforms[0].PosXY[0] -= resetOriginalPos
		del platforms[0]
	for i in range(len(checkpoints)):
		checkpoints[0].PosXY[0] -= resetOriginalPos
		del checkpoints[0]
	for i in range(len(regionpoints)):
		regionpoints[0].PosXY[0] -= resetOriginalPos
		del regionpoints[0]
	resetOriginalPos = 0
	return resetOriginalPos

def collision(obj1, obj2, obj1Pos, obj2Pos):
	# tracks top left corner of obj1 to see if it
	# collides with anywhere on the top of obj2

	obj1Dim = obj1.get_size()
	obj2Dim = obj2.get_size()
	xAxisCollision = False
	yAxisCollision = False

	# Map top left corner of object 1 within object 2's boundries
	for i in range(obj2Dim[0]):
		if obj1Pos[0] == obj2Pos[0] + i:
			xAxisCollision = True
	for i in range(obj2Dim[1]):
		if obj1Pos[1] == obj2Pos[1] + i:
			yAxisCollision = True

	# Map bottom right corner of object 1 within object 2's boundries
	for i in range(obj2Dim[0]):
		if obj1Pos[0] + obj1Dim[0] == obj2Pos[0] + i:
			xAxisCollision = True
	for i in range(obj2Dim[1]):
		if obj1Pos[1] + obj1Dim[1] == obj2Pos[1] + i:
			yAxisCollision = True

	if xAxisCollision and yAxisCollision:
		return True

def relativeLocation(obj1, obj2, obj1Pos, obj2Pos):
	# detect which direction object1 is relative to object2
	# return a string assigned to direction

	location = []
	obj1Dim = obj1.get_size()
	obj2Dim = obj2.get_size()
	TRfurtherRight = 0
	TRfurtherUp = False
	obj1Pos = obj1Pos[0], obj1Pos[1] - 10

	# find whether X is further right or left
	if collision(obj1, obj2, obj1Pos, obj2Pos):
		# left
		if obj1Pos[0] > obj2Pos[0] + obj2Dim[0]/2:
			TRfurtherRight = 2
		# right
		if obj1Pos[0] < obj2Pos[0] + obj2Dim[0]/2:
			TRfurtherRight = 1
	# if object1 Y pos is higher (inverted y so lower num) than object2 Y pos
	if obj1Pos[1] < obj2Pos[1]:
		TRfurtherUp = True

	if TRfurtherUp == True:
		location.append("Above")
	elif TRfurtherUp == False:
		location.append("Below")
	if TRfurtherRight == 1:
		location.append("Right")
	elif TRfurtherRight == 2:
		location.append("Left")

	return location



## Classes
class progressBar:
	def __init__(self, barLen):
		# Progress bar using sys.stdout --- a tool to mod text on the fly
		print("")

		self.barLen = barLen
		self.progress = 0

		# setup toolbar
		sys.stdout.write("[%s]" % (" " * self.barLen))
		sys.stdout.flush()
		sys.stdout.write("\b" * (self.barLen+1)) # return to start of line, after '['

	def update(self):
		self.progress += 1
		# update the bar
		sys.stdout.write("-")
		sys.stdout.flush()

		if self.progress == self.barLen:
			sys.stdout.write("]") # this ends the progress bar

class platform:
	def __init__(self, LenX, LenY, PosX, PosY):
		self.LenX = LenX
		self.LenY = LenY
		self.PosXY = [PosX, PosY]
		self.hitbox = pygame.Surface((self.LenX, self.LenY))
		platforms.append(self)
		self.spriteTick = 0
		self.spriteState = 0
		self.physicalState = "Solid" # "Liquid","Gas"

	def makeSolid(self):
		self.physicalState = "Solid"
	def makeLiquid(self):
		self.physicalState = "Liquid"
	def makeGas(self):
		self.physicalState = "Gas"

	def movePos(self, direction):
		if direction == "Right":
			self.PosXY[0] += 10
		if direction == "Left":
			self.PosXY[0] -= 10
		if direction == "Up":
			self.PosXY[1] -= 10
		if direction == "Down":
			self.PosXY[1] += 10

	def spriteAnimation(self, spriteFolder, mode):
		frames = os.listdir(spriteFolder)
		if mode == "animation":
			self.spriteTick += 1
			if self.spriteState == len(frames):
				self.spriteState = 0
			if self.spriteTick == len(frames)*10:
				self.spriteTick = 0
			if self.spriteTick%10 == 0:
				self.spriteTick += 1
				self.hitbox = pygame.image.load(spriteFolder + "/" + frames[self.spriteState])
				self.hitbox = pygame.transform.scale(self.hitbox, (self.LenX, self.LenY))
				self.spriteState += 1
		if mode == "image":
			self.hitbox = pygame.image.load(spriteFolder + "/" + frames[0])
			self.hitbox = pygame.transform.scale(self.hitbox, (self.LenX, self.LenY))

class checkpoint:
	def __init__(self, PosX, PosY):
		self.PosXY = [PosX, PosY]
		self.hitbox = pygame.Surface((25, 25))
		checkpoints.append(self)

class regionPoint:
	def __init__(self, PosX, PosY):
		self.PosXY = [PosX, PosY]
		self.hitbox = pygame.Surface((25, 25))
		self.Collected = False
		regionpoints.append(self)

class entity:
	def __init__(self, PosX, PosY):
		self.PosXY = [PosX, PosY]
		self.hitbox = pygame.Surface((25, 25))
		self.moveDirection = 1
		self.repellant = self.moveDirection
		entitys.append(self)

	def update(self):
		# Gravity
		if self.PosXY[1] < 610:
			self.PosXY[1] += 10
		elif levelHeight == 0:
			del self
			return
		self.PosXY[0] += self.moveDirection

		# for i in range(2):
		for p in range(len(platforms)):
			if platforms[p].physicalState == "Solid":
				lift = 10
			if platforms[p].physicalState == "Liquid":
				lift = -4
			if platforms[p].physicalState == "Gas":
				lift = 0
			if collision(self.hitbox, platforms[p].hitbox, self.PosXY, platforms[p].PosXY):
				if "Above" in relativeLocation(self.hitbox, platforms[p].hitbox, self.PosXY, platforms[p].PosXY):
					self.PosXY[1] -= lift
				if "Below" in relativeLocation(self.hitbox, platforms[p].hitbox, self.PosXY, platforms[p].PosXY):
					self.PosXY[1] += lift
				if lift == 10:
					if "Right" in relativeLocation(self.hitbox, platforms[p].hitbox, self.PosXY, platforms[p].PosXY):
						self.PosXY[0] -= self.repellant
						self.PosXY[1] -= lift
						self.moveDirection = -self.repellant
					if "Left" in relativeLocation(self.hitbox, platforms[p].hitbox, self.PosXY, platforms[p].PosXY):
						self.PosXY[0] += self.repellant
						self.PosXY[1] -= lift
						self.moveDirection = self.repellant

	#
	#		MOVE DIRECTION IF THERE IS NO PLATFORM BELOW ENTITY
	#
