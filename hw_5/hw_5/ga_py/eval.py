def zero_sort(population):
	fitness_list = list((chromosome.fitness for chromosome in population))
	abs_fitness_list = [abs(ele) for ele in fitness_list] 
	sorted_idx = sorted(range(len(abs_fitness_list)), key=lambda k: abs_fitness_list[k])
	return abs_fitness_list, sorted_idx

def zero_normalize(population):
	fitness_list = list((chromosome.fitness for chromosome in population))
	abs_fitness_list = [abs(ele) for ele in fitness_list]
	weight_away_from_zero = [(1 / (ele - 0)) for ele in abs_fitness_list]
	total_weight = sum(weight_away_from_zero)
	normalized_fitness = [ele/total_weight for ele in weight_away_from_zero]
	sorted_idx = sorted(range(len(normalized_fitness)), key=lambda k: normalized_fitness[k])
	return normalized_fitness, sorted_idx
