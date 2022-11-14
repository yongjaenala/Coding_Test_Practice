def solution(price, money, count):
    mo = price*sum(range(1,count+1)) - money
    if mo > 0 :
        return mo
    else :
        return 0