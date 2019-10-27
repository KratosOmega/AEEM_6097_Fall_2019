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


def map():
	m = np.array([
		[0, 5, 0, 20,4, 0, 0, 14, 0],
		[5, 0, 6, 0, 7, 0, 0, 0, 0],
		[0, 6, 0, 15, 10, 0, 0, 0, 0],
		[20, 0, 15, 0, 20, 7, 12, 0, 0],
		[4, 7, 10, 20, 0, 3, 5, 13, 6],
		[0, 0, 0, 7, 3, 0, 0, 0, 0],
		[0, 0, 0, 12, 5, 0, 0, 7, 0],
		[14, 0, 0, 0, 13, 0, 7, 0, 5],
		[0, 0, 0, 0, 6, 0, 0, 5, 0],
		])

def route():
	p = 999
	gene = np.zeros((9, 9))
	remaining_well = [1, 2, 3, 4, 5, 6, 7, 8]
	m = np.array([
		[0, 5, 0, 20,4, 0, 0, 14, 0],
		[5, 0, 6, 0, 7, 0, 0, 0, 0],
		[0, 6, 0, 15, 10, 0, 0, 0, 0],
		[20, 0, 15, 0, 20, 7, 12, 0, 0],
		[4, 7, 10, 20, 0, 3, 5, 13, 6],
		[0, 0, 0, 7, 3, 0, 0, 0, 0],
		[0, 0, 0, 12, 5, 0, 0, 7, 0],
		[14, 0, 0, 0, 13, 0, 7, 0, 5],
		[0, 0, 0, 0, 6, 0, 0, 5, 0],
		])
	m_punish = np.array([
		[p, 5, p, 20,4, p, p, 14, p],
		[5, p, 6, p, 7, p, p, p, p],
		[p, 6, p, 15, 10, p, p, p, p],
		[20, p, 15, p, 20, 7, 12, p, p],
		[4, 7, 10, 20, p, 3, 5, 13, 6],
		[p, p, p, 7, 3, p, p, p, p],
		[p, p, p, 12, 5, p, p, 7, p],
		[14, p, p, p, 13, p, 7, p, 5],
		[p, p, p, p, 6, p, p, 5, p],
		])

	r = {
		0 : [1, 3, 4, 7],
		1 : [0, 2, 4],
		2 : [1, 3, 4],
		3 : [0, 2, 4, 5, 6],
		4 : [0, 1, 2, 3, 5, 6, 7, 8],
		5 : [3, 4],
		6 : [3, 4, 7],
		7 : [0, 4, 6, 8],
		8 : [4, 7],
	}

	for i in range(0, len(r)-1):
		print(i)
		print(remaining_well)
		next_well = choice(remaining_well)
		gene[i, next_well] = m_punish[i, next_well]
		remaining_well.remove(next_well)

	return gene


if __name__ == '__main__':
    main() # main run()
    #debug() # testing & generate dataset

    #show_best_gene()
    #generate_data_csv()


    """
    1. get static data set [80 / 20]
    2. partialy repeatly train on 80%
    3. validate on whole 20%
    """















