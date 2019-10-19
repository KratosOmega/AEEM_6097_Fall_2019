from CONSTANT import *
from utils import *
from GeneticAlgorithm import GeneticAlgorithm
from Chromosome import Chromosome
import numpy as np
import random

def main():
	# ------------------ data action
	data_action = "load"
	#data_action = "generate"
	#data_action = "reset"

	X_train, X_valid = data(data_action)

	ga = GeneticAlgorithm(is_load_gene,
		M, MaxGen, pc, pm, er, 
		X_train,
		X_valid,
		x_prefix, y_prefix, f_prefix, 
		mf_size_in, mf_space_in, mf_size_out, mf_space_out, 
		rand, shuffle_type, visuailzation,
		draw_size,
		mutation_rand,
		is_train,
	)

	result = ga.run()

	if is_train:
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

	else:
		print("---------------------- Validation reult: ")
		print(result)

def debug():
	# ------------------ data action
	#data_action = "generate"
	data_action = "reset"
	data(data_action)

	data_action = "load"
	X_train, X_valid = data(data_action)

	print(X_train)
	print(X_valid)
	print(type(X_train))
	print(X_train.shape)
	print(type(X_valid))
	print(X_valid.shape)

def data(action = "load"):
	if action == "load":
		X_train, X_valid = load_data_csv()
		return np.array(X_train[0]), np.array(X_valid[0])

	if action == "generate":
		return generate_data(dim_size, dim_space, data_size, train_percent)

	if action == "reset":
		generate_data_csv(dim_size, dim_space, data_size, train_percent, "./_data/")

def show_best_gene():
    result = load_gene()
    print(result)
    print("------------------------------ input X: ")
    for i, x in result.gene["input_mf"]["X"].items():
        print(".......... : ", i)
        print(x)
    print("------------------------------ input Y: ")
    for i, y in result.gene["input_mf"]["Y"].items():
        print(".......... : ", i)
        print(y)
    print("------------------------------ output F: ")
    for i, f in result.gene["output_mf"]["F"].items():
        print(".......... : ", i)
        print(f)
    print("------------------------------ rule matrix: ")
    print(result.gene["rule_mat"])
    print("")

def load_gene(input_path = "./_saved/"):
	population = []
	input_mf = {}
	output_mf = {}
	rule_mat = None

	for p_idx in range(M):
		X = {}
		Y = {}
		F = {}

	chromosome = Chromosome("empty",
		x_prefix, y_prefix, f_prefix,
		mf_size_in, mf_space_in, mf_size_out, mf_space_out,
		shuffle_type, -1)

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

	#chromosome.update_fitness(self.inp, self.out)

	print("###############################")
	print("###      Gene Is Loaded     ###")
	print("###############################")

	return chromosome    



if __name__ == '__main__':
    main()
    #debug()
    #show_best_gene()
    #generate_data_csv()


    """
    1. get static data set [80 / 20]
    2. partialy repeatly train on 80%
    3. validate on whole 20%
    """















