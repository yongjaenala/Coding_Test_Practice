def solution(a, b):
    for i in range(max(a,b), 0, -1) :
        if (a%i == 0) & (b%i == 0) :
            a = a//i
            b = b//i
    while True :
        if b%2 == 0 :
            b = b//2
        elif b%5 == 0 :
            b = b//5
        else :
            break
    if b != 1 :
        return 2
    else :
        return 1