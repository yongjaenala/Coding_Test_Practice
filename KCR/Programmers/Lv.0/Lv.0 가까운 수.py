import numpy as np
def solution(array, n):
    diff = []
    array = sorted(array)
    for i in array :
        diff.append(abs(n-i))
    return array[np.argmin(diff)]