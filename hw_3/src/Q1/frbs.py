import numpy as np
import matplotlib.pyplot as plt
import linear_func

class FRBS():
    def __init__(self, 
        pts_output,
        pts_input_I, 
        pts_input_II = None, 
        pts_input_III = None):

        self.pts_output = pts_output
        self.pts_input_I = pts_input_I
        self.output_func = self.memb_func_builder(self.pts_output)
        self.memb_func_I = self.memb_func_builder(self.pts_input_I)
        # ------------------------------------------------
        # add more membership functions as needed below
        # ------------------------------------------------
        self.pts_input_II = pts_input_II
        self.pts_input_III = pts_input_III
        self.memb_func_II = None if self.pts_input_II == None else self.memb_func_builder(self.pts_input_II)
        self.memb_func_III = None if self.pts_input_III == None else self.memb_func_builder(self.pts_input_III)


    def memb_func_builder(self, pts):
        memb_funcs = {}

        for k, v in pts.items():
            lf = linear_func.Linear_Func(v)
            memb_funcs[k] = lf

        return memb_funcs

    def fuzzification(self, x, memb_func):
        #degrees = [0] * len(node_list)
        degrees = {}

        for key, func in memb_func.items():
            degrees[key] = func.eval_y(x)
            
        degrees = self.cleaning(degrees)

        return degrees

    def cleaning(self, degrees):
        for k in degrees.keys():
            if degrees[k] != None:
                if degrees[k] > 0.0 and degrees[k] < 1e-10:
                    degrees[k] = None

        return degrees

    def rules_eval(self):
        return False

    def rules_agg(self):
        return False

    def fuzzy_ops(self, op, degrees):
        if op == "1D":
            return max(degrees.values())
        if op == "AND":
            return min(degrees.values())
        elif op == "OR":
            return max(degrees.values())

"""
if __name__ == '__main__':
"""
   


