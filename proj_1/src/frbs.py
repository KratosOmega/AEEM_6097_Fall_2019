import numpy as np
import matplotlib.pyplot as plt
from linear_func import Linear_Func
import operator

# QtFuzzyLite

class FRBS():
    def __init__(self,
        input_funcs_node_set,
        output_funcs_node_set,
        precision):
        self.input_funcs_node_set = input_funcs_node_set
        self.output_funcs_node_set = output_funcs_node_set
        self.input_func_set = self.memb_func_builder(self.input_funcs_node_set)
        self.output_func_set = self.memb_func_builder(self.output_funcs_node_set)
        self.precision = precision

    def memb_func_builder(self, node_set):
        func_set = {}
        for cat, nodes in node_set.items():
            memb_funcs = {}
            for k, v in nodes.items():
                lf = Linear_Func(v)
                memb_funcs[k] = lf
            func_set[cat] = memb_funcs

        return func_set

    def mu(self, inp_x):
        winner = max(inp_x.values())
        key = list(inp_x.keys())[list(inp_x.values()).index(winner)]
        return key, inp_x[key]

    def fuzzification(self, x, func):
        #degrees = [0] * len(node_list)
        degrees = {}

        for k, v in x.items():
            degrees[k] = {}
            for i, x_f in func[k].items():
                y = x_f.eval_y(v)
                if y != None and y > self.precision:
                    degrees[k][i] = y

        return degrees

    def cleaning(self, degrees):
        for k in degrees.keys():
            if degrees[k] != None:
                if degrees[k] > 0.0 and degrees[k] < 1e-10:
                    degrees[k] = None

        return degrees

    def defuzzification(self, evaled_rules, output_cat):
        try: 
            numerator = 0
            denominator = 0

            for f, degree in evaled_rules.items():
                output_func = self.output_func_set[output_cat][str(f)]
                w, cog = self.cog(output_func, self.precision, degree)
                numerator += (w * cog)
                denominator += w

            cog_aggregated = numerator / denominator

            return cog_aggregated
        except:
            return 0

    def cog(self, func, precision, degree):
        """
        given a complete part of a member function with a degree
        return the cog
        """
        numerator = 0
        denominator = 0
        weight = 0

        for idx, interval in func.range_map.items():
            pointer = interval[0]
            destination = interval[1]
            while pointer < destination:
                a = min(degree, func.memb_func[idx](pointer))
                b = min(degree, func.memb_func[idx](pointer + precision))
                pointer += precision
                weight += (a + b) * precision / 2
                numerator += (a + b) * pointer / 2
                denominator += ((a + b) / 2)
        cog = numerator / denominator
        return weight, cog

    def remove_none(self, dirty_input):
        clean_input = {}

        for k in dirty_input.keys():
            if dirty_input[k]:
                clean_input[k] = dirty_input[k]

        return clean_input


    def rule_op(self):
        return False

    def rule_mat_eval(self, fuzzified_input, rule_mat):
        evaled_rules = {}
        x_pool = fuzzified_input["X"]
        y_pool = fuzzified_input["Y"]

        for x_k, x in x_pool.items():
            for y_k, y in y_pool.items():
                output_func_idx = int(rule_mat[int(x_k), int(y_k)])
                degree = min(x, y)
                if output_func_idx in evaled_rules.keys():
                    if evaled_rules[output_func_idx] < degree:
                        evaled_rules[output_func_idx] = degree
                else:
                    evaled_rules[output_func_idx] = degree
        return evaled_rules

"""
if __name__ == '__main__':
"""


