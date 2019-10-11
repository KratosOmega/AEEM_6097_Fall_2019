import random
from Chromosome import Chromosome
from eval import zero_normalize

def selection(population):
	size_gene = len(population[0].gene)
	boundary = population[0].gene_boundary
	temp_population = []
	normalized_fitness = []
	num_chromosome = len(population)

	normalized_fitness, sorted_idx = zero_normalize(population)

	for i in range(num_chromosome):
		temp_chromosome = Chromosome(size_gene, boundary)
		temp_chromosome.gene = population[sorted_idx[i]].gene
		temp_chromosome.fitness = population[sorted_idx[i]].fitness
		temp_chromosome.normalized_fitness = normalized_fitness[sorted_idx[i]]
		temp_population.append(temp_chromosome)

	cum_sum = [0] * num_chromosome

	for i in range(num_chromosome):
		cum_sum[i] = sum(p.normalized_fitness for p in temp_population[i : ])

	r = random.uniform(0 ,1)

	parent1_idx = num_chromosome - 1

	for i in range(len(cum_sum)):
		if r > cum_sum[i]:
			parent1_idx = i - 1
			break

	parent2_idx = parent1_idx

	while_loop_stop = 0

	while parent2_idx == parent1_idx:
		while_loop_stop = while_loop_stop + 1
		r = random.uniform(0, 1)
		if while_loop_stop > 20:
			break;

		for i in range(len(cum_sum)):
			if r > cum_sum[i]:
				parent2_idx = i - 1
				break;

	parent1 = temp_population[parent1_idx]
	parent2 = temp_population[parent2_idx]

	return parent1, parent2