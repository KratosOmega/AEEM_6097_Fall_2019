from math import *

x_prefix = "X"
y_prefix = "Y"
f_prefix = "F"

# ------------------------------------------ model setup (this affect the model loading funciton)
M = 10
dim_size = 2
dim_space = [-pi, pi]
train_percent = 0.8
mf_size_in = 5 # num of input mf
mf_space_in = [-pi, pi] # domain of input mf
mf_size_out = 5 # num of output mf
mf_space_out = [-1, 1] # domain of output mf
cog_precision = 0.1 #0.01
# ------------------------------------------

# ------------------------------------------ training setup
MaxGen = 500
pc = 0.50
pm = 0.25
er = 0.1

draw_size = 100
data_size = 400
rand = -1#0.50
mutation_rand = 0.25
shuffle_type = "h" # h, v, random
visuailzation = True
# ------------------------------------------

is_load_gene = False
is_train = True

#is_load_gene = True
#is_train = False


