# 첫 번째 풀이
def solution(s):
    p = 0
    y = 0
    for i in s :
        if i.lower() == 'p' :
            p += 1
        elif i.lower() == 'y' :
            y += 1
    return y==p

# 두 번째 풀이
def solution(s) :
    return s.lower().count('p') == s.lower().count('y')