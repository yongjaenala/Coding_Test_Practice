# https://school.programmers.co.kr/learn/courses/30/lessons/120903
# 배열의 유사도

def solution(s1, s2):
    answer = 0

    for v1 in s1:
        for v2 in s2:
            if v1 == v2:
                answer += 1

    return answer