# https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 피자 나눠 먹기 (3)

import math

def solution(slice, n):
    answer = 0

    answer = math.ceil(n / slice)
    # if n % slice == 0:
    #     answer = n / slice
    # else:
    #     answer = n // slice + 1

    return answer