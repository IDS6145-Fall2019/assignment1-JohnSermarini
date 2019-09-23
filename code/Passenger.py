import sys
from Position import Position
from PassengerRoute import PassengerRoute

class Passenger:
	def __init__(self, route, enterTime, isWalking, baseSpeed):
		self.route = route
		self.enterTime = enterTime
		self.exitTime = enterTime
		self.isWalking = isWalking
		self.activeWalkway = None
		self.baseSpeed = baseSpeed

	def EnterStation(self):
		return None
		
	def ExitStation(self):
		return None

	def StartWalking(self):
		return None

	def StopWalking(self):
		return None

	def Walk(self):
		return None

	def GetOnWalkway(self, walkway):
		return None

	def GetOffWalkway(self):
		return None

	def GetCurrentPosition(self):
		return None

	def GetSpeed(self):
		return None