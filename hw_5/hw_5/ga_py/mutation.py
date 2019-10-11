import random

def mutation(child, pm):
	gene_no = len(child.gene)

	for k in range(gene_no):
		r = random.uniform(0, 1)

		if r < pm:
			child.mutate_gene(k)

	return child