# https://school.programmers.co.kr/learn/courses/30/lessons/120835
# 진료 순서 정하기

import numpy as np

def solution(emergency):
    answer = []

    answer = [0 for i in range(len(emergency))]
    for i in range(1, len(answer) + 1):
        id = np.argmax(emergency)
        answer[id] = i
        emergency[id] = 0

    return answer