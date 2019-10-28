from random import *
from math import *
import numpy as np
import copy

def self_shuffle(A):
	dim = len(A)
	idx = choice(list(range(1, dim-1))) # skip the 1st and last idex to ensure crossover is done

	left = A[0:idx]
	right = A[idx:dim]

	new = right + left

	return new
