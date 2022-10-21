# https://school.programmers.co.kr/learn/courses/30/lessons/120583
# 중복된 숫자 개수

def solution(array, n):
    answer = 0

    for i in array:
        if i == n:
            answer += 1

    return answer