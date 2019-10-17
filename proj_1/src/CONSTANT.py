from math import *

x_prefix = "X"
y_prefix = "Y"
f_prefix = "F"

# ------------------------------------------ model setup (this affect the model loading funciton)
M = 10 #20
dim_size = 2
dim_space = [0.0, 3.14]#[-pi, pi]
train_percent = 0.8
mf_size_in = 3#4 # num of input mf
mf_space_in = [0.0, 3.14]#[-pi, pi] # domain of input mf
mf_size_out = 3#4 # num of output mf
mf_space_out = [-1, 1] # domain of output mf
# ------------------------------------------

# ------------------------------------------ training setup
MaxGen = 500
pc = 0.75
pm = 0.25
er = 0.3

draw_size = 25 #50
data_size = 100
rand = 0.50
mutation_rand = 0.50
shuffle_type = "h" # h, v, random
visuailzation = True
# ------------------------------------------

#is_load_gene = True
is_load_gene = False
