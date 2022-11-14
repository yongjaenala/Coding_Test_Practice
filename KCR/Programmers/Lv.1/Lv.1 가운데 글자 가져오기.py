# 첫 번째 풀이
def solution(s):
    if len(s)%2 == 0 :
        return s[len(s)//2-1 : len(s)//2 +1]
    else :
        return s[len(s)//2]

# 두 번째 풀이
def solution(s):
    return s[(len(s)-1)//2:len(s)//2+1]