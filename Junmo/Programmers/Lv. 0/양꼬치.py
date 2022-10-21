#
# 양꼬치

def solution(n, k):
    answer = 0

    answer = n * 12000 + k * 2000
    answer -= (n // 10) * 2000

    return answer