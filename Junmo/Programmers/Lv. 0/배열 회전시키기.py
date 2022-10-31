# https://school.programmers.co.kr/learn/courses/30/lessons/120844
# 배열 회전시키기

def solution(numbers, direction):
    answer = []

    if direction == "left":
        for i in range(1, len(numbers)):
            answer.append(numbers[i])
        answer.append(numbers[0])
    else:
        answer.append(numbers[len(numbers) - 1])
        for i in range(0, len(numbers) - 1):
            answer.append(numbers[i])

    return answer