from initialization import initialization
from crossover import crossover
from Chromosome import Chromosome
from selection import selection
from mutation import mutation
from elitism import elitism
from eval import zero_sort

def GeneticAlgorithm(M, N, MaxGen, Pc, Pm, Er, gene_boundary, visuailzation):
    cgcurve = []

    # Initialization
    population = initialization(M, N, gene_boundary)
    new_population = []
    
    # grab the 1st fitness
    sorted_fintness_values, sorted_indx = zero_sort(population)

    cgcurve.append(sorted_fintness_values[0])

    # grab the rest fitness
    for g in range (2, MaxGen):
        for i in range (M):
            population[i].update_fitness()

        for i in range(0, M, 2):
            # Selection
            parent1, parent2 = selection(population)
            
            # Crossover
            child1 , child2 = crossover(parent1 , parent2, Pc, 'single')
        
            # Mutation
            child1 = mutation(child1, Pm)
            child2 = mutation(child2, Pm)
        
            child1.update_fitness()
            child2.update_fitness()

            new_population.append(child1)
            new_population.append(child2)

        # Elitism
        new_population = elitism(population, new_population, Er)

        population = new_population; # replace the previous population with the newly made

    best_chrom = {
        "gene": population[0].gene,
        "fitness": population[0].fitness,
    }

    return best_chrom
