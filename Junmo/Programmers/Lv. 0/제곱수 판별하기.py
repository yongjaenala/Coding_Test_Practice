# https://school.programmers.co.kr/learn/courses/30/lessons/120909
# 제곱수 판별하기

import math

def solution(n):
    answer = 0

    if math.sqrt(n) % 1 == 0:
        answer = 1
    else:
        answer = 2

    return answer