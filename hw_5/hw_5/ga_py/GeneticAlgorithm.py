import matplotlib.pyplot as plt
from initialization import initialization
from crossover import crossover
from Chromosome import Chromosome
from selection import selection
from mutation import mutation
from elitism import elitism
from eval import zero_sort

def GeneticAlgorithm(M, N, MaxGen, pc, pm, er, gene_boundary, visuailzation):
    stop_count = 0
    prev_fitness = 0
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
            child1 , child2 = crossover(parent1 , parent2, pc, 'continuous')
        
            # Mutation
            child1 = mutation(child1, pm)
            child2 = mutation(child2, pm)
        
            child1.update_fitness()
            child2.update_fitness()

            new_population.append(child1)
            new_population.append(child2)

        # Elitism
        new_population = elitism(population, new_population, er)

        currnt_fitness = new_population[0].fitness

        cgcurve.append(currnt_fitness)

        if abs(prev_fitness - currnt_fitness) < 0.0001:
            stop_count += 1
        else:
            stop_count = 0

        prev_fitness = currnt_fitness
        # replace the previous population with the newly made
        population = new_population;

        if stop_count > 15:
            stop_count = 0
            break

    if visuailzation:
        plt.plot(cgcurve)
        plt.xlabel('x - generation')
        plt.ylabel('y - fitness')
        plt.title('converging graph')
        plt.show() 

    best_chrom = {
        "gene": population[0].gene,
        "fitness": population[0].fitness,
    }

    return best_chrom
