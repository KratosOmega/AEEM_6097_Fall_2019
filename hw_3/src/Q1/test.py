import matplotlib.pyplot as plt
import math

x = 0

gap = 0.001
num = 7
size = 1/7 - gap
end = 0
while end <= 1:
    output = [[x,0], [x + size/2, 1], [x+size, 0]]
    print(output)
    end = x+size
    x = x + (size - gap)
    #step += size

