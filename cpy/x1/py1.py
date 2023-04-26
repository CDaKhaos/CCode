import random
import math
import time

def add(i, j):
    start_t = time.time()
    ret = list()
    for i in range(100*10000):
        ret.append(math.sin(random.uniform(2.0, 100.0)))
    # print(time.time() - start_t)
    return ret

if __name__ == "__main__":
    # print(add(1, 2))
    add(1, 2)
