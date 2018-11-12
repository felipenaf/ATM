import random
from time import time as t

def xrange(x):
    return iter(range(x))

def nrConta():                                                                                             
    n = [random.randrange(10) for i in xrange(9)]                                                                                              
    return "%d%d.%d%d%d%d%d%d.%d" % tuple(n)
