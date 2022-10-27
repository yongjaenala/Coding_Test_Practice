# https://school.programmers.co.kr/learn/courses/30/lessons/120842
# 2차원으로 만들기

def solution(num_list, n):
    answer = [[]]

    answer = [[0 for i in range(n)] for j in range(len(num_list) // n)]
    for i in range(len(num_list) // n):
        for j in range(n):
            answer[i][j] = num_list[i * n + j]

    return answer