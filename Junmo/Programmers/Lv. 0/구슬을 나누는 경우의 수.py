# 미완
# https://school.programmers.co.kr/learn/courses/30/lessons/120840
# 구슬을 나누는 경우의 수

def factorial(n):
    if n <= 1:
        return 1
    return factorial(n - 1) * n

def solution(balls, share):
    answer = 0

    answer = factorial(balls) / (factorial(share) * factorial(balls - share))

    return answer