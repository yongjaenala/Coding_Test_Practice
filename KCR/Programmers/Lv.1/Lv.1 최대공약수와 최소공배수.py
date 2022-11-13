def solution(n, m):
    g = 1
    l = 1
    for i in range(min(m, n),0, -1) :
        if (n%i == 0) & (m%i == 0) :
            g *= i
            l *= i
            n = n//i
            m = m//i
    l *= m*n
    return [g, l]