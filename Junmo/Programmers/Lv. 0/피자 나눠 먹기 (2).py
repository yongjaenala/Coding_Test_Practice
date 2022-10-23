# https://school.programmers.co.kr/learn/courses/30/lessons/120815
# 피자 나눠 먹기 (2)

def solution(n):
    answer = 0

    i = 0
    while True:
        i += 1
        if (6 * i) % n == 0:
            answer = i
            return answer

    # return answer