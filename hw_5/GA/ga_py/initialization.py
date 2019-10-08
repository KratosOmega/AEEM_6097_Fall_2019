import random
from Chromosome import Chromosome

def initialization(num_chromosome, num_gene, gene_boundary):
	population = []

	for m in range(num_chromosome):
		chromosome = Chromosome(num_gene, gene_boundary)
		population.append(chromosome)

	return population
