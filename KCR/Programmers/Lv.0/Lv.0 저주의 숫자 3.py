def solution(n):
    num = 0
    cnt = 0
    while cnt < n :
        num += 1
        if (num%3 != 0) and ('3' not in str(num)) :
            cnt +=1
    return num