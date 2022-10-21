# https://school.programmers.co.kr/learn/courses/30/lessons/120822
# 문자열 뒤집기

def solution(my_string):
    answer = ''

    for i in range(len(my_string)):
        answer += my_string[len(my_string) - 1 - i]

    return answer