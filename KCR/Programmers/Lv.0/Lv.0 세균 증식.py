# 첫 번째 풀이
def solution(n, t):
    for i in range(t) :
        n *= 2
    return n

# 두 번째 풀이
def solution(n, t):
    return n*(t**2)

# 세 번째 풀이
def solution(n, t):
    return n << t  # 비트 연산자 : # a * 2ⁿ
# 10 << 1 = 20
# 10 >> 1 = 5
