# https://school.programmers.co.kr/learn/courses/30/lessons/120847
# 최댓값 만들기(1)

def solution(numbers):
    answer = 0

    for i in range(len(numbers) - 1):
        for j in range(i + 1, len(numbers)):
            temp = numbers[i] * numbers[j]
            if answer < temp:
                answer = temp

    return answer