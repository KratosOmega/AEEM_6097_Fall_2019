import random
from frbs import FRBS
from utils import *
from statistics import mean

class Chromosome(object):
	def __init__(self, 
		ancestors, 
		cog_precision,
		x_prefix = "X", y_prefix = "Y", f_prefix = "F", 
		mf_size_in = 0, mf_space_in = [], mf_size_out = 0, mf_space_out =[], 
		shuffle_type = "random", rand = -1):
		#self.target = Target_Function()
		self.cog_precision = cog_precision
		self.x_prefix = x_prefix
		self.y_prefix = y_prefix
		self.f_prefix = f_prefix
		self.mf_size_in = mf_size_in
		self.mf_space_in = mf_space_in
		self.mf_size_out = mf_size_out
		self.mf_space_out = mf_space_out
		self.rand = rand
		self.shuffle_type = shuffle_type
		self.gene = self.init_gene(ancestors)
		self.fitness = 0
		self.normalized_fitness = 0

	def init_gene(self, ancestors):
		input_mf = {}
		output_mf = {}
		rule_mat = {}

		if ancestors == "empty":
			return {}

		elif ancestors == None:
			input_mf = {
				self.x_prefix : init_mf("x", self.mf_size_in, self.mf_space_in, self.rand),
				self.y_prefix : init_mf("y", self.mf_size_in, self.mf_space_in, self.rand),
			}

			output_mf = {
				self.f_prefix : init_mf("f", self.mf_size_out, self.mf_space_out, self.rand),
			}

			rule_mat = init_rule(self.mf_size_in, self.mf_size_in, self.mf_size_out)
		else:
			input_mf = {
				self.x_prefix : inherit_mf("input_mf", "X", ancestors),
				self.y_prefix : inherit_mf("input_mf", "Y", ancestors)
			}

			output_mf = {
				self.f_prefix : inherit_mf("output_mf", "F", ancestors),
			}

			rule_mat = inherit_rule(ancestors, self.shuffle_type)

		gene = {
			"input_mf" : input_mf,
			"output_mf": output_mf,
			"rule_mat" : rule_mat,
		}
		return gene
	
	def update_fitness(self, X, Y):
		diff = []
		input_mf = self.gene["input_mf"]
		output_mf = self.gene["output_mf"]
		rule_mat = self.gene["rule_mat"]

		fuzzy = FRBS(input_mf, output_mf, self.cog_precision)

		for i in range(len(X)):
			x = {
				self.x_prefix : X[i][0],
				self.y_prefix : X[i][1],
			}

			fuzzified_input = fuzzy.fuzzification(x, fuzzy.input_func_set)
			evaled_rules = fuzzy.rule_mat_eval(fuzzified_input, rule_mat)
			crisp = fuzzy.defuzzification(evaled_rules, "F")

			diff.append(abs(crisp - Y[i]))

		avg = mean(diff)

		# loop all the data by using frbs
		self.fitness = avg

	def mutate_gene(self, geneType, mutation_rand):
		if geneType == "rule_mat":
			self.gene[geneType] = init_rule(self.mf_size_in, self.mf_size_in, self.mf_size_out)
		elif geneType == "input_mf":
			self.gene[geneType] = {
				self.x_prefix : init_mf("x", self.mf_size_in, self.mf_space_in, mutation_rand),
				self.y_prefix : init_mf("y", self.mf_size_in, self.mf_space_in, mutation_rand),
			}
		elif geneType == "output_mf":
			self.gene[geneType] = {
				self.f_prefix : init_mf("f", self.mf_size_out, self.mf_space_out, mutation_rand),
			}





