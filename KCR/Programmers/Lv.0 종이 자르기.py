def solution(M, N):
    answer = 0
    if (M == 1) & (N == 1):
        return 0
    else:
        if N > M:
            N, M = M, N
        answer += (M - 1)
        answer += (N - 1) * M
    return answer
