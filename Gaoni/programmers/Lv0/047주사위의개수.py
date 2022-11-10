def solution(box, n):
    box_n = [int(i / n) for i in box]

    answer = 1

    for i in box_n:
        answer = answer * i

    return answer