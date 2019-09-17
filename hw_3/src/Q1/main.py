import frbs

def main():
	# ----------------------------------------- preset dicts
    input_func_I = {
        "S" : [[0, 0], [0.25, 1], [0.5, 0]],
        "M" : [[0.25, 0], [0.5, 1], [0.75, 0]],
        "B" : [[0.5, 0], [1, 1]],
    }

    output_func = {
        "SM": [[0, 0], [0.25, 1], [0.5, 0]],
        "L" : [[0.25, 0], [1, 1]]
    }

    # 3 * 2 = 6 rules totoally
    rules = [
        ["S", "then", "SM"],
        #["S", "then", "L"],
        #["M", "then", "SM"],
        ["M", "then", "L"],
        #["B", "then", "SM"],
        ["B", "then", "L"],
    ]

    # -----------------------------------------
    fuzzy = frbs.FRBS(output_func, input_func_I)
    input_I = 0.1
    step_size = 0.001
    output = fuzzy.fuzzification(input_I, fuzzy.memb_func_I)
    print(output)
    X = fuzzy.output_func["SM"].eval_x(1)
    print(X)


    """
    while input_I <= 1:
    	output = fuzzy.fuzzification(input_I, fuzzy.memb_func_I)
    	print(output)
    	input_I += step_size
	"""
if __name__ == '__main__':
    main()

