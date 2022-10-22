import numpy as np
def solution(n):
    if np.sqrt(n) % 1 == 0 :
        return 1
    else :
        return 2