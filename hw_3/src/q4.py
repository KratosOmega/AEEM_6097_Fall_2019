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

def get_data():
	# ----------------------------------------- preset dicts
    input_funcs = {
        "input_1" : {
            "x1_1" : [[0, 1], [4, 1], [8, 0]],
            "x1_2" : [[4, 0], [7, 1], [10, 1]],
        },
        "input_2" : {
            "x2_1" : [[0,0], [8, 1], [16, 0]],
        }
    }

    output_funcs = {
        "output_1" : {
            "y1_1": [[0, 0], [2, 1], [4, 0]],
            "y1_2" : [[1, 0], [3, 1], [5, 0]],
        },
    }

    rules = [
        ["input_1=x1_1+input_2=x2_1", "y1_1"],
        ["input_1=x1_2+input_2=x2_1", "y1_2"],
    ]

    return input_funcs, output_funcs, rules

def main():
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    lb = 0.0
    rb = 10.0
    step_size = 0.1

    X = []
    Y_fuzzy = []
    Y_origin = []


    for i in np.arange(lb, rb, step_size):
        print("============ ", i)
        input_x = {
            "input_1": i,
            "input_2": 10,
        }
        fuzz = fuzzy.fuzzification(input_x, fuzzy.input_func_set)
        evaled_rules = fuzzy.rules_eval(fuzz, rules, "max_prod_comp")
        crisp = fuzzy.defuzzification(evaled_rules, "output_1")
        X.append(i)
        Y_fuzzy.append(crisp)

    plt.plot(X, Y_fuzzy)
    plt.show()


def debug():
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    input_x = {
        "input_1": 6,
        "input_2": 10,
    }

    fuzz = fuzzy.fuzzification(input_x, fuzzy.input_func_set)
    evaled_rules = fuzzy.rules_eval(fuzz, rules, "max_prod_comp")

    yH = fuzzy.defuzzification(evaled_rules, "output_1")

    print("input_1 = ", input_x["input_1"], ", input_2 = ", input_x["input_2"])
    print("output = ", yH)


if __name__ == '__main__':
    #main()
    debug()
    """
    - the size of output function determine ...
    """
