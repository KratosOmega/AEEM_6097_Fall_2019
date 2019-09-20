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
        ["x1", "y1"],
        ["x2", "y2"],
        ["x3", "y3"],
        ["x4", "y4"],
        ["x5", "y5"],
    ]

    return input_funcs, output_funcs, rules

def target(x):
    if x >= -1 and x <=-0.8:
        return -0.8
    elif x >= 0.8 and x <= 1:
        return 0.8
    else:
        return x

def main(inp, out):
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.01)
    lb = -1.0
    rb = 1.0
    step_size = 0.01

    X = []
    Y_fuzzy = []
    Y_origin = []

    for i in np.arange(lb, rb, step_size):
        print("============ ", i)
        fuzz = fuzzy.fuzzification(i, fuzzy.input_func_set[inp])
        evaled_rules = fuzzy.rules_eval(fuzz, rules)
        crisp = fuzzy.defuzzification(fuzz, evaled_rules, out)
        X.append(i)
        Y_fuzzy.append(crisp)
        Y_origin.append(target(i))

    plt.plot(X, Y_fuzzy, X, Y_origin)
    plt.show()

    avg_performance = performance(X, Y_fuzzy, Y_origin)
    print(avg_performance)

def debug(inp, out):
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.01)
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
