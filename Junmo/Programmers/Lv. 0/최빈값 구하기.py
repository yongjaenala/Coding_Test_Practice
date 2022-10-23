# 미완
#
# 최빈값 구하기

import numpy as np

def solution(array):
    answer = 0

    frequency = [0 for i in range(max(array))]
    maxFreq = -1
    temp = -1

    for num in array:
        frequency[num] += 1
    maxFreq = frequency[np.argmax(frequency)]
    while maxFreq == frequency[np.argmax(frequency)]:
        frequency[np.argmax(frequency)] = 0
        if maxFreq == np.argmax(frequency):
            answer += 1


    return answer

