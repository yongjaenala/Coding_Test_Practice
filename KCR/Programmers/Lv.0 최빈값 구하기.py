import numpy as np
def solution(array):
    if len(array) == 1:
        return array[0]

    a = [0]*(max(array)+1)  

    for i in array :
        a[i] += 1
    mx = int(np.argmax(a))
    mx_v = max(a)
    a[mx] = 0
    if mx_v == max(a) :
        return -1
    return mx