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
		p = 999
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
		m_punish = np.array([
			[p, 5, p, 20,4, p, p, 14, p],
			[5, p, 6, p, 7, p, p, p, p],
			[p, 6, p, 15, 10, p, p, p, p],
			[20, p, 15, p, 20, 7, 12, p, p],
			[4, 7, 10, 20, p, 3, 5, 13, 6],
			[p, p, p, 7, 3, p, p, p, p],
			[p, p, p, 12, 5, p, p, 7, p],
			[14, p, p, p, 13, p, 7, p, 5],
			[p, p, p, p, 6, p, p, 5, p],
			])

		m_preset = np.array([
			[0, 5, 0, 20,4, 0, 0, 14, 0],
			[0, 0, 6, 0, 7, 0, 0, 0, 0],
			[0, 6, 0, 15, 10, 0, 0, 0, 0],
			[0, 0, 15, 0, 20, 7, 12, 0, 0],
			[0, 7, 10, 20, 0, 3, 5, 13, 6],
			[0, 0, 0, 7, 3, 0, 0, 0, 0],
			[0, 0, 0, 12, 5, 0, 0, 7, 0],
			[0, 0, 0, 0, 13, 0, 7, 0, 5],
			[0, 0, 0, 0, 0, 0, 0, 0, 0],
			])

		r = {
			0 : [1, 3, 4, 7],
			1 : [0, 2, 4],
			2 : [1, 3, 4],
			3 : [0, 2, 4, 5, 6],
			4 : [0, 1, 2, 3, 5, 6, 7, 8],
			5 : [3, 4],
			6 : [3, 4, 7],
			7 : [0, 4, 6, 8],
			8 : [4, 7],
		}

		route_idx = np.where(self.gene == 1)

		for i in range(len(route_idx[0])):
			distance = m[route_idx[0][i], route_idx[1][i]]
			if distance == 0:# note: 0 means no route connected, it's BAD
				self.fitness = 999
				break
			else:
				self.fitness += distance

	def mutate_gene(self):
		dim = self.gene.shape[0]

		mutated_idx_1 = 0
		mutated_idx_2 = 0

		while mutated_idx_1 == mutated_idx_2:
			mutated_idx_1 = choice(list(range(0, dim-1)))
			mutated_idx_2 = choice(list(range(0, dim-1)))

		temp_1 = copy.deepcopy(self.gene[mutated_idx_1, :])
		temp_2 = copy.deepcopy(self.gene[mutated_idx_2, :])

		self.gene[mutated_idx_1] = temp_2
		self.gene[mutated_idx_2] = temp_1


	def init_route(self):
		gene = np.zeros((9, 9))
		remaining_well = [1, 2, 3, 4, 5, 6, 7, 8]

		for i in range(0, 9 - 1):
			next_well = choice(remaining_well)
			gene[i, next_well] = 1
			remaining_well.remove(next_well)

		return gene



