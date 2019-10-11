episode = 10
M = 10 # number of chromosomes (cadinate solutions)
N = 2 # number of genes (variables)
MaxGen = 75 # number of generation
pc = 0.75 # probability of parent <= change => child
pm = 0.1 # probability of mutation
er = 0.1 # percentage of elite selection
gene_boundary = [[-10, 10], [-1, 1]] # global searching space
fitness_thres = 0.01 # threshold for accepting or reject solution
filter_thres = 0.3 # threshold of identifying duplicated solution

visualization = False