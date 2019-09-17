import numpy as np
import matplotlib.pyplot as plt
import linear_func

# QtFuzzyLite

class FRBS():
    def __init__(self,
        input_funcs_node_set,
        output_funcs_node_set):
        self.input_funcs_node_set = input_funcs_node_set
        self.output_funcs_node_set = output_funcs_node_set
        self.output_func_set = self.memb_func_builder(self.output_funcs_node_set)
        self.input_func_set = self.memb_func_builder(self.input_funcs_node_set)

    def memb_func_builder(self, node_set):
        """
        node_set = {
            "func_1" : {
                "A" : [[,], [,], [,]],
                "B" : [[,], [,], [,]],
                "C" : [[,], [,]],
            },
            "func_1" : {
                "D" : [[,], [,], [,]],
                "E" : [[,], [,], [,]],
                "F" : [[,], [,]],
            },
            ...
        }

        func_set = {
            "func_1" : <numpy poly1d object>,
            "func_2" : <numpy poly1d object>,
            ...
        }
        """
        func_set = {}
        for cat, nodes in node_set.items():
            memb_funcs = {}
            for k, v in nodes.items():
                lf = linear_func.Linear_Func(v)
                memb_funcs[k] = lf
            func_set[cat] = memb_funcs
        return func_set

    def fuzzification(self, x, func):
        #degrees = [0] * len(node_list)
        degrees = {}

        for k, f in func.items():
            degrees[k] = f.eval_y(x)
            
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
   


