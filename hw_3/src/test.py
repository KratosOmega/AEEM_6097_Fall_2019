import matplotlib.pyplot as plt
import math

"""
# generate membership tests
x = 0
size = 0.26
end = 0
while end <= 1:
    output = [[x,0], [x + size/2, 1], [x+size, 0]]
    print(output)
    end = x+size
    x = x + size/2
    #step += size
"""


x = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4
}

v = x.values()
m = max(v)


k = list(x.keys())[list(x.values()).index(m)]

print(k)

