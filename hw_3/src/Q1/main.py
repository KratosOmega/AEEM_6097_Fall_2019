import frbs
import matplotlib.pyplot as plt
import math

def main():
	# ----------------------------------------- preset dicts
    input_funcs = {
        "input_1" : {
            "S" : [[0, 0], [0.25, 1], [0.5, 0]],
            "M" : [[0.25, 0], [0.5, 1], [0.75, 0]],
            "B" : [[0.5, 0], [1, 1]],
        }
    }

    output_funcs = {
        "output_1" : {
            "SM": [[0, 0], [0.25, 1], [0.5, 0]],
            "L" : [[0.25, 0], [1, 1]],
            #"test": [[0, 0.1], [0.26, 0.1], [0.27, 0.2], [0.63, 0.2], [0.68, 0.5], [1, 0.5]]
            #"test": [[0, 0.5], [0.5, 0.5], [1, 0]]
        }
    }

    # 3 * 2 = 6 rules totoally
    # rules[0] is the input & logic
    # ex: "S,and,M|B"
    # S
    # 
    rules = [
        ["S", "SM"],
        ["S", "L"],
        ["M", "SM"],
        ["M", "L"],
        ["B", "SM"],
        ["B", "L"],
    ]

    # -----------------------------------------
    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    input_1 = 0
    step_size = 0.01

    X = []
    Y_fuzzy = []
    Y_origin = []

    while input_1 <= 1:
        fuzz = fuzzy.fuzzification(input_1, fuzzy.input_func_set["input_1"])
        crisp = fuzzy.defuzzification(fuzz, rules)
        X.append(input_1)
        Y_fuzzy.append(crisp)
        Y_origin.append(math.pow(input_1, 0.45))
        input_1 += step_size

    plt.plot(X, Y_fuzzy, X, Y_origin)
    plt.show()

if __name__ == '__main__':
    main()

