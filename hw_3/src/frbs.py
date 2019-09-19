import numpy as np
import matplotlib.pyplot as plt
import linear_func
import operator

# QtFuzzyLite

class FRBS():
    def __init__(self,
        input_funcs_node_set,
        output_funcs_node_set,
        precision):
        self.input_funcs_node_set = input_funcs_node_set
        self.output_funcs_node_set = output_funcs_node_set
        self.output_func_set = self.memb_func_builder(self.output_funcs_node_set)
        self.input_func_set = self.memb_func_builder(self.input_funcs_node_set)
        self.precision = precision

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

    def defuzzification(self, fuzzified_input, evaled_rules, output_cat):
        numerator = 0
        denominator = 0

        for i, r in enumerate(evaled_rules):
            # 0.8
            degree = r[1]
            output_func = self.output_func_set[output_cat][r[0]]

            if degree != None:
                w, cog = self.cog(output_func, self.precision, degree)
                numerator += (w * cog)
                denominator += w

        cog_aggregated = numerator / denominator

        return cog_aggregated

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

    def rules_eval(self, fuzzified_input, rules):
        evaled_rules = []
        clean_input = self.remove_none(fuzzified_input)

        for r in rules:
            AND = r[0].split("+")
            OR = r[0].split("-")
            """
            print("-----------")
            print(r)
            print(AND)
            print(OR)
            print("-----------")
            """
            # 1-to-1 operation
            if len(AND) == 1 and len(OR) == 1:
                try:
                    evaled_rules.append([r[1], clean_input[r[0]]])
                except:
                    pass

            if len(AND) > 1:
                degrees = {}
                try:
                    for p in AND:
                        degrees.append(clean_input[p])
                    evaled_degree = min(degrees)
                    evaled_rules.append([r[1], evaled_degree])
                except:
                    pass

            if len(OR) > 1:
                degrees = {}
                try:
                    """
                    for p in OR:
                        degrees.append(clean_input[p])
                    evaled_degree = max(degrees)
                    evaled_rules.append([r[1], evaled_degree])
                    """
                    for p in OR:
                        if p in clean_input.keys():
                            if clean_input[p] > self.precision:
                                degrees[p] = clean_input[p]

                    if len(degrees) != 0:
                        op = max(degrees.values())
                        key = list(degrees.keys())[list(degrees.values()).index(op)]
                        evaled_rules.append([r[1], clean_input[key]])
                except:
                    pass

        return evaled_rules

"""
if __name__ == '__main__':
"""


