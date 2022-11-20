# 첫 번째 풀이
def solution(s, n):
    answer = ''
    a = 'abcdefghijklmnopqrstuvwxyz'
    for i in s:
        if i == i.upper() and i != ' ':
            answer += a[a.index(i.lower())+n-26].upper()
        elif i != i.upper() and i != ' ':
            answer += a[a.index(i.lower())+n-26]
        else:
            answer += ' '
    return answer

# 두 번째 풀이
def solution(s, n):
    answer = ''
    al = 'abcdefghijklmnopqrstuvwxyz'
    for i in s :
        if (i !=' ') & (i in al) :
            answer += al[(al.index(i)+n+26)%26]
        elif (i != ' ') & (i not in al) :
            answer += al[(al.upper().index(i)+n+26)%26].upper()
        else :
            answer += ' '
    return answer