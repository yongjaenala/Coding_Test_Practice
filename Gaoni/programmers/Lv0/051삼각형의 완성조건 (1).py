def solution(sides):
    answer = 0

    result = sum(sides) - max(sides) * 2

    if result > 0:
        answer = 1
    else:
        answer = 2

    return answer