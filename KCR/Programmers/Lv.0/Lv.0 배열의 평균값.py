# 첫 번째 풀이
def solution(numbers):
    return sum(numbers)/len(numbers)

# 두 번째 풀이
import numpy as np
def solution(numbers):
    return np.mean(numbers)