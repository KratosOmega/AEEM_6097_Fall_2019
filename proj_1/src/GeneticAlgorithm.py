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
        X,
        x_prefix, 
        y_prefix, 
        f_prefix, 
        mf_size_in, 
        mf_space_in, 
        mf_size_out, 
        mf_space_out, 
        rand,
        shuffle_type,
        visuailzation, 
        draw_size,
        mutation_rand,
        ):

        self.M = M
        self.MaxGen = MaxGen
        self.pc = pc
        self.pm = pm
        self.er = er
        self.X = X
        self.X_random_draw = random_draw(self.X, draw_size)
        self.inp, self.out = split_XY(self.X_random_draw)
        self.x_prefix = x_prefix
        self.y_prefix = y_prefix
        self.f_prefix = f_prefix
        self.mf_size_in = mf_size_in
        self.mf_space_in = mf_space_in
        self.mf_size_out = mf_size_out
        self.mf_space_out = mf_space_out
        self.rand = rand
        self.shuffle_type = shuffle_type
        self.mutation_rand = mutation_rand
        self.visuailzation = visuailzation
        self.population = self.pop_init()
        self.new_population = []
        self.stop_count = 0
        self.prev_fitness = 0
        self.cgcurve = []

    def run(self):
        # grab the 1st fitness
        sorted_fintness_values, sorted_idx = self.zero_sort(self.population)

        print("Generation : ----------------------- @ (", self.MaxGen, " - ", 1, ")")
        print("fitness --------: ", sorted_fintness_values[0])
        for i in sorted_idx:
            print(self.population[i].fitness)
        print("")

        self.cgcurve.append(sorted_fintness_values[0])

        # grab the rest fitness
        for g in range (2, self.MaxGen):
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

            if abs(self.prev_fitness - currnt_fitness) < 0.0001:
                self.stop_count += 1
            else:
                self.stop_count = 0

            self.prev_fitness = currnt_fitness

            for p in self.population:
                print(p.fitness)
            print("")

            # reset new_population

            if self.stop_count > 5:
                #self.rand *= (1 + 0.5)
                self.mutation_rand *= (1 + 0.5)
                self.stop_count = 0

        if self.visuailzation:
            plt.plot(self.cgcurve)
            plt.xlabel('x - generation')
            plt.ylabel('y - fitness')
            plt.title('converging graph')
            plt.show() 

        best_chrom = {
            "gene": self.population[0].gene,
            "fitness": self.population[0].fitness,
        }

        return best_chrom

    def pop_init(self):
        population = []

        for m in range(self.M):
            chromosome = Chromosome(
                None,
                self.x_prefix, self.y_prefix, self.f_prefix, 
                self.mf_size_in, self.mf_space_in, self.mf_size_out, self.mf_space_out, None, self.rand
            )
            chromosome.update_fitness(self.inp, self.out)
            population.append(chromosome)

        return population

    def crossover(self, parent1 , parent2):
        ancestors = [parent1, parent2]

        child1 = Chromosome(ancestors, self.x_prefix, self.y_prefix, self.f_prefix, 
        self.mf_size_in, self.mf_space_in, self.mf_size_out, self.mf_space_out, 
        self.shuffle_type, self.rand)

        child2 = Chromosome(ancestors, self.x_prefix, self.y_prefix, self.f_prefix, 
        self.mf_size_in, self.mf_space_in, self.mf_size_out, self.mf_space_out, 
        self.shuffle_type, self.rand)

        if uniform(0, 1) <= self.pc:
            child1 = child1
        else:
            child1 = parent1

        if uniform(0, 1) <= self.pc:
            child2 = child2
        else:
            child2 = parent2

        child1.update_fitness(self.inp, self.out)
        child1.update_fitness(self.inp, self.out)

        return child1, child2

    def selection(self):
        temp_population = []
        normalized_fitness = []
        num_chromosome = len(self.population)

        normalized_fitness, sorted_idx = self.zero_normalize(self.population)

        for i in range(num_chromosome):
            temp_chromosome = copy.deepcopy(self.population[sorted_idx[i]])
            temp_chromosome.normalized_fitness = normalized_fitness[sorted_idx[i]]
            temp_population.append(temp_chromosome)

        cum_sum = [0] * num_chromosome

        for i in range(num_chromosome):
            cum_sum[i] = sum(p.normalized_fitness for p in temp_population[i : ])

        r = uniform(0 ,1)

        parent1_idx = num_chromosome - 1

        for i in range(len(cum_sum)):
            if r > cum_sum[i]:
                parent1_idx = i - 1
                break

        parent2_idx = parent1_idx

        while_loop_stop = 0

        while parent2_idx == parent1_idx:
            while_loop_stop = while_loop_stop + 1
            r = uniform(0, 1)
            if while_loop_stop > 20:
                break;

            for i in range(len(cum_sum)):
                if r > cum_sum[i]:
                    parent2_idx = i - 1
                    break;

        parent1 = temp_population[parent1_idx]
        parent2 = temp_population[parent2_idx]

        return parent1, parent2

    def mutation(self, child):
        mutated = copy.deepcopy(child)
        if uniform(0, 1) < self.pm:
            #print("-------------------------- rule mutated!")
            mutated.mutate_gene("rule_mat", self.mutation_rand)
        if uniform(0, 1) < self.pm:
            #print("-------------------------- input mutated!")
            mutated.mutate_gene("input_mf", self.mutation_rand)
        if uniform(0, 1) < self.pm:
            #print("-------------------------- output mutated!")
            mutated.mutate_gene("output_mf", self.mutation_rand)

        mutated.update_fitness(self.inp, self.out)

        return mutated

    def elitism(self):
        new_generation = []

        m = len(self.population)
        elite_size = int(m * self.er)

        _, sorted_idx = self.zero_sort(self.population)

        for i in range(elite_size):
            temp_chromosome = copy.deepcopy(self.population[sorted_idx[i]])
            temp_chromosome.update_fitness(self.inp, self.out)
            new_generation.append(temp_chromosome)

        for i in range(elite_size, m):
            temp_chromosome = copy.deepcopy(self.new_population[sorted_idx[i]])
            temp_chromosome.update_fitness(self.inp, self.out)
            new_generation.append(temp_chromosome)

        return new_generation

    def zero_sort(self, population):
        fitness_list = list((chromosome.fitness for chromosome in population))
        abs_fitness_list = [abs(ele) for ele in fitness_list] 
        sorted_idx = sorted(range(len(abs_fitness_list)), key=lambda k: abs_fitness_list[k])
        return abs_fitness_list, sorted_idx

    def zero_normalize(self, population):
        fitness_list = list((chromosome.fitness for chromosome in population))
        abs_fitness_list = [abs(ele) for ele in fitness_list]
        weight_away_from_zero = [(1 / (ele - 0)) for ele in abs_fitness_list]
        total_weight = sum(weight_away_from_zero)
        normalized_fitness = [ele/total_weight for ele in weight_away_from_zero]
        sorted_idx = sorted(range(len(normalized_fitness)), key=lambda k: normalized_fitness[k])
        return normalized_fitness, sorted_idx









