from GeneticAlgorithm import GeneticAlgorithm
from target import Target_Function
import random
import math
import numpy as np



def main():
	root = []

	for i in range(episode):
		print("ep: ---------------------> ", i)
		BestChrom  = GeneticAlgorithm(M, N, MaxGen, pc, pm, er, gene_boundary, visualization)

		print(BestChrom)

		if abs(BestChrom["fitness"]) <= fitness_thres:
			BestChrom["gene"][0] = round(BestChrom["gene"][0], 3)
			BestChrom["gene"][1] = round(BestChrom["gene"][1], 3)
			root.append(BestChrom)
			#print("The best chromosome found: ", BestChrom["gene"])
			#print("The best fitness value: ", BestChrom["fitness"])

	filtered_roots = filter_result(root, filter_thres)

	print("==========================")

	for r in filtered_roots:
		print("The best chromosome found: ", r["gene"])
		print("The best fitness value: ", r["fitness"])

if __name__ == '__main__':
	M = 50 # number of chromosomes (cadinate solutions)
	N = 2 # number of genes (variables)
	MaxGen = 10 # number of generation
	pc = 0.85 # probability of parent <= change => child
	pm = 0.1 # probability of mutation
	er = 0.1 # percentage of elite selection
	gene_boundary = [[-50, 50], [-10, 10]] # global searching space
	fitness_thres = 0.01 # threshold for accepting or reject solution
	filter_thres = 0.3 # threshold of identifying duplicated solution

	visualization = True

	BestChrom  = GeneticAlgorithm(M, N, MaxGen, pc, pm, er, gene_boundary, visualization)














