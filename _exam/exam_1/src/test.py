 import numpy
>>> p = numpy.poly1d([2, 4, 6])
>>> print p
   2
2 x + 4 x + 6
>>> i = p.integ()
>>> i
poly1d([ 0.66666667,  2.        ,  6.        ,  0.        ])
>>> integrand = i(1) - i(0) # Use call notation to evaluate a poly1d
>>> integrand
8.6666666666666661