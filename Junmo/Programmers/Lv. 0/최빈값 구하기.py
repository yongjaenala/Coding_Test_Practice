# https://school.programmers.co.kr/learn/courses/30/lessons/120812
# 최빈값 구하기

import numpy as np

def solution(array):
    answer = 0

    frequency = [0 for i in range(max(array)+1)]
    maxFreq = -1
    maxFreqIndex = -1
    temp = -1

    for num in array:
        frequency[num] += 1

    maxFreq = frequency[np.argmax(frequency)]
    maxFreqIndex = np.argmax(frequency)
    frequency[int(maxFreqIndex)] = 0

    if maxFreq == frequency[np.argmax(frequency)]:
        answer = -1
    else:
        answer = int(maxFreqIndex)

    return answer