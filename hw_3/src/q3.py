"""
Author: XIN LI
"""

import frbs
import matplotlib.pyplot as plt
import math
import numpy as np

def generate_membership_func():
    num_of_cat = 9
    funcs = {
        "x1" : [[0, 1], [0.01, 0]],
        "x2" : [[0.99, 0], [1, 1]],
    }
    step = 0.005
    init = 0.005

    for i in range(3, num_of_cat+1):
        print(i)
        key = "x" + str(i)
        funcs[key] = [[init - step, 0], [init, 1], [init + step, 0]]
        step = step * 2
        init += step

    return funcs

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
            "x1" : [[-2, 1], [-0.8, 1], [-0.4, 0]],
            "x2" : [[-0.8, 0], [0.4, 1], [0, 0]],
            "x3" : [[-0.4, 0], [0, 1], [0.4, 0]],
            "x4" : [[0, 0], [0.4, 1], [0.8, 0]],
            "x5" : [[0.4, 0], [0.8, 1], [2, 1]],
        },
    }

    output_funcs = {
        "output_1" : {
            "y1": [[-0.9, 1], [-0.8, 1], [-0.4, 0]],
            "y2" : [[-0.8, 0], [-0.4, 1], [0, 0]],
            "y3" : [[-0.4, 0], [0, 1], [0.4, 0]],
            "y4" : [[0, 0], [0.4, 1], [0.8, 0]],
            "y5" : [[0.4, 0], [0.8, 1], [0.9, 1]],
        },
    }

    rules = [
        ["input_1=x1", "y1"],
        ["input_1=x2", "y2"],
        ["input_1=x3", "y3"],
        ["input_1=x4", "y4"],
        ["input_1=x5", "y5"],
    ]

    return input_funcs, output_funcs, rules

def get_hint_data():
    # ----------------------------------------- preset dicts
    input_funcs = {
        "input_1" : {
            "x1" : [[-1.5, 0], [-1.5, 1], [-1, 1], [-0.5, 0]],
            "x2" : [[-1, 0], [-0.5, 1], [0, 0]],
            "x3" : [[-0.5, 0], [0, 1], [0.5, 0]],
            "x4" : [[0, 0], [0.5, 1], [1, 0]],
            "x5" : [[0.5, 0], [1, 1], [1.5, 1], [1.5, 0]],
        },
    }

    output_funcs = {
        "output_1" : {
            "y1": [[-0.9, 0], [-0.9, 1], [-0.8, 1], [-0.5, 0]],
            "y2" : [[-0.8, 0], [-0.5, 1], [0, 0]],
            "y3" : [[-0.5, 0], [0, 1], [0.5, 0]],
            "y4" : [[0, 0], [0.5, 1], [0.8, 0]],
            "y5" : [[0.5, 0], [0.8, 1], [0.9, 1], [0.9, 0]],
        },
    }

    """
    output_funcs = {
        "output_1" : {
            "y1": [[-1.5, 0], [-1.5, 1], [-0.8, 1], [-0.5, 0]],
            "y2" : [[-0.8, 0], [-0.5, 1], [0, 0]],
            "y3" : [[-0.5, 0], [0, 1], [0.5, 0]],
            "y4" : [[0, 0], [0.5, 1], [0.8, 0]],
            "y5" : [[0.5, 0], [0.8, 1], [1.5, 1], [1.5, 0]],
        },
    }
    """

    rules = [
        ["input_1=x1", "y1"],
        ["input_1=x2", "y2"],
        ["input_1=x3", "y3"],
        ["input_1=x4", "y4"],
        ["input_1=x5", "y5"],
    ]

    return input_funcs, output_funcs, rules    

def target(x):
    if x >= -1.5 and x <=-0.8:
        return -0.8
    elif x >= 0.8 and x <= 1.5:
        return 0.8
    else:
        return x

def main():
    # -----------------------------------------
    """
    get_hint_data() using hw given MF and rules
    get_data() using updated MF and rules
    """
    #input_funcs, output_funcs, rules = get_data()
    input_funcs, output_funcs, rules = get_hint_data()
    # -----------------------------------------

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.01)
    lb = -1.5
    rb = 1.5
    step_size = 0.01

    X = []
    Y_fuzzy = []
    Y_origin = []

    for i in np.arange(lb, rb, step_size):
        if i > rb:
            break
        print("============ ", i)
        input_x = {"input_1" : i}
        fuzz = fuzzy.fuzzification(input_x, fuzzy.input_func_set)
        evaled_rules = fuzzy.rules_eval(fuzz, rules)
        crisp = fuzzy.defuzzification(evaled_rules, "output_1")
        X.append(i)
        Y_fuzzy.append(crisp)
        Y_origin.append(target(i))

    plt.plot(X, Y_fuzzy, X, Y_origin)
    plt.show()

    avg_performance = performance(X, Y_fuzzy, Y_origin)
    print(avg_performance)

def debug():
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_hint_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    x = -0.1366
    input_x = {
        "input_1" : x
    }

    fuzz = fuzzy.fuzzification(input_x, fuzzy.input_func_set)
    evaled_rules = fuzzy.rules_eval(fuzz, rules)
    crisp = fuzzy.defuzzification(evaled_rules, "output_1")


    print(x)
    print(fuzz)
    print(evaled_rules)
    print(crisp)

if __name__ == '__main__':
    main()
    #debug()
    """
    - the size of output function determine ...
    """
