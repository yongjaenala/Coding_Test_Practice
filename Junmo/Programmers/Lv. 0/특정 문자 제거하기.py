# https://school.programmers.co.kr/learn/courses/30/lessons/120826
# 특정 문자 제거하기

def solution(my_string, letter):
    answer = ''

    for i in range(len(my_string)):
        if my_string[i] != letter:
            answer += (my_string[i])

    return answer