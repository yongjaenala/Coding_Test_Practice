def solution(n):
    answer = 0

    slice = 1

    while True:

        if n * slice % 6 == 0:
            answer = n * slice / 6
            break
        else:
            slice += 1

    return answer