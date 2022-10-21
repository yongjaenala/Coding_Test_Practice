# https://school.programmers.co.kr/learn/courses/30/lessons/120889
# 삼각형의 완성조건 (1)

def solution(sides):
    answer = 0

    a, b = 0, 0
    for num in sides:
        b += num
        if a < num:
            a = num
    b -= a
    if a < b:
        answer = 1
    else:
        answer = 2

    return answer