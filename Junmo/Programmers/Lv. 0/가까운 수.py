# https://school.programmers.co.kr/learn/courses/30/lessons/120890#
# 가까운 수

def solution(array, n):
    answer = 0

    temp = []
    for i in range(len(array)):
        temp.append(abs(array[i] - n))

    for i in range(len(array)):
        if array[i] == n - min(temp):
            answer = array[i]
            break
        elif array[i] == n + min(temp):
            answer = array[i]

    return answer