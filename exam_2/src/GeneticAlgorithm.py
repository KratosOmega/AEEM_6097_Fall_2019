"""
import matplotlib.pyplot as plt
from crossover import crossover
from selection import selection
from mutation import mutation
from elitism import elitism
"""
from Chromosome import Chromosome
import matplotlib.pyplot as plt
import random
from utils import *
import copy

class GeneticAlgorithm():
    """docstring for ClassName"""
    def __init__(self,
        M, 
        MaxGen, 
        pc, 
        pm, 
        er, 
        visuailzation, 
        ):
        self.M = M
        self.MaxGen = MaxGen
        self.pc = pc
        self.pm = pm
        self.er = er
        self.visuailzation = visuailzation
        self.population = self.pop_init()
        self.new_population = []
        self.cgcurve = []
        self.best_fitness = 0

    def run(self):
        sorted_idx = self.zero_sort(self.population)

        self.best_fitness = self.population[sorted_idx[0]].fitness

        print("Generation : ----------------------- @ (", self.MaxGen, " - ", 0, ")")
        print("fitness --------: ", self.best_fitness)

        for i in sorted_idx:
            print(self.population[i].fitness)
        print("")

        self.cgcurve.append(self.best_fitness)

        # grab the rest fitness
        for g in range (1, self.MaxGen):
            print("Generation : ----------------------- @ (", self.MaxGen, " - ", g, ")")
            self.new_population = []

            for i in range(0, self.M, 2):
                # Selection
                parent1, parent2 = self.selection()

                # Crossover
                child1 , child2 = self.crossover(parent1 , parent2)


                    
                # Mutation
                child1 = self.mutation(child1)
                child2 = self.mutation(child2)
                
                self.new_population.append(child1)
                self.new_population.append(child2)

            # Elitism
            # replace the previous population with the newly made
            self.population = self.elitism()

            currnt_fitness = self.population[0].fitness

            self.cgcurve.append(currnt_fitness)

            print("fitness --------: ", currnt_fitness)

            # ################################################## backup save Gene
            if g % 5 == 0:
                plt.plot(self.cgcurve)
                plt.xlabel('x - generation')
                plt.ylabel('y - fitness')
                plt.title('converging graph')
                plt.savefig('./_plot/plot.png')
            # ################################################## backup save Gene

        if self.visuailzation:
            plt.plot(self.cgcurve)
            plt.xlabel('x - generation')
            plt.ylabel('y - fitness')
            plt.title('converging graph')
            plt.savefig('./_plot/plot.png')

        best_chrom = {
            "gene": self.population[0].gene,
            "fitness": self.population[0].fitness,
            }

        return best_chrom

    def pop_init(self):
        population = []

        for m in range(self.M):
            chromosome = Chromosome()
            chromosome.update_fitness()
            population.append(chromosome)

        return population
            
    def crossover(self, parent1 , parent2):
        # selfcross over
        child1 = Chromosome(parent1)

        child2 = Chromosome(parent2)

        if uniform(0, 1) <= self.pc:
            child1 = child1
        else:
            child1 = parent1

        if uniform(0, 1) <= self.pc:
            child2 = child2
        else:
            child2 = parent2

        child1.update_fitness()
        child1.update_fitness()

        return child1, child2

    def selection(self):
        temp_population = []
        normalized_fitness = []
        sorted_nf = []
        spin_wheel = []
        num_chromosome = len(self.population)
        parent1_idx = -1
        parent2_idx = -1

        normalized_fitness, sorted_idx = self.zero_normalize(self.population)

        for i in range(num_chromosome):
            temp_chromosome = copy.deepcopy(self.population[sorted_idx[i]])
            temp_chromosome.normalized_fitness = normalized_fitness[sorted_idx[i]]
            sorted_nf.append(temp_chromosome.normalized_fitness)
            temp_population.append(temp_chromosome)

        l = 0
        for snf in sorted_nf:
            r = snf + l
            spin_wheel.append([l, r])
            l = r

        r = uniform(0, 1)

        for i, sw in enumerate(spin_wheel):
            if sw[0] < r and r < sw[1]:
                parent1_idx = i
                break
        
        while parent2_idx == -1:
            r = uniform(0, 1)
            for i, sw in enumerate(spin_wheel):
                if i != parent1_idx and (sw[0] < r and r < sw[1]):
                    parent2_idx = i
                    break

        parent1 = temp_population[parent1_idx]
        parent2 = temp_population[parent2_idx]

        return parent1, parent2

    def mutation(self, child):
        mutated = copy.deepcopy(child)
        if uniform(0, 1) < self.pm:
            mutated.mutate_gene()

        mutated.update_fitness()

        return mutated

    def elitism(self):
        new_generation = []

        m = len(self.population)
        elite_size = 1 if int(m * self.er) == 0 else int(m * self.er)

        sorted_idx = self.zero_sort(self.population)

        for i in range(elite_size):
            temp_chromosome = copy.deepcopy(self.population[sorted_idx[i]])
            temp_chromosome.update_fitness()
            new_generation.append(temp_chromosome)

        for i in range(elite_size, m):
            temp_chromosome = copy.deepcopy(self.new_population[sorted_idx[i]])
            new_generation.append(temp_chromosome)

        return new_generation

    def zero_sort(self, population):
        fitness_list = list((chromosome.fitness for chromosome in population))
        sorted_idx = sorted(range(len(fitness_list)), key=lambda k: fitness_list[k])
        return sorted_idx

    def zero_normalize(self, population):
        fitness_list = list((chromosome.fitness for chromosome in population))
        total_weight = sum(fitness_list)
        normalized_fitness = [ele / total_weight for ele in fitness_list]
        sorted_idx = sorted(range(len(normalized_fitness)), key=lambda k: normalized_fitness[k])
        return normalized_fitness, sorted_idx

