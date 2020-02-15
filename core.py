### Functions and Classes that will be used in the program

import pygame
from pygame.locals import *
import subprocess
#from __main__ import platforms
platforms = []
checkpoints = []

## Functions
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
class platform:
	def __init__(self, LenX, LenY, PosX, PosY):
		self.LenX = LenX
		self.LenY = LenY
		self.PosXY = [PosX, PosY]
		self.hitbox = pygame.Surface((self.LenX, self.LenY))
		platforms.append(self)
		self.spriteTick = 0
		self.spriteState = 0

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
		frames = subprocess.getoutput("ls " + spriteFolder)
		frames = frames.split("\n")
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
