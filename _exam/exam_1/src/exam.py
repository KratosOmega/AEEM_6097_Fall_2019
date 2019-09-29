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
import csv

def plot_3d(X, Y, Z, x_size, y_size):
    x = np.reshape(X, (x_size, y_size))
    y = np.reshape(Y, (x_size, y_size))
    z = np.reshape(Z, (x_size, y_size))

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.plot_surface(x, y, z)

    ax.set_xlabel('water_fr')
    ax.set_ylabel('water_lvl')
    ax.set_zlabel('power')

    plt.show()

def get_input_data(num_pts_1, num_pts_2):
    input_1 = []
    input_2 = []

    for i in range(num_pts_1):
        input_1.append(random.uniform(0, 4000)) # Dam Water Level
        
    for i in range(num_pts_2):
        input_2.append(random.uniform(0, 160)) # Upstream Water Flow Rate

    #plt.plot(input_1, input_2)
    #plt.show()

    return input_1, input_2


def get_input_data_segmented(num_pts_1, num_pts_2, segment_num_1, segment_num_2):
    input_1 = []
    input_2 = []

    l = 0
    r = 0
    for m in range(segment_num_1):
        interval = (4000 - 0) / segment_num_1
        l = r
        r = l + interval
        for n in range(num_pts_1):
            input_1.append(random.uniform(l, r)) # Dam Water Level
        
    l = 0
    r = 0
    for m in range(segment_num_2):
        interval = (160 - 0) / segment_num_2
        l = r
        r = l + interval
        for n in range(num_pts_2):
            input_2.append(random.uniform(l, r)) # Upstream Water Flow Rate

    #plt.plot(input_1, input_2)
    #plt.show()

    return input_1, input_2    

def get_mf_rule():
	# ----------------------------------------- preset dicts
    input_funcs = {
        "water_fr" : {
            "x1_1" : [[0,0], [0.1, 1], [1000, 0]],
            "x1_2" : [[890,0], [1400, 1], [2000, 0]],
            "x1_3" : [[1000,0], [2000, 1], [3000, 0]],
            "x1_4" : [[2000,0], [3000, 1], [4000, 0]],
            "x1_5" : [[3000,0], [4000, 1], [4000.1, 0]],
        },
        "water_lvl" : {
            "x2_1" : [[0, 0], [0.1, 1], [42.5, 0]],
            "x2_2" : [[0, 0], [42.5, 1], [85, 0]],
            "x2_3" : [[80, 0], [100, 1], [130, 0]],
            "x2_4" : [[110, 0], [130, 1], [160, 0]],
            "x2_5" : [[140, 0], [170, 1], [170.1, 0]],
        },
    }

    output_funcs = {
        "power" : {
            "y1_1": [[0, 0], [0.1, 1], [55, 0]],
            "y1_2" : [[0, 0], [45, 1], [90, 0]],
            "y1_3" : [[30, 0], [115, 1], [160, 0]],
        },
    }

    rules = [
        ["water_fr=x1_1+water_lvl=x2_1", "y1_1"],
        ["water_fr=x1_1+water_lvl=x2_2", "y1_1"],
        ["water_fr=x1_1+water_lvl=x2_3", "y1_1"],
        ["water_fr=x1_2+water_lvl=x2_1", "y1_1"],
        ["water_fr=x1_2+water_lvl=x2_2", "y1_1"],
        ["water_fr=x1_2+water_lvl=x2_3", "y1_1"],
        ["water_fr=x1_3+water_lvl=x2_1", "y1_1"],
        ["water_fr=x1_3+water_lvl=x2_2", "y1_1"],
        ["water_fr=x1_3+water_lvl=x2_3", "y1_1"],

        ["water_fr=x1_1+water_lvl=x2_4", "y1_1"],
        ["water_fr=x1_1+water_lvl=x2_5", "y1_2"],
        ["water_fr=x1_2+water_lvl=x2_4", "y1_1"],
        ["water_fr=x1_2+water_lvl=x2_5", "y1_2"],
        ["water_fr=x1_3+water_lvl=x2_4", "y1_2"],
        ["water_fr=x1_3+water_lvl=x2_5", "y1_3"],

        ["water_fr=x1_4+water_lvl=x2_1", "y1_2"],
        ["water_fr=x1_4+water_lvl=x2_2", "y1_2"],
        ["water_fr=x1_4+water_lvl=x2_3", "y1_2"],
        
        ["water_fr=x1_5+water_lvl=x2_1", "y1_2"],
        ["water_fr=x1_5+water_lvl=x2_2", "y1_2"],
        ["water_fr=x1_5+water_lvl=x2_3", "y1_2"],

        ["water_fr=x1_4+water_lvl=x2_4", "y1_3"],
        ["water_fr=x1_4+water_lvl=x2_5", "y1_3"],
        ["water_fr=x1_5+water_lvl=x2_4", "y1_3"],
        ["water_fr=x1_5+water_lvl=x2_5", "y1_3"],
    ]


    return input_funcs, output_funcs, rules

def main():
    # -----------------------------------------
    num_pts_1, num_pts_2 = 2, 2
    segment_num_1, segment_num_2 = 10, 10
    counter = 1
    total = num_pts_1 * num_pts_2 * segment_num_1 * segment_num_2
    
    # this is an alternative to segment the domain in order to get data from all coners evenly
    input_1, input_2 = get_input_data_segmented(num_pts_1, num_pts_2, segment_num_1, segment_num_2)
    # this is suit for supercomputer to getnerate huge data to cover all coners
    #input_1, input_2 = get_input_data(num_pts_1, num_pts_2)
    input_funcs, output_funcs, rules = get_mf_rule()

    # !!!: precision in FRBS() need to be adjusted base on input scale
    # ex: for scale of 100+, precision = 0.1 is good
    # ex: for scale of 0 ~ 1, precision = 0.001 is good
    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.05)

    water_fr = []
    water_lvl = []
    power = []

    for m in input_1:
        for n in input_2:
            x = {
                "water_fr": m,
                "water_lvl": n,
            }
            fuzz = fuzzy.fuzzification(x, fuzzy.input_func_set)
            evaled_rules = fuzzy.rules_eval(fuzz, rules)
            crisp = fuzzy.defuzzification(evaled_rules, "power")

            water_fr.append(m)
            water_lvl.append(n)
            power.append(crisp)

            print("Total run: ", total, " -----------> ", counter)
            #print("water_lvl = ", m, " water_fr = ", n, " power = ", crisp)
            updateReport("/report.csv", [str(m), str(n), str(crisp)])
            updateReport("/output_dim", [str(len(input_1)), str(len(input_2))])
            counter += 1

    plot_3d(water_fr, water_lvl, power, len(input_1), len(input_2))

def debug():
    # -----------------------------------------
    # this is an alternative to segment the domain in order to get data from all coners evenly
    #input_1, input_2 = get_input_data_segmented(input_1_size, input_2_size, segment_num_1, segment_num_2)
    # this is suit for supercomputer to getnerate huge data to cover all coners
    #input_1, input_2 = get_input_data(input_1_size, input_2_size)
    input_funcs, output_funcs, rules = get_mf_rule()

    fuzzy = frbs.FRBS(input_funcs, output_funcs, 0.05)

    water_fr = 250
    water_lvl = 150
    power = []

    x = {
        "water_fr": water_fr,
        "water_lvl": water_lvl,
    }

    fuzz = fuzzy.fuzzification(x, fuzzy.input_func_set)
    evaled_rules = fuzzy.rules_eval(fuzz, rules)

    print(evaled_rules)
    crisp = fuzzy.defuzzification(evaled_rules, "power")

    print(x)
    print(crisp)


def plot_output(data_path = "./report.csv", dim_path = "./output_dim.csv"):
    water_fr = []
    water_lvl = []
    power = []
    x_size = 0
    y_size = 0

    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    with open(dim_path, 'r') as f:
        reader = csv.reader(f)
        dims = list(reader)

    for d in data:
        water_fr.append(float(d[0]))
        water_lvl.append(float(d[1]))
        power.append(float(d[2]))

    for d in dims:
        x_size += int(d[0])
        y_size += int(d[1])

    print(x_size)
    print(y_size)

    plot_3d(water_fr, water_lvl, power, x_size, y_size)


if __name__ == '__main__':
    #plot_output("./report.csv", "./output_dim.csv")
    main()
    #debug()
    
    """
    - the size of output function determine ...
    """
