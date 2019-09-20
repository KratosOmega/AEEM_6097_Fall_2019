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
            "x1" : [[0, 1], [0.01, 0]],
            "x2" : [[0, 0], [0.05, 1], [0.1, 0]],
            "x3" : [[0.05, 0], [0.125, 1], [0.2, 0]],
            "x4" : [[0.125, 0], [0.225, 1], [0.335, 0]],
            "x5" : [[0.225, 0], [0.35, 1], [0.475, 0]],
            "x6" : [[0.35, 0], [0.5, 1], [0.65, 0]],
            "x7" : [[0.5, 0], [0.675, 1], [0.85, 0]],
            "x8" : [[0.675, 0], [0.875, 1], [1, 0]],
            "x9" : [[0.99, 0], [1, 1]],
        },
    }

    output_funcs = {
        "output_1" : {
            "y1" : [[0, 1], [0.01, 0]],
            "y2" : [[0.01, 0], [0.2, 1], [0.4, 0]],
            "y3" : [[0.2, 0], [0.4, 1], [0.6, 0]],
            "y4" : [[0.4, 0], [0.5, 1], [0.6, 0]],
            "y5" : [[0.5, 0], [0.6, 1], [0.7, 0]],
            "y6" : [[0.6, 0], [0.7, 1], [0.8, 0]],
            "y7" : [[0.7, 0], [0.8, 1], [0.9, 0]],
            "y8" : [[0.85, 0], [0.95, 1], [0.99, 1]],
            "y9" : [[0.99, 0], [1, 1]],
        },
    }

    rules = [
        ["input_1=x1", "y1"],
        ["input_1=x2", "y2"],
        ["input_1=x3", "y3"],
        ["input_1=x4", "y4"],
        ["input_1=x5", "y5"],
        ["input_1=x6", "y6"],
        ["input_1=x7", "y7"],
        ["input_1=x8", "y8"],
        ["input_1=x9", "y9"],
    ]

    return input_funcs, output_funcs, rules

def main():
    # -----------------------------------------
    lb = 0.0
    rb = 1.0
    step_size = 0.1

    X = []
    Y_fuzzy = []
    Y_origin = []

    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)

    for i in np.arange(lb, rb+1, step_size):
        if i > rb:
            break
        print("-------------------- ", i)
        input_x = {"input_1" : i}
        fuzz = fuzzy.fuzzification(input_x, fuzzy.input_func_set)
        evaled_rules = fuzzy.rules_eval(fuzz, rules)
        crisp = fuzzy.defuzzification(evaled_rules, "output_1")
        X.append(i)
        Y_fuzzy.append(crisp)
        Y_origin.append(math.pow(i, 0.45))

    plt.plot(X, Y_fuzzy, X, Y_origin)
    plt.show()

    avg_performance = performance(X, Y_fuzzy, Y_origin)
    print(avg_performance)

if __name__ == '__main__':
    main()

