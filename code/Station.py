import sys
from Passenger import Passenger
from Walkway import Walkway

def main(argv):
	##################################################################################
	# Used only by main for randomization
	# Wasn't sure if y'all wanted me to make another class to house the main stuff 
	from Position import Position
	from PassengerRoute import PassengerRoute
	##################################################################################

	# Random routes
	route1 = PassengerRoute([Position(0, 0, 0), Position(0, 0, 0), Position(0, 0, 0)])
	print("Route1: ", type(route1))
	route2 = PassengerRoute([Position(0, 0, 0), Position(0, 0, 0), Position(0, 0, 0)])
	print("Route2: ", type(route2))

	# Random passengers
	passenger1 = Passenger(route1, 0, True, 5.0)
	print("Passenger1: ", type(passenger1))
	passenger2 = Passenger(route1, 0, True, 7.0)
	print("Passenger2: ", type(passenger2))
	passenger3 = Passenger(route2, 0, True, 5.0)
	print("Passenger3: ", type(passenger3))

	# Random walkway
	walkway1 = Walkway(Position(0, 0, 0), 0, 3, 2, 4.0, True)
	print("Walkway1: ", type(walkway1))

	station = Station()
	station.PassengerEnter(passenger1)
	station.PassengerEnter(passenger2)
	station.PassengerEnter(passenger3)
	station.AddWalkway(walkway1)
	print("Station: ", type(station))

class Station:
	activePassengers = []
	exitedPassengers = []
	walkways = []

	def __init__(self):
		pass

	def PassengerEnter(self, Passenger):
		return None

	def PassengerExit(self, Passenger):
		return None

	def GetTotalTimeSpent(self):
		return None

	def GetTotalCost(self):
		return None

	def AddWalkway(self, walkway):
		return None

	def RemoveWalkway(self, walkway):
		return None

	def AdvanceTime(self):
		return None

if __name__ == "__main__":
    main(sys.argv[1:])