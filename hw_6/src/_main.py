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
	print("The best pipeline sequence is: ", result["gene"])
	print("The corresponding total distance is: ", result["fitness"])
	print("-------------------------")

if __name__ == '__main__':
    main()



