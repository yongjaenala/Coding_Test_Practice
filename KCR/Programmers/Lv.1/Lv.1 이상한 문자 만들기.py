def solution(s):
    s = s.split(' ')
    for i in s :
        l = ''
        for j, a in enumerate(i) :
            if j%2 == 0 :
                l += a.upper()
            else :
                l += a.lower()
        s[s.index(i)] = l
    return ' '.join(s)