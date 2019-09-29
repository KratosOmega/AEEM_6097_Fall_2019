"""
Author: XIN LI
"""
# ---------------------------------- customized libs
import frbs
from utils import updateReport
# ----------------------------------
# ---------------------------------- public libs
import matplotlib.pyplot as plt
import math
import numpy as np
import random
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
# ----------------------------------

def main():
    #######################################################
    ###################### pre-setup ######################
    #######################################################
    # data storing setup
    water_fr = []
    water_lvl = []
    power = []

    # input generating setup
    num_pts_1, num_pts_2 = 5, 5
    segment_num_1, segment_num_2 = 10, 10
    counter = 1
    total = num_pts_1 * num_pts_2 * segment_num_1 * segment_num_2
    #######################################################
    
    # get input data
    input_1, input_2 = get_input_data_segmented(
        0, 4000, 
        0, 160, 
        num_pts_1, num_pts_2, 
        segment_num_1, segment_num_2)
    # get membership function & rules
    input_funcs, output_funcs, rules = get_mf_rule()
    # get FRBS initialized
    _frbs = frbs.FRBS(input_funcs, output_funcs, 0.05)

    # iterate 2-D input data
    for m in input_1:
        for n in input_2:
            # pack input data into dictionary datatype
            x = {
                "water_fr": m,
                "water_lvl": n,
            }
            # fuzzification
            fuzzied = _frbs.fuzzification(x, _frbs.input_func_set)
            # get mu
            evaled_rules = _frbs.rules_eval(fuzzied, rules)
            # defuzzification
            crisp = _frbs.defuzzification(evaled_rules, "power")

            # store input & output data
            water_fr.append(m)
            water_lvl.append(n)
            power.append(crisp)

            # terminal output
            print("Total run: ", total, " -----------> Current @ ", counter)
            # store data into csv for backup
            updateReport("/report.csv", [str(m), str(n), str(crisp)])
            counter += 1
    
    updateReport("/output_dim.csv", [str(len(input_1)), str(len(input_2))])
    plot_3d(water_fr, water_lvl, power, len(input_1), len(input_2))

def get_input_data_segmented(
    input_1_l, input_1_r, 
    input_2_l, input_2_r, 
    num_pts_1, num_pts_2, 
    segment_num_1, segment_num_2):
    input_1 = []
    input_2 = []

    # generate input: Upstream Water Flow Rate
    l = input_1_l
    r = input_1_l
    for m in range(segment_num_1):
        interval = (input_1_r - input_1_l) / segment_num_1
        l = r
        r = l + interval
        for n in range(num_pts_1):
            input_1.append(random.uniform(l, r))
        
    # generate input: Dam Water Level
    l = input_2_l
    r = input_2_l
    for m in range(segment_num_2):
        interval = (input_2_r - input_2_l) / segment_num_2
        l = r
        r = l + interval
        for n in range(num_pts_2):

            input_2.append(random.uniform(l, r))

    return input_1, input_2    

def get_mf_rule():
    input_funcs = {
        "water_fr" : {
            "x1_1" : [[0,0], [0.1, 1], [1000, 0]],
            "x1_2" : [[0,0], [1000, 1], [2000, 0]],
            "x1_3" : [[1000,0], [2000, 1], [3000, 0]],
            "x1_4" : [[2000,0], [3000, 1], [4000, 0]],
            "x1_5" : [[3000,0], [3999.9, 1], [4000, 0]],
        },
        "water_lvl" : {
            "x2_1" : [[0, 0], [0.1, 1], [40, 0]],
            "x2_2" : [[0, 0], [40, 1], [80, 0]],
            "x2_3" : [[40, 0], [80, 1], [120, 0]],
            "x2_4" : [[80, 0], [120, 1], [160, 0]],
            "x2_5" : [[120, 0], [169.9, 1], [170, 0]],
        },
    }

    output_funcs = {
        "power" : {
            "y1_0" : [[-1, 0], [0, 1], [1, 0]],
            "y1_1" : [[0, 0], [0.1, 1], [50, 0]],
            "y1_2" : [[0, 0], [50, 1], [100, 0]],
            "y1_3" : [[50, 0], [110, 1], [170, 0]],
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
        ["water_fr=x1_5+water_lvl=x2_5", "y1_0"],
    ]

    return input_funcs, output_funcs, rules

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

def plot_output(data_path = "./report.csv", dim_path = "./output_dim.csv"):
    water_fr = []
    water_lvl = []
    power = []
    x_size = 0
    y_size = 0

    # read output data
    with open(data_path, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    # read output dimensions
    with open(dim_path, 'r') as f:
        reader = csv.reader(f)
        dims = list(reader)
        x_size = int(dims[0])
        y_size = int(dims[1])

    for d in data:
        water_fr.append(float(d[0]))
        water_lvl.append(float(d[1]))
        power.append(float(d[2]))

    plot_3d(water_fr, water_lvl, power, x_size, y_size)

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

if __name__ == '__main__':
    main()
    #plot_output("./report.csv", "./output_dim.csv")
    #debug()



