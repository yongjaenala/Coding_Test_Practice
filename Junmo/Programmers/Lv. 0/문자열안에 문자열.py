# https://school.programmers.co.kr/learn/courses/30/lessons/120908
# 문자열안에 문자열

def solution(str1, str2):
    answer = 0

    if str1.find(str2) == -1:
        answer = 2
    else:
        answer = 1

    return answer