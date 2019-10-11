class Target_Function(object):
	def target_value(self, gene):
		x = complex(gene[0],gene[1])
		fitness_value = ((x ** 5) + 7 * (x ** 4) + 6 * (x ** 3) - 4 * (x ** 2) - 3 * (x ** 1) + 2) * 0.01

		fitness_value = abs(fitness_value)
		
		return fitness_value