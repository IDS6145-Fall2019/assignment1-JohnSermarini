import sys
from Position import Position

class Walkway:
	def __init__(self, basePosition, polarDirection, length, width, speed, isLeftSideForWalking):
		self.basePosition = basePosition
		self.polarDirection = polarDirection
		self.length = length
		self.width = width
		self.speed = speed
		self.isLeftSideForWalking = isLeftSideForWalking

	def GetCost(self):
		return None

		