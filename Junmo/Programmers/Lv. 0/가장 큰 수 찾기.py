# https://school.programmers.co.kr/learn/courses/30/lessons/120899
# 가장 큰 수 찾기

def solution(array):
    answer = []

    answer = [0, 0]
    for i in range(len(array)):
        if answer[0] < array[i]:
            answer[0] = array[i]
            answer[1] = i

    return answer