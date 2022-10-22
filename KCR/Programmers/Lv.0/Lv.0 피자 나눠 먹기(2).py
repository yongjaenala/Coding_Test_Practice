def solution(n):
    answer = 1
    p = 6
    for i in range(min(n, p)+1,1,-1) :
        if (n%i == 0) & (p%i == 0) :
            answer *= i
            n /= i
            p /= i
    return answer*n*p/6