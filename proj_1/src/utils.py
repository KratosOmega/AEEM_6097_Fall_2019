from random import *
from math import *
import numpy as np
import copy


def target_function(data):
	# F(x, y) = sin(x) * cos(y)
	return sin(data[0]) * cos(data[1])

def generate_data(dim_size, dim_space, data_size, train_percent):
	XY = []

	# ---------------------------------------------------- data generation
	for i in range(data_size):
		pt = []
		for d in range(dim_size):
			pt.append(uniform(dim_space[0], dim_space[1]))
		t_val = target_function(pt)
		pt.append(t_val)
		XY.append(pt)

	# ---------------------------------------------------- data split
	split_at = int(data_size *  train_percent)

	X_train = np.array(XY[:split_at])
	X_valid = np.array(XY[split_at:])

	return X_train, X_valid

def init_mf(mf_prefix, mf_size, mf_space, rand = -1):
    mf = {}
    step = (mf_space[1] - mf_space[0]) / (mf_size - 1)
    l = mf_space[0] - step
    m = l
    r = l

    for i in range(mf_size):
    	m = l + step
    	r = m + step
    	#mf[mf_prefix + str(i)] = [[l, 0], [m, 1], [r, 0]]
    	mf[str(i)] = np.array([[l, 0], [m, 1], [r, 0]])
    	l = m

    # rand = -1, no randomness
    # rand in [0, 1], introduce different degrees of randomness
    if rand != -1:
    	for i in range(1, mf_size - 1):
    		node_setup = mf[str(i)]
    		for node in node_setup:
    			rand_scalar = uniform(-1 * rand, rand)
    			node[0] = node[0] * (1 + rand_scalar)

    return mf

def init_rule(x_size, y_size, f_size):
	rule_mat = np.zeros((x_size, y_size))

	for x in range(x_size):
		for y in range(y_size):
			rule_mat[x, y] = randrange(f_size)

	return rule_mat

def inherit_mf(mfType, geneType, ancestors):
	comb_gene = {}
	# copy gene without reference
	gene1 = ancestors[0].gene[mfType][geneType]
	gene2 = ancestors[1].gene[mfType][geneType]

	keys = gene1.keys()

	for k in keys:
		beta = uniform(0, 1)
		gene1_cp = copy.deepcopy(gene1[k])
		gene2_cp = copy.deepcopy(gene2[k])
		gene1_cp[:,0] *= beta
		gene2_cp[:,0] *= (1 - beta)
		comb_gene[k] = np.vstack((gene1_cp[:,0] + gene2_cp[:,0], gene1_cp[:,1])).T

	return comb_gene

def inherit_rule(ancestors, shuffle_type):
	A = copy.deepcopy(ancestors[0].gene["rule_mat"])
	B = copy.deepcopy(ancestors[1].gene["rule_mat"])

	if shuffle_type == "v":
		return shuffle_v(A, B)
	elif shuffle_type == "h":
		return shuffle_h(A, B)
	elif shuffle_type == "random":
		return shuffle_random(A, B)

def random_draw(data, draw_size):
	idx = np.random.randint(data.shape[0], size = draw_size)
	return data[idx, :]

def split_XY(data):
	X = data[: , [1, -2]]
	Y = data[:, -1]
	return X, Y

def shuffle_h(A, B):
	shape = A.shape
	shuffled = np.ndarray(shape=shape)

	for r in range(shape[0]):
		if (r % 2) == 0:
			shuffled[r, :] = A[r, :]
		else:
			shuffled[r, :] = B[r, :]

	return shuffled

def shuffle_v(A, B):
	shape = A.shape
	shuffled = np.ndarray(shape=shape)

	for c in range(shape[1]):
		if (c % 2) == 0:
			shuffled[:, c] = A[:, c]
		else:
			shuffled[:, c] = B[:, c]

	return shuffled

def shuffle_random(A, B):
	shape = A.shape
	shuffled = np.ndarray(shape=shape)

	for r in range(shape[0]):
		for c in range(shape[1]):
			if uniform(0, 1) < 0.5:
				shuffled[r, c] = A[r, c]
			else:
				shuffled[r, c] = B[r, c]
	return shuffled


def generate_data_csv(dim_size, dim_space, data_size, train_percent, output_path = "./_data/"):
	X_train, X_valid = generate_data(dim_size, dim_space, data_size, train_percent)

	train_output_path = output_path + "train.npz"
	np.savez(train_output_path, X_train)

	valid_output_path = output_path + "valid.npz"
	np.savez(valid_output_path, X_valid)

	print("###############################")
	print("###      Data Is Saved      ###")
	print("###############################")


def load_data_csv(load_path = "./_data/"):

	train = np.load(load_path + "train.npz")
	valid = np.load(load_path + "valid.npz")
	X_train = [train[i] for i in train]
	X_valid = [valid[i] for i in valid]

	return X_train, X_valid






