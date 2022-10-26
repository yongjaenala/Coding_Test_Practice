# https://school.programmers.co.kr/learn/courses/30/lessons/120825
# 문자 반복 출력하기

def solution(my_string, n):
    answer = ''

    for char in my_string:
        for i in range(n):
            answer += char

    return answer