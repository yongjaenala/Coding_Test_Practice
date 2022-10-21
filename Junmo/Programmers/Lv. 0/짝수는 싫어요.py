# https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 짝수는 싫어요

def solution(n):
    answer = []

    for i in range(1, n + 1, 2):
        answer.append(i)

    return answer