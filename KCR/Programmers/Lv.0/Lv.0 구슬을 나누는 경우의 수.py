def solution(balls, share):
    answer = 1
    for i in range(balls, balls - share, -1):
        answer *= i

    for i in range(share, 0, -1):
        answer /= i
    return round(answer)