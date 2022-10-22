def solution(num, total):
    n = (total-sum(range(1,num)))//num
    return list(range(n,n+num))