# 미해걀
def solution(balls, share):
    answer = 1
    for i in range(balls,share,-1):
        print(i)
        answer *= i
    return answer

balls = 5
share = 3
print(solution(balls,share))