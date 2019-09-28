"""
Author: XIN LI
"""

import frbs
import matplotlib.pyplot as plt
import math
import numpy as np
import random
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from utils import updateReport
from mpl_toolkits.mplot3d import Axes3D


def plot_3d(X, Y, Z, x_size, y_size):
    x = np.reshape(X, (x_size, y_size))
    y = np.reshape(Y, (x_size, y_size))
    z = np.reshape(Z, (x_size, y_size))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z)

    ax.set_xlabel('water_lvl')
    ax.set_ylabel('water_fr')
    ax.set_zlabel('power')

    plt.show()

def get_input_data(input_1_size, input_2_size):
    input_1 = []
    input_2 = []

    for i in range(input_1_size):
        input_1.append(random.uniform(0, 170)) # Dam Water Level
        
    for i in range(input_2_size):
        input_2.append(random.uniform(0, 4000)) # Upstream Water Flow Rate

    #plt.plot(input_1, input_2)
    #plt.show()

    return input_1, input_2


def get_input_data_segmented(input_1_size, input_2_size, segment_num_1, segment_num_2):
    input_1 = []
    input_2 = []

    l = 0
    r = 0
    for m in range(segment_num_1):
        interval = (170 - 0) / segment_num_1
        l = r
        r = l + interval
        for n in range(input_1_size):
            input_1.append(random.uniform(l, r)) # Dam Water Level
        
    l = 0
    r = 0
    for m in range(input_2_size):
        interval = (4000 - 0) / segment_num_1
        l = r
        r = l + interval
        for n in range(input_1_size):
            input_2.append(random.uniform(l, r)) # Upstream Water Flow Rate

    #plt.plot(input_1, input_2)
    #plt.show()

    return input_1, input_2    

def get_mf_rule():
	# ----------------------------------------- preset dicts
    input_funcs = {
        "water_lvl" : {
            "x1_1" : [[-42.5, 0], [0, 1], [42.5, 0]],
            "x1_2" : [[0, 0], [42.5, 1], [85, 0]],
            "x1_3" : [[42.5, 0], [85, 1], [127.5, 0]],
            "x1_4" : [[85, 0], [127.5, 1], [170, 0]],
            "x1_5" : [[127.5, 0], [170, 1], [212.5, 0]],
        },
        "water_fr" : {
            "x2_1" : [[-1000,0], [0, 1], [1000, 0]],
            "x2_2" : [[0,0], [1000, 1], [2000, 0]],
            "x2_3" : [[1000,0], [2000, 1], [3000, 0]],
            "x2_4" : [[2000,0], [3000, 1], [4000, 0]],
            "x2_5" : [[3000,0], [4000, 1], [5000, 0]],
        }
    }

    output_funcs = {
        "power" : {
            "y1_1": [[0, 0], [0.1, 1], [60, 0]],
            "y1_2" : [[0, 0], [60, 1], [120, 0]],
            "y1_3" : [[60, 0], [120, 1], [120.1, 0]],
        },
    }

    rules = [
        ["water_lvl=x1_1+water_fr=x2_1", "y1_1"],
        ["water_lvl=x1_1+water_fr=x2_2", "y1_1"],
        ["water_lvl=x1_1+water_fr=x2_3", "y1_1"],
        ["water_lvl=x1_2+water_fr=x2_1", "y1_1"],
        ["water_lvl=x1_2+water_fr=x2_2", "y1_1"],
        ["water_lvl=x1_2+water_fr=x2_3", "y1_1"],
        ["water_lvl=x1_3+water_fr=x2_1", "y1_1"],
        ["water_lvl=x1_3+water_fr=x2_2", "y1_1"],
        ["water_lvl=x1_3+water_fr=x2_3", "y1_1"],

        ["water_lvl=x1_1+water_fr=x2_4", "y1_2"],
        ["water_lvl=x1_1+water_fr=x2_5", "y1_2"],
        ["water_lvl=x1_2+water_fr=x2_4", "y1_2"],
        ["water_lvl=x1_2+water_fr=x2_5", "y1_2"],
        ["water_lvl=x1_3+water_fr=x2_4", "y1_2"],
        ["water_lvl=x1_3+water_fr=x2_5", "y1_2"],

        ["water_lvl=x1_4+water_fr=x2_1", "y1_2"],
        ["water_lvl=x1_4+water_fr=x2_2", "y1_2"],
        ["water_lvl=x1_4+water_fr=x2_3", "y1_2"],
        ["water_lvl=x1_5+water_fr=x2_1", "y1_2"],
        ["water_lvl=x1_5+water_fr=x2_2", "y1_2"],
        ["water_lvl=x1_5+water_fr=x2_3", "y1_2"],

        ["water_lvl=x1_4+water_fr=x2_4", "y1_3"],
        ["water_lvl=x1_4+water_fr=x2_5", "y1_3"],
        ["water_lvl=x1_5+water_fr=x2_4", "y1_3"],
        ["water_lvl=x1_5+water_fr=x2_5", "y1_3"],
    ]

    return input_funcs, output_funcs, rules

def main():
    # -----------------------------------------
    input_1_size, input_2_size = 10, 10
    segment_num_1, segment_num_2 = 10, 10
    # this is an alternative to segment the domain in order to get data from all coners evenly
    input_1, input_2 = get_input_data_segmented(input_1_size, input_2_size, segment_num_1, segment_num_2)
    # this is suit for supercomputer to getnerate huge data to cover all coners
    #input_1, input_2 = get_input_data(input_1_size, input_2_size)
    input_funcs, output_funcs, rules = get_mf_rule()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)

    water_lvl = []
    water_fr = []
    power = []

    for m in input_1:
        for n in input_2:
            x = {
                "water_lvl": m,
                "water_fr": n,
            }
            fuzz = fuzzy.fuzzification(x, fuzzy.input_func_set)
            evaled_rules = fuzzy.rules_eval(fuzz, rules)
            crisp = fuzzy.defuzzification(evaled_rules, "power")

            water_lvl.append(m)
            water_fr.append(n)
            power.append(crisp)

            print("water_lvl = ", m, " water_fr = ", n, " power = ", crisp)
            updateReport("/report.csv", [str(m), str(n), str(crisp)])

    plot_3d(water_lvl, water_fr, power, input_1_size, input_2_size)

    #plt.plot(X, Y_fuzzy)
    #plt.show()

    """
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # prepare data.
    water_lvl = np.asarray(water_lvl)
    water_fr = np.asarray(water_fr)
    power = np.asarray(power)
    water_lvl, water_fr = np.meshgrid(water_lvl, water_fr)

    # Plot the surface.
    surf = ax.plot_surface(water_lvl, water_fr, power, cmap=cm.coolwarm,
                           linewidth=0, antialiased=False)
    plt.show()
    """

def debug():
    # -----------------------------------------
    input_1, input_2 = get_input_data(10)
    input_funcs, output_funcs, rules = get_mf_rule()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.001)

    water_lvl = 40
    water_fr = 3500
    power = []

    x = {
        "water_lvl": water_lvl,
        "water_fr": water_fr,
    }

    fuzz = fuzzy.fuzzification(x, fuzzy.input_func_set)
    evaled_rules = fuzzy.rules_eval(fuzz, rules)

    print(evaled_rules)
    crisp = fuzzy.defuzzification(evaled_rules, "power")

    print(water_lvl)
    print(water_fr)
    print(crisp)

if __name__ == '__main__':
    main()
    #debug()
    
    """
    - the size of output function determine ...
    """
