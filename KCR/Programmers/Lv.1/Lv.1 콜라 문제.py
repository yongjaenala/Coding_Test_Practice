def solution(a, b, n):
    # n : 가지고 있는 병
    # a : 줘야 하는 병의 개수
    # b : 받게 되는 병의 개수
    cnt = 0
    while n >= a :
        cnt += n//a*b
        n = n//a*b + n%a
    return cnt