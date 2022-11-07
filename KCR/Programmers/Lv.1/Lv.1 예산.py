import numpy as np
def solution(d, budget):
    cnt = 0
    sum = 0
    for i in range(len(d)) :
        sum += min(d)
        if sum > budget :
            break
        d.pop(np.argmin(d))
        cnt += 1
    return cnt