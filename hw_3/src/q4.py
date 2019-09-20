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
            "x1_1" : [[0, 0], [4, 1], [9, 0]],
            "x1_2" : [[4, 0], [7, 1], [10, 0]],
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
    lb = -10.0
    rb = 10.0
    step_size = 0.1

    X = []
    Y_fuzzy = []
    Y_origin = []


    for i in np.arange(lb, rb+1, step_size):
        print("============ ", i)
        fuzz = fuzzy.fuzzification(i, fuzzy.input_func_set)
        evaled_rules = fuzzy.rules_eval(fuzz, rules)
        crisp = fuzzy.defuzzification(fuzz, evaled_rules, out)
        X.append(i)
        Y_fuzzy.append(crisp)
        Y_origin.append(math.pow(i, 2))

    plt.plot(X, Y_fuzzy, X, Y_origin)
    plt.show()

    avg_performance = performance(X, Y_fuzzy, Y_origin)
    print(avg_performance)

def debug():
    # -----------------------------------------
    input_funcs, output_funcs, rules = get_data()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)
    input_x = {
        "input_1": 6,
        "input_2": 10,
    }

    fuzz = fuzzy.fuzzification(input_x, fuzzy.input_func_set)
    evaled_rules = fuzzy.rules_eval(fuzz, rules)


    print(evaled_rules)


    yH = fuzzy.defuzzification(evaled_rules, "output_1")

    print(yH)
    print("------------")


if __name__ == '__main__':
    #main()
    debug()
    """
    - the size of output function determine ...
    """
