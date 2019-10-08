from GeneticAlgorithm import GeneticAlgorithm
from target import Target_Function

def main():
	#Problem.obj = @Sphere;
	#Problem.nVar = 20;

	# number of chromosomes (cadinate solutions)
	M = 20
	# number of genes (variables)
	N = 3
	MaxGen = 100
	Pc = 0.85
	Pm = 0.01
	Er = 0.05

	gene_boundary = [[0, 5], [0, 5], [0, 5]]

	# set to 0 if you do not want the convergence curve 
	visualization = 1

	BestChrom  = GeneticAlgorithm(M, N, MaxGen, Pc, Pm, Er, gene_boundary, visualization)

	print("The best chromosome found: ", BestChrom["gene"])
	print("The best fitness value: ", BestChrom["fitness"])

if __name__ == '__main__':
    main()
