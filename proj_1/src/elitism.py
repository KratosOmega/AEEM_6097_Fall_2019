from Chromosome import Chromosome
from eval import zero_sort

def elitism(population, new_population, er):
	size_gene = len(population[0].gene)
	boundary = population[0].gene_boundary
	new_generation = []

	m = len(population)
	elite_size = int(m * er)

	_, sorted_idx = zero_sort(population)

	for k in range(elite_size):
		temp_chromosome = Chromosome(size_gene, boundary)
		temp_chromosome.gene = population[sorted_idx[k]].gene
		temp_chromosome.update_fitness()
		new_generation.append(temp_chromosome)

	for k in range(elite_size, m):
		temp_chromosome = Chromosome(size_gene, boundary)
		temp_chromosome.gene = new_population[k].gene
		temp_chromosome.update_fitness()
		new_generation.append(temp_chromosome)

	return new_generation