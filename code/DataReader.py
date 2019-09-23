import sys
import csv

fileName = "data.csv"


def main(argv):
	points = []

	with open(fileName, newline='') as csvfile:
		csvReader = csv.reader(csvfile, quotechar='|')	
		for row in csvReader:
			#points.append(row[3])
			csvPoint = row[3] # POINT (x y)
			csvPoint = csvPoint[7:] # x y)
			csvPoint = csvPoint[:-1] # x y
			#print(csvPoint.split(" "))
			i = 0
			x = -1
			y = -1
			for p in csvPoint.split(" "):
				if(i == 0):
					x = p.strip()
				else:
					y = float(p.strip())
				i = i + 1
			print("x: ", x, " ~~~~ y: ", y)

			#x = csvPoint.split(" ")[0]
			#y = csvPoint.split(" ")[1]
			#print("x: ", x, " ~~~~ y: ", y)
			#csvPoints = csvPoint.split(" ")
			#points.append(Point(csvPoints[0], csvPoints[1]))


class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def GetX():
		return self.x

	def GetY():
		return self.y


if __name__ == "__main__":
    main(sys.argv[1:])