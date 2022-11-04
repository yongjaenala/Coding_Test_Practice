def solution(food):
    me = ''
    you = ''
    for i in range(1, len(food)) :
        both = food[i]//2
        me += str(i)*both
        you = str(i)*both + you
    return me+'0'+you