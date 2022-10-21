# https://school.programmers.co.kr/learn/courses/30/lessons/120817
# 배열의 평균값

def solution(numbers):
    answer = 0

    for number in numbers:
        answer += number

    answer /= len(numbers)

    return answer