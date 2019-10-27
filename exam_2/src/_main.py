from CONSTANT import *
from utils import *
from GeneticAlgorithm import GeneticAlgorithm
from Chromosome import Chromosome
import numpy as np
from random import *

def main():
	ga = GeneticAlgorithm(M, MaxGen, pc, pm, er, visuailzation)

	result = ga.run()

	print("-------------------------")
	print(result["gene"])
	print(result["fitness"])
	print("-------------------------")


def debug():
	gene = route()
	
	print(gene)
	print(gene.shape)


def print_route():
	result = np.array([
		[0., 0., 0., 0., 1., 0., 0., 0., 0.,],
		[0., 0., 1., 0., 0., 0., 0., 0., 0.,],
		[0., 1., 0., 0., 0., 0., 0., 0., 0.,],
		[0., 0., 0., 0., 0., 1., 0., 0., 0.,],
		[0., 0., 0., 0., 0., 0., 1., 0., 0.,],
		[0., 0., 0., 1., 0., 0., 0., 0., 0.,],
		[0., 0., 0., 0., 0., 0., 0., 1., 0.,],
		[0., 0., 0., 0., 0., 0., 0., 0., 1.,],
		[0., 0., 0., 0., 0., 0., 0., 0., 0.,]
	])

	current = 5
	for i in range(result.shape[0]):
		print(current + 1)
		current = np.where(result[current] == 1)[0][0]




if __name__ == '__main__':
    main() # main run()
    #debug() # testing & generate dataset
    #print_route()

    #show_best_gene()
    #generate_data_csv()


    """
    1. get static data set [80 / 20]
    2. partialy repeatly train on 80%
    3. validate on whole 20%
    """















