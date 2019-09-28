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
        self.output_func_set = self.mf_builder(self.output_funcs_node_set)
        self.input_func_set = self.mf_builder(self.input_funcs_node_set)
        self.precision = precision

    def mf_builder(self, node_set):
        func_set = {}
        for cat, nodes in node_set.items():
            mfs = {}
            for k, v in nodes.items():
                lf = linear_func.Linear_Func(v)
                mfs[k] = lf
            func_set[cat] = mfs

        return func_set

    def mu(self, inp_x):
        winner = max(inp_x.values())
        key = list(inp_x.keys())[list(inp_x.values()).index(winner)]
        return key, inp_x[key]

    def fuzzification(self, x, func):
        #degrees = [0] * len(node_list)
        degrees = {}

        for k, v in x.items():
            for i, x_f in func[k].items():
                y = x_f.eval_y(v)
                if y != None and y > self.precision:
                    degrees[k + "=" + i] = y

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

            for y, degree in evaled_rules.items():
                output_func = self.output_func_set[output_cat][y]
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
                a = min(degree, func.mf[idx](pointer))
                b = min(degree, func.mf[idx](pointer + precision))
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

    def rules_eval(self, fuzzified_input, rules, special_op = ""):
        evaled_rules = {}
        clean_input = self.remove_none(fuzzified_input)

        for r in rules:
            AND = r[0].split("+")
            OR = r[0].split("-")

            # 1-to-1 operation
            # TODO!
            if len(AND) == 1 and len(OR) == 1:
                try:
                    evaled_rules[r[1]] = fuzzified_input[r[0]]
                except:
                    pass

            if len(AND) > 1:
                not_fire = False
                degrees = []
                for p in AND:
                    try:
                        degrees.append(fuzzified_input[p])
                    except:
                        not_fire = True
                        pass

                if not not_fire:
                    evaled_degree = min(degrees)

                    # Q4 operation
                    if special_op == "max_prod_comp":
                        evaled_degree = np.prod(degrees)

                    evaled_rules[r[1]] = evaled_degree

            # TODO!
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


