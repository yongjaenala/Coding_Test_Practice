# https://school.programmers.co.kr/learn/courses/30/lessons/120904
# 숫자 찾기

def solution(num, k):
    answer = 0

    for c in str(num):
        if c != str(k):
            answer += 1
        else:
            answer += 1
            return answer
    answer = -1

    return answer