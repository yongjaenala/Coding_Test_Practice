def solution(balls, share):
    answer = 0

    fac = [i for i in range(31)]
    fac[0] = 1
    for i in fac:
        fac[i] = fac[i - 1] * fac[i]

    answer = fac[balls] / (fac[balls - share] * fac[share])

    return answer