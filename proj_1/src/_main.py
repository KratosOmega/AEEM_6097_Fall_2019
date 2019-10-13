from CONSTANT import *
from utils import *
from GeneticAlgorithm import GeneticAlgorithm
from Chromosome import Chromosome
import numpy as np

import random

def main():
    X_train, X_valid = generate_data(dim_size, dim_space, data_size, train_percent)

    ga = GeneticAlgorithm(
        M, MaxGen, pc, pm, er, 
        X_train, 
        x_prefix, y_prefix, f_prefix, 
        mf_size_in, mf_space_in, mf_size_out, mf_space_out, 
        rand, shuffle_type, visuailzation,
        draw_size,
        mutation_rand,
    )

    result = ga.run()

    print(result["gene"])
    print(result["fitness"])

def debug():
    X_train, X_valid = generate_data(dim_size, dim_space, data_size, train_percent)

    ga = GeneticAlgorithm(
        M, MaxGen, pc, pm, er, 
        X_train, 
        x_prefix, y_prefix, f_prefix, 
        mf_size_in, mf_space_in, mf_size_out, mf_space_out, 
        rand, shuffle_type, visuailzation,
        draw_size,
        mutation_rand,
    )

    pop = ga.population
    p1, p2 = ga.selection(pop)

    p1.update_fitness(ga.inp, ga.out)



if __name__ == '__main__':
    main()
    #debug()

