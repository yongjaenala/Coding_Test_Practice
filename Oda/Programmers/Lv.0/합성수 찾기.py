def solution(n):
    answer = 0
    for i in range(4, n+1):
        for j in range(2, i):
            if i % j == 0:
                answer += 1
                break
    return answer
# 1~10
# 4,6,8,9,10 = 5개
# 1과 자신을 제외하고도 나누어진다면 합성수
