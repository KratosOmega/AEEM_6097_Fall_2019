from CONSTANT import *
from utils import *
from GeneticAlgorithm import GeneticAlgorithm
from Chromosome import Chromosome
import numpy as np
import random

def main():
    X_train, X_valid = generate_data(dim_size, dim_space, data_size, train_percent)

    ga = GeneticAlgorithm(is_load_gene,
        M, MaxGen, pc, pm, er, 
        X_train, 
        x_prefix, y_prefix, f_prefix, 
        mf_size_in, mf_space_in, mf_size_out, mf_space_out, 
        rand, shuffle_type, visuailzation,
        draw_size,
        mutation_rand,
    )

    result = ga.run()

    print("------------------------------ input X: ")
    for i, x in result["gene"]["input_mf"]["X"].items():
        print(".......... : ", i)
        print(x)
    print("------------------------------ input Y: ")
    for i, y in result["gene"]["input_mf"]["Y"].items():
        print(".......... : ", i)
        print(y)
    print("------------------------------ output F: ")
    for i, f in result["gene"]["output_mf"]["F"].items():
        print(".......... : ", i)
        print(f)
    print("------------------------------ rule matrix: ")
    print(result["gene"]["rule_mat"])
    print("")
    print("========================")
    print(result["fitness"])
    print("========================")

def debug():
    """
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

    save_gene(pop)
    """
    test = load_gene()
    print(test[0].gene)
    




if __name__ == '__main__':
    main()
    #debug()


    """
    1. using sorted population for each generation gonna help?
    """















