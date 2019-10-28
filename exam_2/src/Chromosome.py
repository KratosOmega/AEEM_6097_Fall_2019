from random import *
from utils import *
from statistics import mean
from math import *
import copy

class Chromosome(object):
	def __init__(self, ancestors = None):
		self.gene = self.init_gene(ancestors)
		self.fitness = 0
		self.normalized_fitness = 0

	def init_gene(self, ancestors):
		gene = None

		if ancestors == None:
			gene = self.init_route()
		else:
			A = copy.deepcopy(ancestors.gene)
			gene = self_shuffle(A)
		
		return gene
	
	def update_fitness(self):
		self.fitness = 0

		m = np.array([
			[0, 5, 0, 20,4, 0, 0, 14, 0],
			[5, 0, 6, 0, 7, 0, 0, 0, 0],
			[0, 6, 0, 15, 10, 0, 0, 0, 0],
			[20, 0, 15, 0, 20, 7, 12, 0, 0],
			[4, 7, 10, 20, 0, 3, 5, 13, 6],
			[0, 0, 0, 7, 3, 0, 0, 0, 0],
			[0, 0, 0, 12, 5, 0, 0, 7, 0],
			[14, 0, 0, 0, 13, 0, 7, 0, 5],
			[0, 0, 0, 0, 6, 0, 0, 5, 0],
			])

		step = len(self.gene) - 1

		for i in range(step):
			distance = m[self.gene[i], self.gene[i+1]]
			if distance == 0:# note: 0 means no route connected, it's BAD
				self.fitness = 999
				break
			else:
				self.fitness += distance

	def mutate_gene(self):
		dim = len(self.gene)

		mutated_idx_1 = 0
		mutated_idx_2 = 0

		while mutated_idx_1 == mutated_idx_2:
			mutated_idx_1 = choice(list(range(0, dim)))
			mutated_idx_2 = choice(list(range(0, dim)))

		temp_1 = copy.deepcopy(self.gene[mutated_idx_1])
		temp_2 = copy.deepcopy(self.gene[mutated_idx_2])

		self.gene[mutated_idx_1] = temp_2
		self.gene[mutated_idx_2] = temp_1


	def init_route(self):
		gene = []
		remaining_well = [0, 1, 2, 3, 4, 5, 6, 7, 8]

		for i in range(0, 9):
			next_well = choice(remaining_well)
			gene.append(next_well)
			remaining_well.remove(next_well)

		return gene



