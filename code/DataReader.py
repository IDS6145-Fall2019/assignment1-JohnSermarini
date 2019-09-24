import sys
import csv
import numpy
import matplotlib.pyplot as plt

fileName = "data.csv"


def main(argv):
	points = []

	with open(fileName, newline='') as csvfile:
		csvReader = csv.reader(csvfile, quotechar='|')	
		for row in csvReader:
			# Strip Point from csv
			csvPoint = row[3] # POINT (x y)
			csvPoint = csvPoint[7:] # x y)
			csvPoint = csvPoint[:-1] # x y
			split = csvPoint.split(" ")

			# Determine if csv has empty value
			if(len(split) < 2):
				continue

			# Record data
			x = float(split[0])
			y = float(split[1])
			points.append(Point(x, y))

	xSTD = numpy.std([p.GetX() for p in points])
	xMean = numpy.mean([p.GetX() for p in points])
	xMedian = numpy.median([p.GetX() for p in points])
	ySTD = numpy.std([p.GetY() for p in points])
	yMean = numpy.mean([p.GetY() for p in points])
	yMedian = numpy.median([p.GetY() for p in points])

	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Standard Deviation: ")
	print("X: ", xSTD)
	print("Y: ", ySTD)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Mean: ")
	print("X: ", xMean)
	print("Y: ", yMean)
	print("~~~~~~~~~~~~~~~~~~~~~~~~~~~")
	print("Median: ")
	print("X: ", xMedian)
	print("Y: ", yMedian)

	PlotEntrances([p.GetX() for p in points], [p.GetY() for p in points])


def PlotEntrances(x, y):
	fig = plt.figure(figsize=(10,10))
	ax = plt.gca()
	ax.set_aspect(1.)
	ax.set_aspect('equal', adjustable='box')
	ax.set_title("Map of NYC Subway Entrances")
	ax.grid(c='black')
	ax.scatter(x, y, s=10.0, c='#f25746')
	plt.show()


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def GetX(self):
		return self.x

	def GetY(self):
		return self.y


if __name__ == "__main__":
    main(sys.argv[1:])