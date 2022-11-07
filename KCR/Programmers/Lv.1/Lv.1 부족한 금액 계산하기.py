def solution(price, money, count):
    notenough = price*sum(range(1,count+1)) - money
    if notenough > 0 :
        return notenough
    else :
        return 0