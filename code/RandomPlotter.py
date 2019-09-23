import sys
import numpy as np
import matplotlib.pyplot as plt
import sobol_seq

def main(argv):
	n = [100, 500, 1000, 2000, 5000]
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

if __name__ == "__main__":
    main(sys.argv[1:])