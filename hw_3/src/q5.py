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
            "x1" : [[-11, 1], [-10, 1], [-5, 0]],
            "x2" : [[-10, 0], [-5, 1], [0, 0]],
            "x3" : [[-5, 0], [0, 1], [5, 0]],
            "x4" : [[0, 0], [5, 1], [10, 0]],
            "x5" : [[5, 0], [10, 1], [11, 1]],
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
        ["x3", "y1"],
        ["x2-x4", "y2"],
        ["x1-x5", "y3"],
    ]

    return input_funcs, output_funcs, rules

def main(inp, out):
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    lb = -10.0
    rb = 10.0
    step_size = 0.1

    X = []
    Y_fuzzy = []
    Y_origin = []

    for i in np.arange(lb, rb+1, step_size):
        print("============ ", i)
        fuzz = fuzzy.fuzzification(i, fuzzy.input_func_set[inp])
        evaled_rules = fuzzy.rules_eval(fuzz, rules)
        crisp = fuzzy.defuzzification(fuzz, evaled_rules, out)
        X.append(i)
        Y_fuzzy.append(crisp)
        Y_origin.append(math.pow(i, 2))

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
    inp = "input_1"
    out = "output_1"
    main(inp, out)
    #debug(inp, out)
    """
    - the size of output function determine ...
    """
