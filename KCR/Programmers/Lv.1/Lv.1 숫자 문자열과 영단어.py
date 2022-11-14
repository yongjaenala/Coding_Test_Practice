def solution(s):
    dic = {'zero' : 0, 'one' : 1, 'two' : 2, 'three' :3, 'four':4, 'five' :5, 'six' : 6, 'seven' : 7, 'eight' :8,'nine' :9}
    answer = ''
    i = 1
    while len(s) > 0 :
        try :
            answer += str(int(s))
            break
        except :
            if s[:i] in dic.keys() :
                answer += str(int(dic[s[:i]]))
                s = s[i:]
                i = 1
            elif s[:i] in list(map(str, range(10))) :
                answer += str(s[:i])
                s = s[i:]
                i = 1
            else :
                i += 1
    return answer