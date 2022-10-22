# 첫 번째 풀이
import numpy as np
def solution(n):
    return np.ceil(n/7)

# 두 번째 풀이 : 함수X
def solution(n):
    if n%7 != 0 :
        return (n//7)+1
    else :
        return n//7