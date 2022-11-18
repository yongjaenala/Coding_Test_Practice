import numpy as np
def solution(arr):
    arr.pop(np.argmin(arr))
    return ([-1] if len(arr) == 0 else arr)