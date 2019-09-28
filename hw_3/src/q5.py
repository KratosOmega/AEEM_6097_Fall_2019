"""
Author: XIN LI
"""

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

def get_hint_data():
    # ----------------------------------------- preset dicts
    input_funcs = {
        "input_1" : {
            "x1_1" : [[-4, 1], [-2, 0], [2, 0], [4, 1]],
            "x1_2" : [[-4, 0], [-2, 1], [0, 0], [2, 1], [4, 0]],
            "x1_3" : [[-2, 0], [0, 1], [2, 0]]
        },
    }

    output_funcs = {
        "output_1" : {
            "y1_1" : [[4, 0], [8, 1]],        
            "y1_2" : [[0, 0], [4, 1], [8, 0]],
            "y1_3": [[0, 1], [4, 0]],
        },
    }

    rules = [
        ["input_1=x1_1", "y1_1"],
        ["input_1=x1_2", "y1_2"],
        ["input_1=x1_3", "y1_3"],
    ]

    return input_funcs, output_funcs, rules

def get_data():
	# ----------------------------------------- preset dicts
    input_funcs = {
        "input_1" : {
            "x1_1" : [[-4, 1], [-2, 0], [2, 0], [4, 1]],
            "x1_2" : [[-4, 0], [-1, 1], [0, 0], [1, 1], [4, 0]],
            "x1_3" : [[-4, 0], [0, 1], [4, 0]]
        },
    }

    output_funcs = {
        "output_1" : {
            "y1_1" : [[7, 0], [8, 1]],        
            "y1_2" : [[3.9, 0], [4, 1], [4.1, 0]],
            "y1_3": [[0, 1], [1, 0]],
        },
    }

    rules = [
        ["input_1=x1_1", "y1_1"],
        ["input_1=x1_2", "y1_2"],
        ["input_1=x1_3", "y1_3"],
    ]

    return input_funcs, output_funcs, rules

def main():
    # -----------------------------------------
    """
    get_hint_data() using hw given MF and rules
    get_data() using updated MF and rules
    """
    #input_funcs, output_funcs, rules = get_data()
    input_funcs, output_funcs, rules = get_hint_data()
    # -----------------------------------------

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    lb = -4.0
    rb = 4.0
    step_size = 0.01

    X = []
    Y_fuzzy = []
    Y_origin = []

    for i in np.arange(lb, rb+1, step_size):
        if i > rb:
            break
        print("============ ", i)
        input_x = {"input_1" : i}
        fuzz = fuzzy.fuzzification(input_x, fuzzy.input_func_set)
        evaled_rules = fuzzy.rules_eval(fuzz, rules)
        crisp = fuzzy.defuzzification(evaled_rules, "output_1")
        X.append(i)
        Y_fuzzy.append(crisp)
        Y_origin.append(math.pow(i, 2)/2)

    plt.plot(X, Y_fuzzy, X, Y_origin)
    plt.show()

    avg_performance = performance(X, Y_fuzzy, Y_origin)
    print(avg_performance)

def debug(inp, out):
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    input_1 = 0.99

    fuzz = fuzzy.fuzzification(input_1, fuzzy.input_func_set[inp])
    evaled_rules = fuzzy.rules_eval(fuzz, rules)
    yH = fuzzy.defuzzification(fuzz, evaled_rules, out)
    yT = math.pow(input_1, 0.45)

    print(input_1)
    print(yH)
    print(yT)
    print("------------")
    print(evaled_rules)


if __name__ == '__main__':
    main()
    #debug(inp, out)
    """
    - the size of output function determine ...
    """
