import random
from target import Target_Function

class Chromosome(object):
	"""docstring for ClassName"""
	def __init__(self, size_gene, gene_boundary):
		self.gene_boundary = gene_boundary
		self.target = Target_Function()
		self.gene = self.init_gene(size_gene)
		self.fitness = self.target.target_value(self.gene)
		self.normalized_fitness = 0

	def init_gene(self, size_gene):
		gene = []

		for i in range(size_gene):
			boundary = self.gene_boundary[i]
			gene.append(random.uniform(boundary[0], boundary[1]))

		return gene

	def update_fitness(self):
		self.fitness = self.target.target_value(self.gene)

	def mutate_gene(self, gene_indx):
		boundary = self.gene_boundary[gene_indx]
		self.gene[gene_indx] = random.uniform(boundary[0], boundary[1])
