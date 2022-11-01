def solution(order):
    cnt = 0
    for i in ['3', '6' , '9'] :
        cnt += str(order).count(i)
    return cnt