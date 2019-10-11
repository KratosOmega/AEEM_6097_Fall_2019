import random
from Chromosome import Chromosome

def crossover(parent1 , parent2, pc, crossoverName):
    size_gene = len(parent1.gene)

    boundary = parent1.gene_boundary
    child1 = Chromosome(size_gene, boundary)
    child2 = Chromosome(size_gene, boundary)
    
    gene_len = len(parent1.gene)
    ub = gene_len - 1
    lb = 0

    if crossoverName == "single":
        cross_indx = random.randint(lb + 1, ub)
        
        part1 = parent1.gene[0 : cross_indx]
        part2 = parent2.gene[cross_indx : gene_len]
        child1.gene = part1 + part2
        
        part1 = parent1.gene[0 : cross_indx]
        part2 = parent2.gene[cross_indx : gene_len]
        child2.gene = part1 + part2
        
    if crossoverName == "double":
        cross_indx_1 = random.randint(lb + 1, ub)
        cross_indx_2 = random.randint(lb + 1, ub)
        
        while cross_indx_1 == cross_indx_2:
            cross_indx_2 = random.randint(lb + 1, ub)
        
        if cross_indx_1 > cross_indx_2:
            temp =  cross_indx_1
            cross_indx_1 =  cross_indx_2
            cross_indx_2 = temp

        part1 = parent1.gene[0 : cross_indx_1]
        part2 = parent2.gene[cross_indx_1: cross_indx_2]
        part3 = parent1.gene[cross_indx_2: gene_len]
        child1.gene = part1 + part2 + part3

        part1 = parent2.gene[0 : cross_indx_1]
        part2 = parent1.gene[cross_indx_1: cross_indx_2]
        part3 = parent2.gene[cross_indx_2: gene_len]
        child2.gene = part1 + part2 + part3

    if crossoverName == "continuous":
        for i in range(gene_len):
            beta = random.uniform(0, 1)
            child1.gene[i] = beta * parent1.gene[i] + (1 - beta) * parent2.gene[i]
            child2.gene[i] = (1 - beta) * parent1.gene[i] + beta * parent2.gene[i]

    if random.uniform(0, 1) <= pc:
        child1 = child1
    else:
        child1 = parent1

    if random.uniform(0, 1) <= pc:
        child2 = child2
    else:
        child2 = parent2

    return child1, child2