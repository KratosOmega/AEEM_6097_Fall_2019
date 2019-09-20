import frbs
import matplotlib.pyplot as plt
import math
import numpy as np

def performance(X, Yh, Yt):
    deviations = []
    diffs = []
    for i in range(len(X)):
        deviations.append(Yh[i] - Yt[i])
        diffs.append(abs(Yh[i] - Yt[i]))

    plt.plot(X, deviations)

    avg =  sum(diffs) / len(diffs)
    return avg

def get_data():
	# ----------------------------------------- preset dicts
    input_funcs = {
        "input_1" : {
            "x1" : [[-11, 1], [-10, 1], [-5, 0], [5, 0], [10, 1], [11, 1]],
            "x2" : [[-10, 0], [-5, 1], [0, 0], [5, 1], [10, 0]],
            "x3" : [[-5, 0], [0, 1], [5, 0]],
        },
    }

    output_funcs = {
        "output_1" : {
            "y1": [[0, 1], [25, 0]],
            "y2" : [[0, 0], [25, 1], [100, 0]],
            "y3" : [[25, 0], [100, 1]],
        },
    }

    rules = [
        ["input_1=x1", "y3"],
        ["input_1=x2", "y2"],
        ["input_1=x3", "y1"],
    ]

    return input_funcs, output_funcs, rules

def main():
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    lb = -10.0
    rb = 10.0
    step_size = 1

    X = []
    Y_fuzzy = []
    Y_origin = []

    for i in np.arange(lb, rb, step_size):
        if i > rb:
            break
        input_x = {"input_1" : i}
        print("============ ", i)
        fuzz = fuzzy.fuzzification(input_x, fuzzy.input_func_set)
        evaled_rules = fuzzy.rules_eval(fuzz, rules)
        crisp = fuzzy.defuzzification(evaled_rules, "output_1")
        X.append(i)
        Y_fuzzy.append(crisp)
        Y_origin.append(math.pow(i, 2))

    plt.plot(X, Y_fuzzy, X, Y_origin)
    plt.show()

    avg_performance = performance(X, Y_fuzzy, Y_origin)
    print(avg_performance)

if __name__ == '__main__':
    main()
    #debug(inp, out)
    """
    - the size of output function determine ...
    """

