import numpy as np
def solution(n):
    if np.sqrt(n) % 1 == 0 :  # sqrt : 제곱근 함수
        return 1
    else :
        return 2