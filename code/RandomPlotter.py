import sys
import numpy as np
import matplotlib.pyplot as plt
import sobol_seq

n = [100, 500, 1000, 2000, 5000]


def main(argv):
	#Plot3_1()
	Plot3_2()


def Plot3_1():
	numRows = 2

	fig = plt.figure(figsize=(20,10))

	for i in range(0, len(n) * numRows):
		x = []
		y = []
		if(i < (len(n) * numRows) / 2): # Psuedo random
			x = np.random.rand(n[i % len(n)])
			y = np.random.rand(n[i % len(n)])
		else: # Quasi random
			seq = sobol_seq.i4_sobol_generate(2, n[i % len(n)])
			for s in seq:
				x.append(s[0])
				y.append(s[1])

		axes = fig.add_subplot(numRows, len(n), i + 1)
		axes.set_aspect(1.)
		axes.set_title("N = " + str(n[i % len(n)]))
		axes.scatter(x, y, s=0.5, c='#dcaa79')

	plt.show()


def Plot3_2():
	numRows = 3

	fig = plt.figure(figsize=(20,10))

	for i in range(0, len(n) * numRows):
		axes = fig.add_subplot(numRows, len(n), i + 1)
		axes.set_aspect(1.)
		axes.set_title("N = " + str(n[i % len(n)]))

		x = []
		y = []
		if(i < (len(n) * numRows) / 3): # Uniform
			x = np.random.uniform(0, 1.0, n[i % len(n)]) * 2.0
			axes.set_xlim([0, 2.0])
			axes.set_ylim([0, 2.0])
		elif(i >= (len(n) * numRows) / 3 and i < 2 * ((len(n) * numRows) / 3)): # Normal
			x = np.random.normal(0, 1.0, n[i % len(n)]) / 3.0
			axes.set_xlim([-1.0, 1.0])
			axes.set_ylim([0, 2.0])
		else: # Logistic
			x = np.random.logistic(0, 1.0, n[i % len(n)]) / 1.0
			axes.set_xlim([-1.0, 1.0])
			axes.set_ylim([0, 2.0])

		axes.hist(x, bins=100, normed=1)

	plt.show()

if __name__ == "__main__":
    main(sys.argv[1:])