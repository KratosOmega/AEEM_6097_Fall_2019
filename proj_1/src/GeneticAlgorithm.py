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
    def __init__(self, is_load_gene,
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
        self.is_load_gene = is_load_gene
        self.M = M
        self.MaxGen = MaxGen
        self.pc = pc
        self.pm = pm
        self.er = er
        self.X = X
        self.draw_size = draw_size
        self.X_random_draw = random_draw(self.X, self.draw_size)
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
        self.best_fitness = 0

    def run(self):
        # grab the 1st fitness
        _, sorted_idx = self.zero_sort(self.population)

        self.best_fitness = self.population[sorted_idx[0]].fitness

        print("Generation : ----------------------- @ (", self.MaxGen, " - ", 0, ")")
        print("fitness --------: ", self.best_fitness)

        for i in sorted_idx:
            print(self.population[i].fitness)
        print("")

        self.cgcurve.append(self.best_fitness)

        # grab the rest fitness
        for g in range (1, self.MaxGen):
            self.X_random_draw = random_draw(self.X, self.draw_size)
            self.inp, self.out = split_XY(self.X_random_draw)
            
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

            # save best genes
            if currnt_fitness < self.best_fitness:
                self.save_gene()

            # ################################################## backup save Gene
            if g % 5 == 0:
                self.save_gene("./_saved_backup/")
                plt.plot(self.cgcurve)
                plt.xlabel('x - generation')
                plt.ylabel('y - fitness')
                plt.title('converging graph')
                plt.savefig('./_plot/plot.png')
            # ################################################## backup save Gene

            # ################################################## Convergence Check
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
            # ################################################## Convergence Check

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
        if self.is_load_gene:
            return self.load_gene()
        else:
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
        """
        print("--------------- Elitism spot check: ")
        print("OLD:")
        for i, p in enumerate(self.population):
            print(i, " - ", p.fitness)
        print("")
        print("NEW")
        for i, p in enumerate(self.new_population):
            print(i, " - ", p.fitness)
        print("")
        """
        new_generation = []

        m = len(self.population)
        elite_size = 1 if int(m * self.er) == 0 else int(m * self.er)

        _, sorted_idx = self.zero_sort(self.population)

        for i in range(elite_size):
            temp_chromosome = copy.deepcopy(self.population[sorted_idx[i]])
            temp_chromosome.update_fitness(self.inp, self.out)
            new_generation.append(temp_chromosome)

        for i in range(elite_size, m):
            temp_chromosome = copy.deepcopy(self.new_population[sorted_idx[i]])
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

    def save_gene(self, output_path = "./_saved/"):
        for p_idx in range(len(self.population)):
            x_data = []
            y_data = []
            f_data = []

            gene = self.population[p_idx].gene
            input_mf_x = gene["input_mf"]["X"]
            input_mf_y = gene["input_mf"]["Y"]
            output_mf_f = gene["output_mf"]["F"]
            rule_mat = gene["rule_mat"]

            x_output_path = output_path + "gene-" + str(p_idx) + "-X.npz"
            for k, e in input_mf_x.items():
                x_data.append(e)
            np.savez(x_output_path, *x_data)

            y_output_path = output_path + "gene-" + str(p_idx) + "-Y.npz"
            for k, e in input_mf_y.items():
                y_data.append(e)
            np.savez(y_output_path, *y_data)

            f_output_path = output_path + "gene-" + str(p_idx) + "-F.npz"
            for k, e in output_mf_f.items():
                f_data.append(e)
            np.savez(f_output_path, *f_data)

            r_output_path = output_path + "gene-" + str(p_idx) + "-R.npz"
            np.savez(r_output_path, rule_mat=rule_mat)

        print("###############################")
        print("###      Gene Is Saved      ###")
        print("###############################")

    def load_gene(self, input_path = "./_saved/"):
        population = []
        input_mf = {}
        output_mf = {}
        rule_mat = None

        for p_idx in range(self.M):
            X = {}
            Y = {}
            F = {}

            chromosome = Chromosome("empty",
                self.x_prefix, self.y_prefix, self.f_prefix,
                self.mf_size_in, self.mf_space_in, self.mf_size_out, self.mf_space_out,
                self.shuffle_type, self.rand)

            x_container = np.load(input_path + "gene-" + str(p_idx) + "-X.npz")
            y_container = np.load(input_path + "gene-" + str(p_idx) + "-Y.npz")
            f_container = np.load(input_path + "gene-" + str(p_idx) + "-F.npz")
            r_container = np.load(input_path + "gene-" + str(p_idx) + "-R.npz")

            x_data = [x_container[i] for i in x_container]
            y_data = [y_container[i] for i in y_container]
            f_data = [f_container[i] for i in f_container]
            rule_mat = r_container["rule_mat"]

            for i, x in enumerate(x_data):
                X[str(i)] = x
            for i, y in enumerate(y_data):
                Y[str(i)] = y
            for i, f in enumerate(f_data):
                F[str(i)] = f

            input_mf["X"] = X
            input_mf["Y"] = Y
            output_mf["F"] = F

            chromosome.gene["input_mf"] = input_mf
            chromosome.gene["output_mf"] = output_mf
            chromosome.gene["rule_mat"] = rule_mat

            chromosome.update_fitness(self.inp, self.out)

            population.append(chromosome)

        print("###############################")
        print("###      Gene Is Loaded     ###")
        print("###############################")

        return population









