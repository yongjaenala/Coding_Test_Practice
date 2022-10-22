def solution(n):
    answer = 1
    p = 6
    for i in range(min(n, p)+1,1,-1) :  # 사람 수(n)와 피자 조각(6)의 최소공배수
        if (n%i == 0) & (p%i == 0) :
            answer *= i
            n /= i
            p /= i
    return answer*n*p/6