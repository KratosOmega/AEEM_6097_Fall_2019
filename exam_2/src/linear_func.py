"""
Author: XIN LI
"""

import numpy as np

class Linear_Func():
	def __init__(self, data_points):
		self.data = data_points
		self.memb_func = self.func_builder()
		self.range_map = self.range_dist()

	def range_dist(self):
		range_map = {}

		for i in range(len(self.data) - 1):
			range_map[i] = [self.data[i][0], self.data[i+1][0]]

		return range_map

	def func_builder(self):
		funcs = {}
		X = []
		Y = []
		for pts in self.data:
			X.append(pts[0])
			Y.append(pts[1])

		for i in range(len(self.data) - 1):
			coefficients = np.polyfit([X[i], X[i+1]], [Y[i], Y[i+1]], 1)
			poly = np.poly1d(coefficients)
			funcs[i] = poly

		return funcs

	def eval_y(self, x):
		key = -1

		for k, v in self.range_map.items():
			if x >= v[0] and x <= v[1]:
				key = k

		if key == -1:
			return None
		else:
			return self.memb_func[key](x)

	def eval_x(self, y):
		X = []

		for i, f in self.memb_func.items():
			root = (f - y).r
			X.append(root[0])

		return X














"""
if __name__ == '__main__':
	data_points = [[0, 3], [2, 3], [4, 0]]
	func = Linear_Func(data_points)
	test = func.eval(5)
"""














