# https://school.programmers.co.kr/learn/courses/30/lessons/120911
# 문자열 정렬하기 (2)

def solution(my_string):
    answer = ''

    my_string = my_string.lower()
    for word in sorted(my_string):
        answer += word

    return answer