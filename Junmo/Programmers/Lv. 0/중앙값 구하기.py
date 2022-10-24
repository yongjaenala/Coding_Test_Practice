# https://school.programmers.co.kr/learn/courses/30/lessons/120811
# 중앙값 구하기

def solution(array):
    answer = 0

    temp = 0
    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] > array[j]:
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
    answer = array[(len(array) + 1) // 2 - 1]

    return answer