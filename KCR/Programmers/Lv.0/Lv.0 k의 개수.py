def solution(i, j, k):
    cnt = 0
    for n in range(i, j+1) :
        if str(k) in str(n) :
            cnt += str(n).count(str(k))
    return cnt