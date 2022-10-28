# https://school.programmers.co.kr/learn/courses/30/lessons/120843
# 공 던지기

def solution(numbers, k):
    answer = 0

    temp = 2 * k - 1
    if temp >= len(numbers):
        temp %= len(numbers)
    answer = numbers[temp - 1]

    return answer