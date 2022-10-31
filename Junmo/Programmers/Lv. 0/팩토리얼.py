# https://school.programmers.co.kr/learn/courses/30/lessons/120848
# 팩토리얼

def factorial(n):
    if n <= 1:
        return 1
    return factorial(n - 1) * n

def solution(n):
    answer = 0

    for i in range(1, 11):
        if n >= factorial(i):
            answer += 1
        else:
            break

    return answer