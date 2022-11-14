# https://school.programmers.co.kr/learn/courses/30/lessons/120888
# 중복된 문자 제거

def solution(my_string):
    answer = ''

    temp = 0
    for i in range(len(my_string)):
        for j in range(0, i):
            if my_string[i] == my_string[j]:
                temp += 1
        if temp == 0:
            answer += my_string[i]
        temp = 0

    return answer