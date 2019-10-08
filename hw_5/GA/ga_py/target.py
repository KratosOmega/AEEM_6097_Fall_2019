from math import pow

class Target_Function(object):
	def target_value(self, gene):
		x = gene[0]
		y = gene[1]
		z = gene[2]
		# gene = [x, y, z]
		fitness_value = 30 * pow(x, 2) * y * z + 23 * pow(y, 3) * z - 23 * pow(x, 4) * y
		return fitness_value

	def dx(self, gene):
		x = gene[0]
		y = gene[1]
		z = gene[2]
		# gene = [x, y, z]
		fitness_value = 60 * x * y * z - 92 * pow(x, 3) * y
		return fitness_value

	def dy(self, gene):
		x = gene[0]
		y = gene[1]
		z = gene[2]
		# gene = [x, y, z]
		fitness_value = 30 * pow(x, 2) * z + 69 * pow(y, 2) * z - 23 * pow(x, 4)
		return fitness_value

	def dz(self, gene):
		x = gene[0]
		y = gene[1]
		z = gene[2]
		# gene = [x, y, z]
		fitness_value = 30 * pow(x, 2) * y + 23 * pow(y, 3)
		return fitness_value				


