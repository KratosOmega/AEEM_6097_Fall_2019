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
        },
        "input_2" : {
            "x1" : [[0, 1], [0.01, 0]],
            "x2" : [[0, 0], [0.05, 1], [0.1, 0]],
            "x3" : [[0.05, 0], [0.125, 1], [0.2, 0]],
            "x4" : [[0.125, 0], [0.225, 1], [0.335, 0]],
            "x5" : [[0.225, 0], [0.35, 1], [0.475, 0]],
            "x6" : [[0.35, 0], [0.5, 1], [0.65, 0]],
            "x7" : [[0.5, 0], [0.675, 1], [0.85, 0]],
            "x8" : [[0.675, 0], [0.875, 1], [1, 0]],
            "x9" : [[0.99, 0], [1, 1]],
        }
    }

    output_funcs = {
        "output_1" : {
            "SM": [[0, 0], [0.25, 1], [0.5, 0]],
            "L" : [[0.25, 0], [1, 1]],
            #"test": [[0, 0.1], [0.26, 0.1], [0.27, 0.2], [0.63, 0.2], [0.68, 0.5], [1, 0.5]]
            #"test": [[0, 0.5], [0.5, 0.5], [1, 0]]
        },
        "output_2" : {
            "y1": [[0, 1], [0.01, 1], [0.01, 0]],
            "y2": [[0, 0], [0.1, 1], [0.2, 0]],
            "y3": [[0.1, 0], [0.3, 1], [0.5, 0]],
            "y4": [[0.3, 0], [0.6, 1], [0.9, 0]],
            "y5": [[0.6, 0], [0.8, 1], [1, 0]],
            "y6" : [[0.99, 0], [0.99, 1], [1, 1]],
        }
    }

    # 3 * 2 = 6 rules totoally
    # rules[0] is the input & logic
    # ex: "S,and,M|B"
    # S
    #
    """
    rules = [
        ["S", "SM"],
        #["S", "L"],
        #["M", "SM"],
        ["M", "L"],
        #["B", "SM"],
        ["B", "L"],
    ]
    """
    """
    x is in step of 0.1
    y is in step of 0.2
    """
    rules = [
        ["x1", "y1"],
        ["x9", "y6"],
        ["x2", "y2"],
        ["x3", "y3"],
        ["x4", "y4"],
        ["x5", "y4"],
        ["x6", "y5"],
        ["x7", "y5"],
        ["x8", "y5"],
    ]

    # -----------------------------------------
    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    input_1 = 0
    step_size = 0.01

    X = []
    Y_fuzzy = []
    Y_origin = []

    while input_1 <= 1:
        fuzz = fuzzy.fuzzification(input_1, fuzzy.input_func_set["input_2"])
        evaled_rules = fuzzy.rules_eval(fuzz, rules)
        crisp = fuzzy.defuzzification(fuzz, evaled_rules, "output_2")
        X.append(input_1)
        Y_fuzzy.append(crisp)
        Y_origin.append(math.pow(input_1, 0.45))
        input_1 += step_size

    plt.plot(X, Y_fuzzy, X, Y_origin)
    plt.show()

if __name__ == '__main__':
    main()

