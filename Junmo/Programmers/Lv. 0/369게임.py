# https://school.programmers.co.kr/learn/courses/30/lessons/120891#
# 369게임

def solution(order):
    answer = 0

    while True:
        if order % 10 != 0 and (order % 10) % 3 == 0:
            answer += 1
        order //= 10
        if order == 0:
            break

    return answer