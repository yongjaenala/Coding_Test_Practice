# https://school.programmers.co.kr/learn/courses/30/lessons/120846
# 합성수 찾기

def solution(n):
    answer = 0

    for i in range(n, 1, -1):
        count = 0
        for j in range(n, 1, -1):
            if i % j == 0:
                count += 1
            if count >= 2:
                break
        if count == 2:
            answer += 1

    return answer