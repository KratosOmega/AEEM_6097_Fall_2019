from GeneticAlgorithm import GeneticAlgorithm
from target import Target_Function

def generate_searching_space(x_space, y_space, z_space, num_step):
	searching_space = [[], [], []]
	x_gap = (x_space[1] - x_space[0]) / num_step
	y_gap = (y_space[1] - y_space[0]) / num_step
	z_gap = (z_space[1] - z_space[0]) / num_step

	x_current = x_space[0]
	y_current = y_space[0]
	z_current = z_space[0]

	for i in range(num_step):
		searching_space[0].append([x_current, x_current + x_gap])
		searching_space[1].append([y_current, y_current + y_gap])
		searching_space[2].append([z_current, z_current + z_gap])

		x_current += x_gap
		y_current += y_gap
		z_current += z_gap

	return searching_space

def main():
	#Problem.obj = @Sphere;
	#Problem.nVar = 20;

	episode = 20

	# number of chromosomes (cadinate solutions)
	M = 20
	# number of genes (variables)
	N = 3
	MaxGen = 50
	Pc = 0.85
	Pm = 0.01
	Er = 0.05

	gene_boundary = [[-5, 5], [-5, 5], [-5, 5]]

	# set to 0 if you do not want the convergence curve 
	visualization = 1

	fitness_thres = 0.01
	coordinate_thres = 0.001

	maxs_mins = []


	for i in range(episode):
		print("ep: ---------------------> ", i)
		BestChrom  = GeneticAlgorithm(M, N, MaxGen, Pc, Pm, Er, gene_boundary, visualization)

		if abs(BestChrom["fitness"]) <= fitness_thres:
			maxs_mins.append(BestChrom)

	for result in maxs_mins:
		print("The best chromosome found: ", result["gene"])
		print("The best fitness value: ", result["fitness"])

if __name__ == '__main__':
    main()
    """
    test = generate_searching_space([-5, 5], [-5, 5], [-5, 5], 5)
    print(test[0])
    print(test[1])
    print(test[2])
	"""