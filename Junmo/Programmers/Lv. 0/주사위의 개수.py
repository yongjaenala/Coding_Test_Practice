# https://school.programmers.co.kr/learn/courses/30/lessons/120845
# 주사위의 개수

def solution(box, n):
    answer = 1

    temp = [0 for i in range(3)]
    for i in range(3):
        temp[i] = box[i] // n
    for i in range(3):
        answer *= temp[i]

    return answer