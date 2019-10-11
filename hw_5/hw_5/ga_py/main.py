from GeneticAlgorithm import GeneticAlgorithm
from target import Target_Function
from CONSTANT import *
import random
import math
import numpy as np

def filter_result(root, filter_thres):
	filter_result = []
	add_new = True
	for r in root:
		if len(filter_result) == 0:
			filter_result.append(r)
		else:
			add_new = True
			for i, fr in enumerate(filter_result):
				if abs(fr["gene"][0] - r["gene"][0]) < filter_thres and abs(fr["gene"][1] - r["gene"][1]) < filter_thres:
					add_new = False
					if r["fitness"] < fr["fitness"]:
						filter_result[i] = r
						break
			if add_new:
				filter_result.append(r)

	return filter_result

def protection_zone(r_space, r_num):
	zone = []
	r_gap = (r_space[1] - r_space[0]) / r_num

	r_current = r_space[0]

	for r in range(r_num):
		zone.append([r_current, r_current + r_gap])
		r_current += r_gap

	return zone


def seg_main():
	root = []

	zone = protection_zone(gene_boundary[0], 10)

	for z in zone:
		for i in range(episode):
			BestChrom  = GeneticAlgorithm(M, N, MaxGen, pc, pm, er, [z, gene_boundary[1]], visualization)

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
    #main()
    seg_main()
