from math import *

x_prefix = "X"
y_prefix = "Y"
f_prefix = "F"

# ------------------------------------------ model setup (this affect the model loading funciton)
M = 10
dim_size = 2
dim_space = [-pi, pi]
train_percent = 0.8
mf_size_in = 4 # num of input mf
mf_space_in = [-pi, pi] # domain of input mf
mf_size_out = 4 # num of output mf
mf_space_out = [-1, 1] # domain of output mf
# ------------------------------------------

# ------------------------------------------ training setup
MaxGen = 100
pc = 0.75
pm = 0.5
er = 0.3

draw_size = 50
data_size = 1600
rand = 0.75
mutation_rand = 0.75
shuffle_type = "random" # h, v, random
visuailzation = True
# ------------------------------------------

is_load_gene = True
#is_load_gene = False