# https://school.programmers.co.kr/learn/courses/30/lessons/120910
# 세균 증식

def solution(n, t):
    answer = 0

    answer = n
    for i in range(t):
        answer *= 2

    return answer