from math import pow

class Target_Function(object):
	def target_value(self, gene):
		x = gene[0]
		y = gene[1]
		z = gene[2]
		# gene = [x, y, z]
		fitness_value = 30 * pow(x, 2) * y * z + 23 * pow(y, 3) * z - 23 * pow(x, 4) * y
		return fitness_value	
