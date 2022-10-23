# https://school.programmers.co.kr/learn/courses/30/lessons/120849
# 모음 제거

def solution(my_string):
    answer = ''

    vowel = ['a', 'e', 'i', 'o', 'u']
    for string in my_string:
        if string not in vowel:
            answer += string

    return answer