from random import *
import numpy as np

def shuffle_single_h(A, B):
	print("--------------------------")
	print(A)
	print(B)
	
	orig_dim = A.shape[0]
	# for exam_2, we remove 1st column and last row
	# after shuffle, we re-added the 1st col and last row
	temp_A = A[:, range(1, orig_dim)][range(0, orig_dim - 1), :]
	temp_B = B[:, range(1, orig_dim)][range(0, orig_dim - 1), :]

	print(temp_A)
	print(temp_B)
	dim = temp_A.shape[0]

	idx = choice(list(range(1, dim-1))) # skip the 1st and last idex to ensure crossover is done

	print(idx)

	top = temp_B[range(idx, dim), :]
	bot = temp_A[range(0, idx), :]
	
	print("0000000")

	print(top)
	print(bot)
	crossed = np.concatenate((top, bot), axis=0)

	print(crossed)

	col_add = np.zeros((dim, 1))

	temp = np.concatenate((col_add, crossed), axis = 1)

	row_add = np.zeros((1, dim+1))
	final_crossed = np.concatenate((temp, row_add), axis = 0)

	print(final_crossed)
	print("--------------------------")

	return final_crossed


if __name__ == '__main__':
	A = np.array([
			[0,1,0,0,0],
			[0,0,1,0,0],
			[0,0,0,1,0],
			[0,0,0,0,1],
			[0,0,0,0,0],
		])
	B = np.array([
			[0,0,0,0,1],
			[0,0,0,1,0],
			[0,0,1,0,0],
			[0,1,0,0,0],
			[0,0,0,0,0],
		])
	test = shuffle_single_h(A, B)








