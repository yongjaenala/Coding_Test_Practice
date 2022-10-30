def solution(s):
    answer = 0
    before = []
    s = s.split()
    if s[0] == 'Z' :
        s[0] = '0'
    for i in s :
        if i == 'Z' :
            if len(before) == 0 :
                answer -= 0
            else :
                answer -= before[-1]
                before.pop(-1)
            continue
        answer += int(i)
        before.append(int(i))
    return answer