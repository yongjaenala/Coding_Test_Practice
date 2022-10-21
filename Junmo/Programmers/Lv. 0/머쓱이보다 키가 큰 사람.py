# https://school.programmers.co.kr/learn/courses/30/lessons/120585
# 머쓱이보다 키가 큰 사람

def solution(array, height):
    answer = 0

    for i in array:
        if height < i:
            answer += 1

    return answer