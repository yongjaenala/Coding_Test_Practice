# https://school.programmers.co.kr/learn/courses/30/lessons/120895
# 인덱스 바꾸기

def solution(my_string, num1, num2):
    answer = ''

    list = [char for char in my_string]
    temp = list[num1]
    list[num1] = list[num2]
    list[num2] = temp
    for char in list:
        answer += char

    return answer