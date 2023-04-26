import random
import math
import time

def add(i, j):
    cdef list ret = []
    for i in range(100*10000):
        ret.append(math.sin(random.uniform(2.0, 100.0)))
    return ret



